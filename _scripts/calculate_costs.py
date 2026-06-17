#!/usr/bin/env python3
"""Write `_stats/cost.json` mapping each instance to its cost.

Reads every task's `<iid>/<iid>.traj.json` in this run. Only `cost_from_traj` is
trajectory-format-specific; adapt it for other agents and the output shape stays the same.
"""

import json
from pathlib import Path

RUN_DIR = Path(__file__).resolve().parent.parent


def cost_from_traj(traj: dict) -> float | None:
    """mini-swe-agent format: info.model_stats.instance_cost. Adapt for other agents."""
    return traj.get("info", {}).get("model_stats", {}).get("instance_cost")


costs = {}
for traj in sorted(RUN_DIR.glob("[!_]*/*.traj.json")):
    value = cost_from_traj(json.loads(traj.read_text()))
    if value is not None:
        costs[traj.parent.name] = value

(RUN_DIR / "_stats").mkdir(exist_ok=True)
(RUN_DIR / "_stats" / "cost.json").write_text(json.dumps(costs, indent=2, sort_keys=True))
print(f"Wrote _stats/cost.json for {len(costs)} instance(s)")
