from config import WEIGHTS


class CandidateScorer:

    def __init__(self):
        self.weights = WEIGHTS

    def calculate_score(self, feature):

        score = 0

        exp = feature["experience"]

        if 5 <= exp <= 9:
            score += 15
        elif exp > 9:
            score += 12
        elif exp >= 3:
            score += 8
        else:
            score += 2

        score += min(feature["required_skill_count"] * 3, 20)

        score += min(feature["bonus_skill_count"], 5)

        score += min(feature["skill_proficiency"] * 0.5, 8)

        score += min(feature["skill_duration"] / 24, 5)

        score += min(feature["endorsements"] / 20, 5)

        score += min(feature["assessment"] / 10, 5)

        if "engineer" in feature["title"]:
            score += 4

        if "ai" in feature["title"]:
            score += 3

        if "ml" in feature["title"]:
            score += 3

        if "data" in feature["title"]:
            score += 2

        score += min(feature["career_product_company"] * 2, 10)

        score += min(feature["profile_completion"] / 20, 5)

        score += feature["response_rate"] * 5

        score += feature["interview_rate"] * 5

        score += min(feature["saved"], 5)

        if feature["open_to_work"]:
            score += 3

        if feature["relocate"]:
            score += 2

        notice = feature["notice"]

        if notice <= 30:
            score += 5
        elif notice <= 60:
            score += 3
        elif notice <= 90:
            score += 1

        github = feature["github"]

        if github > 0:
            score += min(github / 20, 5)

        if feature["verified_email"]:
            score += 1

        if feature["verified_phone"]:
            score += 1

        if feature["linkedin"]:
            score += 1

        score += min(feature["connections"] / 100, 3)

        score += min(feature["search_appearance"] / 50, 3)

        if "recommendation" in feature["summary"]:
            score += 2

        if "retrieval" in feature["summary"]:
            score += 2

        if "ranking" in feature["summary"]:
            score += 2

        if "embedding" in feature["summary"]:
            score += 2

        if "llm" in feature["summary"]:
            score += 2

        return round(score, 2)