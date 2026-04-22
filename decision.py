# decision.py
# Builds a structured DecisionRecord for every project
# Records phase reached, score, outcome, reason, and timestamp
# This is the audit trail that supports decision traceability

from datetime import datetime


def record_decision(project: dict,
                    phase1_score: float,
                    phase1_outcome: str,
                    final_decision: str,
                    reason: str = None) -> dict:
    """
    Build a complete decision record for a project.

    Args:
        project:         project dict (id, name)
        phase1_score:    float score from Phase 1
        phase1_outcome:  'Pass' or 'Fail'
        final_decision:  'Approved', 'Deferred', or 'Rejected'
        reason:          explanation string if not Approved

    Returns:
        dict: complete decision record
    """
    phase_reached = "Phase 1" if final_decision == "Rejected" else "Phase 2"

    return {
        "project_id":      project["id"],
        "project_name":    project["name"],
        "phase1_score":    phase1_score,
        "phase1_outcome":  phase1_outcome,
        "phase_reached":   phase_reached,
        "final_decision":  final_decision,
        "reason":          reason if reason else "—",
        "timestamp":       datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }


def summarise_results(records: list) -> dict:
    """
    Produce summary statistics from a list of decision records.

    Returns:
        dict with counts and rates for reporting
    """
    total       = len(records)
    approved    = sum(1 for r in records if r["final_decision"] == "Approved")
    deferred    = sum(1 for r in records if r["final_decision"] == "Deferred")
    rejected    = sum(1 for r in records if r["final_decision"] == "Rejected")
    p1_passed   = sum(1 for r in records if r["phase1_outcome"] == "Pass")

    return {
        "total_projects":          total,
        "phase1_passed":           p1_passed,
        "phase1_rejected":         total - p1_passed,
        "phase1_pass_rate_%":      round(p1_passed / total * 100, 1),
        "approved":                approved,
        "deferred":                deferred,
        "rejected":                rejected,
        "feasibility_defer_rate_%":
            round(deferred / p1_passed * 100, 1) if p1_passed > 0 else 0,
        "approval_rate_%":
            round(approved / total * 100, 1),
    }
