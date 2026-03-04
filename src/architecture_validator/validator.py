from __future__ import annotations

from .models import ArchitectureProposal, ValidationFinding

REQUIRED_POWER_REDUNDANCY = {"2N", "N+1"}
REQUIRED_NETWORK_REDUNDANCY = {"dual", "multi-path"}
MIN_POWER_HEADROOM_PERCENT = 20.0
MIN_COOLING_HEADROOM_PERCENT = 15.0


def validate_proposal(proposal: ArchitectureProposal) -> list[ValidationFinding]:
    findings: list[ValidationFinding] = []

    if proposal.power_redundancy not in REQUIRED_POWER_REDUNDANCY:
        findings.append(
            ValidationFinding(
                severity="HIGH",
                code="POWER_REDUNDANCY",
                message=f"Power redundancy '{proposal.power_redundancy}' is below expected standard.",
                remediation="Target at least N+1 (or 2N) power topology before sign-off.",
            )
        )

    if proposal.network_redundancy not in REQUIRED_NETWORK_REDUNDANCY:
        findings.append(
            ValidationFinding(
                severity="HIGH",
                code="NETWORK_REDUNDANCY",
                message=f"Network redundancy '{proposal.network_redundancy}' is not resilient enough.",
                remediation="Provide dual-homed or multi-path network architecture.",
            )
        )

    if proposal.power_headroom_percent < MIN_POWER_HEADROOM_PERCENT:
        findings.append(
            ValidationFinding(
                severity="MEDIUM",
                code="POWER_HEADROOM",
                message=f"Power headroom {proposal.power_headroom_percent:.1f}% is below {MIN_POWER_HEADROOM_PERCENT:.1f}%.",
                remediation="Re-size power envelope or reduce peak load assumptions.",
            )
        )

    if proposal.cooling_headroom_percent < MIN_COOLING_HEADROOM_PERCENT:
        findings.append(
            ValidationFinding(
                severity="MEDIUM",
                code="COOLING_HEADROOM",
                message=f"Cooling headroom {proposal.cooling_headroom_percent:.1f}% is below {MIN_COOLING_HEADROOM_PERCENT:.1f}%.",
                remediation="Increase cooling capacity or optimize rack density layout.",
            )
        )

    if not proposal.has_hld or not proposal.has_lld:
        findings.append(
            ValidationFinding(
                severity="MEDIUM",
                code="DOC_COMPLETENESS",
                message="Architecture documentation is incomplete (HLD/LLD missing).",
                remediation="Provide both HLD and LLD before implementation approval.",
            )
        )

    if not proposal.includes_iac_plan:
        findings.append(
            ValidationFinding(
                severity="LOW",
                code="IAC_PLAN",
                message="No Infrastructure as Code delivery plan included.",
                remediation="Add Terraform/Ansible implementation plan for repeatable rollout.",
            )
        )

    if not proposal.includes_failover_test_plan:
        findings.append(
            ValidationFinding(
                severity="LOW",
                code="FAILOVER_TEST",
                message="Failover test plan is missing.",
                remediation="Define failover scenario testing and pass criteria.",
            )
        )

    return findings
