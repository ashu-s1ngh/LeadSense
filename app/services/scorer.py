class ProgressionEngine:
    def __init__(self):
        self.my_skills = {
            "python": 5,
            "fastapi": 4,
            "sqlalchemy": 4,
            "pydantic": 4,
            "sqlite": 4,
            "docker": 1,
            "aws lambda": 0,
            "selenium": 2,
            "django": 3,
            "flask": 3,
            "jwt": 3,
        }

    def calculate_score(self, lead_tech_stack: list[str]) -> int:
        score = 0
        for tech in lead_tech_stack:
            tech_lower = tech.lower()
            if tech_lower in self.my_skills:
                score += self.my_skills[tech_lower]
        return score