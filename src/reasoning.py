class ReasoningGenerator:

    def generate(self, candidate, feature, score):

        reasons = []

        if feature["experience"] >= 5:
            reasons.append(
                f"{feature['experience']} years of experience"
            )

        if feature["required_skill_count"] > 0:
            reasons.append(
                f"{feature['required_skill_count']} required skills matched"
            )

        if feature["career_product_company"] > 0:
            reasons.append(
                "Product company experience"
            )

        if feature["assessment"] >= 70:
            reasons.append(
                "Strong assessment performance"
            )

        if feature["profile_completion"] >= 80:
            reasons.append(
                "Highly complete profile"
            )

        if feature["response_rate"] >= 0.50:
            reasons.append(
                "Good recruiter response rate"
            )

        if feature["interview_rate"] >= 0.50:
            reasons.append(
                "Strong interview completion"
            )

        if feature["open_to_work"]:
            reasons.append(
                "Open to work"
            )

        if feature["relocate"]:
            reasons.append(
                "Willing to relocate"
            )

        if feature["github"] > 50:
            reasons.append(
                "Active GitHub profile"
            )

        if feature["notice"] <= 30:
            reasons.append(
                "Short notice period"
            )

        if len(reasons) == 0:
            reasons.append(
                "Relevant profile"
            )

        return "; ".join(reasons)