# Data Centre Architecture Validator POC

Role-aligned POC for `Data Centre Architect - 12 Months - Hybrid` (Hamilton Barnes).

## What It Does
- Validates architecture proposals against practical guardrails:
  - Redundancy (power/network path expectations)
  - Power headroom threshold checks
  - Cooling headroom threshold checks
  - Documentation completeness checks
- Produces deterministic risk findings and remediation actions.
- Generates markdown summary output for stakeholder review.

## Why It Matches The Role
- Mirrors architecture review activity before HLD/LLD sign-off.
- Encodes design standards for resilience and operability.
- Provides communication-ready output for non-implementation stakeholders.

## Quick Start
```bash
python -m pip install -r requirements.txt
python main.py --input sample_architecture.json --output architecture_review.md
pytest -q
```

## Sample Output
The generated report includes:
- Overall result (`PASS`/`FAIL`)
- Severity-tagged findings
- Prioritized remediation actions

