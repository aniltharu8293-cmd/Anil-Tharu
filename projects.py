# projects.py
# Sample project proposals for PPMS prototype evaluation
# Three scenarios: A (Balanced), B (Skill Scarcity), C (Competing Priorities)

PROJECTS = [
    {
        "id": "P001",
        "name": "CRM Platform Upgrade",
        "strategic_alignment": 88,
        "financial_value": 80,
        "risk_score": 75,
        "required_skills": {"Java": 3, "DevOps": 1, "BA": 1},
        "budget": 45000,
        "duration_weeks": 12,
        "dependencies": []
    },
    {
        "id": "P002",
        "name": "Cloud Migration Initiative",
        "strategic_alignment": 82,
        "financial_value": 78,
        "risk_score": 70,
        "required_skills": {"DevOps": 3, "CloudArch": 2},
        "budget": 70000,
        "duration_weeks": 16,
        "dependencies": ["P001"]
    },
    {
        "id": "P003",
        "name": "Legacy Reporting Tool",
        "strategic_alignment": 38,
        "financial_value": 45,
        "risk_score": 50,
        "required_skills": {"Python": 1, "BA": 1},
        "budget": 15000,
        "duration_weeks": 8,
        "dependencies": []
    },
    {
        "id": "P004",
        "name": "Cybersecurity Audit System",
        "strategic_alignment": 95,
        "financial_value": 88,
        "risk_score": 92,
        "required_skills": {"Security": 2, "Python": 1},
        "budget": 40000,
        "duration_weeks": 10,
        "dependencies": []
    },
    {
        "id": "P005",
        "name": "Data Warehouse Modernisation",
        "strategic_alignment": 78,
        "financial_value": 72,
        "risk_score": 65,
        "required_skills": {"DataEng": 3, "CloudArch": 1},
        "budget": 85000,
        "duration_weeks": 20,
        "dependencies": []
    },
    {
        "id": "P006",
        "name": "HR Self-Service Portal",
        "strategic_alignment": 65,
        "financial_value": 60,
        "risk_score": 70,
        "required_skills": {"Java": 2, "BA": 2},
        "budget": 30000,
        "duration_weeks": 10,
        "dependencies": []
    },
    {
        "id": "P007",
        "name": "API Integration Framework",
        "strategic_alignment": 80,
        "financial_value": 85,
        "risk_score": 72,
        "required_skills": {"Java": 2, "DevOps": 2, "Python": 1},
        "budget": 55000,
        "duration_weeks": 14,
        "dependencies": []
    },
    {
        "id": "P008",
        "name": "Business Intelligence Dashboard",
        "strategic_alignment": 74,
        "financial_value": 70,
        "risk_score": 68,
        "required_skills": {"DataEng": 2, "BA": 1},
        "budget": 35000,
        "duration_weeks": 12,
        "dependencies": ["P005"]
    },
    {
        "id": "P009",
        "name": "Mobile Customer App",
        "strategic_alignment": 42,
        "financial_value": 55,
        "risk_score": 48,
        "required_skills": {"Mobile": 2, "BA": 1},
        "budget": 60000,
        "duration_weeks": 18,
        "dependencies": []
    },
    {
        "id": "P010",
        "name": "Compliance Tracking Module",
        "strategic_alignment": 90,
        "financial_value": 75,
        "risk_score": 88,
        "required_skills": {"Java": 1, "Security": 1, "BA": 1},
        "budget": 28000,
        "duration_weeks": 8,
        "dependencies": []
    },
]
