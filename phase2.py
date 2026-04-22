# phase2.py
# Phase 2: Feasibility Assessment
# Checks resource availability, budget ceiling, and skill constraints
# Only called for projects that passed Phase 1
# Returns Approved or Deferred (NOT Rejected — that is Phase 1's role)

def phase2_check(project: dict, resources: dict, budget_pool: float) -> tuple:
    """
    Check project feasibility against resource and budget constraints.

    Args:
        project:      dict with required_skills (dict) and budget (float)
        resources:    dict mapping skill name to available units
        budget_pool:  float representing remaining available budget

    Returns:
        tuple: (outcome: str, reason: str or None)
               outcome is 'Approved' or 'Deferred'
    """
    # Check each required skill against available capacity
    for skill, units_needed in project["required_skills"].items():
        available = resources.get(skill, 0)
        if available < units_needed:
            return (
                "Deferred",
                f"Insufficient {skill} capacity "
                f"(need {units_needed}, available {available})"
            )

    # Check budget ceiling
    if project["budget"] > budget_pool:
        return (
            "Deferred",
            f"Budget ceiling exceeded "
            f"(requires £{project['budget']:,}, pool has £{budget_pool:,})"
        )

    return ("Approved", None)


def consume_resources(project: dict, resources: dict, budget_pool: float) -> tuple:
    """
    Deduct approved project's resource and budget demand from pool.
    Called only when a project is Approved.

    Returns:
        updated (resources dict, remaining budget_pool float)
    """
    updated_resources = resources.copy()
    for skill, units_needed in project["required_skills"].items():
        updated_resources[skill] = updated_resources.get(skill, 0) - units_needed

    updated_budget = budget_pool - project["budget"]
    return updated_resources, updated_budget
