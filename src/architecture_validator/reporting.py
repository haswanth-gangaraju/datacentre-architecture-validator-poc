from __future__ import annotations

from .models import ArchitectureProposal, ValidationFinding


def _severity_rank(severity: str) -> int:
    order = {"HIGH": 0, "MEDIUM": 1, "LOW": 2}
    return order.get(severity, 99)


def render_markdown_report(
    proposal: ArchitectureProposal, findings: list[ValidationFinding]
) -> str:
    ordered = sorted(findings, key=lambda item: (_severity_rank(item.severity), item.code))
    overall = "PASS" if not ordered else "FAIL"

    lines: list[str] = []
    lines.append(f"# Architecture Review - {proposal.proposal_name}")
    lines.append("")
    lines.append(f"- Region: {proposal.region}")
    lines.append(f"- Overall Result: **{overall}**")
    lines.append("")

    if not ordered:
        lines.append("## Findings")
        lines.append("- No issues detected against configured guardrails.")
        return "\n".join(lines)

    lines.append("## Findings")
    for idx, finding in enumerate(ordered, start=1):
        lines.append(
            f"{idx}. [{finding.severity}] `{finding.code}` - {finding.message}"
        )

    lines.append("")
    lines.append("## Recommended Actions")
    for idx, finding in enumerate(ordered, start=1):
        lines.append(f"{idx}. {finding.remediation}")

    return "\n".join(lines)
