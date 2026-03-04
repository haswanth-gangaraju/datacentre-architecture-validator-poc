from __future__ import annotations

import argparse
import json
from pathlib import Path

from src.architecture_validator.models import ArchitectureProposal
from src.architecture_validator.reporting import render_markdown_report
from src.architecture_validator.validator import validate_proposal


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate a data centre architecture proposal and generate a report."
    )
    parser.add_argument("--input", required=True, help="Path to JSON proposal file.")
    parser.add_argument("--output", required=True, help="Output markdown report path.")
    args = parser.parse_args()

    raw = json.loads(Path(args.input).read_text(encoding="utf-8"))
    proposal = ArchitectureProposal.from_dict(raw)
    findings = validate_proposal(proposal)
    report = render_markdown_report(proposal, findings)

    Path(args.output).write_text(report, encoding="utf-8")
    print(f"Report generated: {args.output}")
    print(f"Findings: {len(findings)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
