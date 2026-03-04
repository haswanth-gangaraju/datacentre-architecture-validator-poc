from src.architecture_validator.models import ArchitectureProposal
from src.architecture_validator.validator import validate_proposal


def test_validator_flags_expected_issues() -> None:
    proposal = ArchitectureProposal.from_dict(
        {
            "proposal_name": "Bad Design",
            "region": "London",
            "power_redundancy": "N",
            "network_redundancy": "single",
            "power_headroom_percent": 10,
            "cooling_headroom_percent": 8,
            "has_hld": True,
            "has_lld": False,
            "includes_iac_plan": False,
            "includes_failover_test_plan": False,
        }
    )

    findings = validate_proposal(proposal)
    codes = {item.code for item in findings}

    assert "POWER_REDUNDANCY" in codes
    assert "NETWORK_REDUNDANCY" in codes
    assert "POWER_HEADROOM" in codes
    assert "COOLING_HEADROOM" in codes
    assert "DOC_COMPLETENESS" in codes
    assert "IAC_PLAN" in codes
    assert "FAILOVER_TEST" in codes


def test_validator_passes_resilient_design() -> None:
    proposal = ArchitectureProposal.from_dict(
        {
            "proposal_name": "Good Design",
            "region": "London",
            "power_redundancy": "2N",
            "network_redundancy": "dual",
            "power_headroom_percent": 25,
            "cooling_headroom_percent": 20,
            "has_hld": True,
            "has_lld": True,
            "includes_iac_plan": True,
            "includes_failover_test_plan": True,
        }
    )
    assert validate_proposal(proposal) == []
