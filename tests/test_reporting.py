from src.architecture_validator.models import ArchitectureProposal, ValidationFinding
from src.architecture_validator.reporting import render_markdown_report


def test_report_includes_fail_when_findings_exist() -> None:
    proposal = ArchitectureProposal.from_dict({"proposal_name": "Edge Build", "region": "London"})
    findings = [
        ValidationFinding(
            severity="HIGH",
            code="NETWORK_REDUNDANCY",
            message="Insufficient network resiliency.",
            remediation="Add dual path network design.",
        )
    ]
    report = render_markdown_report(proposal, findings)
    assert "Overall Result: **FAIL**" in report
    assert "NETWORK_REDUNDANCY" in report
    assert "Add dual path network design." in report


def test_report_pass_without_findings() -> None:
    proposal = ArchitectureProposal.from_dict({"proposal_name": "Ready Build", "region": "London"})
    report = render_markdown_report(proposal, [])
    assert "Overall Result: **PASS**" in report
    assert "No issues detected" in report
