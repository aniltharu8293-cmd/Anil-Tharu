# main.py
# PPMS Prototype — Scenario Orchestrator
# Runs all three scenarios and prints decision tables + summary statistics
# Exports results to CSV

import pandas as pd
from projects   import PROJECTS
from resources  import SCENARIOS
from phase1     import phase1_evaluate, PHASE1_THRESHOLD
from phase2     import phase2_check, consume_resources
from decision   import record_decision, summarise_results

import sys
sys.stdout.reconfigure(encoding='utf-8')


def run_scenario(scenario: dict, projects: list) -> tuple:
    """
    Run a full two-phase PPMS evaluation for one scenario.

    Args:
        scenario: dict with name, budget_pool, skills
        projects: list of project dicts

    Returns:
        (records list, summary dict)
    """
    resources   = scenario["skills"].copy()
    budget_pool = scenario["budget_pool"]
    records     = []

    for proj in projects:
        # ── PHASE 1: Strategic Screening 
        p1 = phase1_evaluate(proj)

        if not p1["phase1_passed"]:
            # Project rejected at Phase 1 — does NOT proceed to Phase 2
            records.append(record_decision(
                project        = proj,
                phase1_score   = p1["phase1_score"],
                phase1_outcome = p1["phase1_outcome"],
                final_decision = "Rejected",
                reason         = p1["phase1_reason"]
            ))
            continue

        # ── PHASE 2: Feasibility Assessment 
        outcome, reason = phase2_check(proj, resources, budget_pool)

        records.append(record_decision(
            project        = proj,
            phase1_score   = p1["phase1_score"],
            phase1_outcome = p1["phase1_outcome"],
            final_decision = outcome,
            reason         = reason
        ))

        # Consume resources only for approved projects
        if outcome == "Approved":
            resources, budget_pool = consume_resources(proj, resources, budget_pool)

    summary = summarise_results(records)
    return records, summary


def print_scenario(scenario_name: str, records: list, summary: dict):
    """Print a formatted decision table and summary to console."""
    print("\n" + "=" * 90)
    print(f"  {scenario_name}")
    print("=" * 90)

    df = pd.DataFrame(records)[[
        "project_name", "phase1_score", "phase1_outcome",
        "final_decision", "reason"
    ]]
    df.columns = ["Project", "P1 Score", "P1 Result", "Decision", "Reason"]
    print(df.to_string(index=False))

    print("\n── Summary ────────────────────────────────────────────")
    for k, v in summary.items():
        print(f"  {k:<35} {v}")


def main():
    all_records = []

    for scenario in SCENARIOS:
        records, summary = run_scenario(scenario, PROJECTS)
        print_scenario(scenario["name"], records, summary)

        # Tag each record with its scenario name for export
        for r in records:
            r["scenario"] = scenario["name"]
        all_records.extend(records)

    # Export full results to CSV
    df_all = pd.DataFrame(all_records)
    df_all.to_csv("ppms_results.csv", index=False)
    print("\n\n✓ Results exported to ppms_results.csv")

    # Cross-scenario summary table
    print("\n" + "=" * 90)
    print("  CROSS-SCENARIO COMPARISON SUMMARY")
    print("=" * 90)
    comparison_rows = []
    for scenario in SCENARIOS:
        records, summary = run_scenario(scenario, PROJECTS)
        comparison_rows.append({
            "Scenario":              scenario["name"].split("—")[0].strip(),
            "Total":                 summary["total_projects"],
            "P1 Pass":               summary["phase1_passed"],
            "P1 Reject":             summary["phase1_rejected"],
            "Approved":              summary["approved"],
            "Deferred":              summary["deferred"],
            "Feasibility Defer %":   str(summary["feasibility_defer_rate_%"]) + "%",
            "Overall Approval %":    str(summary["approval_rate_%"]) + "%",
        })
    df_comp = pd.DataFrame(comparison_rows)
    print(df_comp.to_string(index=False))


if __name__ == "__main__":
    main()
