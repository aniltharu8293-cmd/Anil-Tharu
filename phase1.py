# phase1.py
# Phase 1: Strategic Screening
# Evaluates each project against weighted strategic criteria
# Returns a score out of 100 and a pass/fail decision

WEIGHTS = {
    "alignment": 0.40,   # Strategic alignment to organisational objectives
    "financial": 0.35,   # Expected financial value / ROI
    "risk":      0.25,   # Risk profile (higher = lower risk = better)
}

PHASE1_THRESHOLD = 60  # Minimum score to pass Phase 1


def phase1_score(project: dict, weights: dict = WEIGHTS) -> float:
    """
    Calculate weighted Phase 1 strategic score for a project.

    Args:
        project: dict with keys strategic_alignment, financial_value, risk_score
        weights: dict with keys alignment, financial, risk (must sum to 1.0)

    Returns:
        float: score between 0 and 100
    """
    score = (
        project["strategic_alignment"] * weights["alignment"] +
        project["financial_value"]     * weights["financial"] +
        project["risk_score"]          * weights["risk"]
    )
    return round(score, 2)


def phase1_evaluate(project: dict, weights: dict = WEIGHTS,
                    threshold: float = PHASE1_THRESHOLD) -> dict:
    """
    Full Phase 1 evaluation: score + pass/fail decision.

    Returns:
        dict with score, passed (bool), outcome label
    """
    score = phase1_score(project, weights)
    passed = score >= threshold
    return {
        "phase1_score": score,
        "phase1_passed": passed,
        "phase1_outcome": "Pass" if passed else "Fail",
        "phase1_reason": None if passed else "Below strategic threshold (score < 60)"
    }
