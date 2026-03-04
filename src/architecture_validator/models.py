from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ArchitectureProposal:
    proposal_name: str
    region: str
    power_redundancy: str
    network_redundancy: str
    power_headroom_percent: float
    cooling_headroom_percent: float
    has_hld: bool
    has_lld: bool
    includes_iac_plan: bool
    includes_failover_test_plan: bool

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "ArchitectureProposal":
        return cls(
            proposal_name=str(raw.get("proposal_name", "Unnamed Proposal")),
            region=str(raw.get("region", "unknown")),
            power_redundancy=str(raw.get("power_redundancy", "N")),
            network_redundancy=str(raw.get("network_redundancy", "single")),
            power_headroom_percent=float(raw.get("power_headroom_percent", 0.0)),
            cooling_headroom_percent=float(raw.get("cooling_headroom_percent", 0.0)),
            has_hld=bool(raw.get("has_hld", False)),
            has_lld=bool(raw.get("has_lld", False)),
            includes_iac_plan=bool(raw.get("includes_iac_plan", False)),
            includes_failover_test_plan=bool(raw.get("includes_failover_test_plan", False)),
        )


@dataclass(frozen=True)
class ValidationFinding:
    severity: str
    code: str
    message: str
    remediation: str
