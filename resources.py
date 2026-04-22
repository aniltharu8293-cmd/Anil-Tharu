# resources.py
# Resource availability and budget pool for each scenario
# Scenario A: Balanced (baseline)
# Scenario B: Skill Scarcity (DevOps and CloudArch bottleneck)
# Scenario C: Competing Priorities (reduced budget, tight security demand)

SCENARIO_A = {
    "name": "Scenario A — Balanced Resources (Baseline)",
    "budget_pool": 300000,
    "skills": {
        "Java": 8,
        "DevOps": 6,
        "Python": 5,
        "CloudArch": 4,
        "DataEng": 5,
        "Security": 4,
        "BA": 6,
        "Mobile": 3,
    }
}

SCENARIO_B = {
    "name": "Scenario B — Skill Scarcity (DevOps & CloudArch Bottleneck)",
    "budget_pool": 300000,
    "skills": {
        "Java": 8,
        "DevOps": 2,       # scarce
        "Python": 5,
        "CloudArch": 1,    # scarce
        "DataEng": 5,
        "Security": 4,
        "BA": 6,
        "Mobile": 3,
    }
}

SCENARIO_C = {
    "name": "Scenario C — Competing Strategic Priorities (Budget Constraint)",
    "budget_pool": 150000,  # reduced budget
    "skills": {
        "Java": 8,
        "DevOps": 6,
        "Python": 5,
        "CloudArch": 4,
        "DataEng": 5,
        "Security": 4,
        "BA": 6,
        "Mobile": 3,
    }
}

SCENARIOS = [SCENARIO_A, SCENARIO_B, SCENARIO_C]
