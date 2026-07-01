from config import REQUIRED_SKILLS, BONUS_SKILLS


class FeatureEngineer:

    def __init__(self):

        self.required_skills = [s.lower() for s in REQUIRED_SKILLS]
        self.bonus_skills = [s.lower() for s in BONUS_SKILLS]

        self.product_companies = [
            "google","microsoft","amazon","flipkart",
            "swiggy","zomato","uber","ola","razorpay",
            "cred","atlassian","adobe","salesforce",
            "redrob","freshworks","browserstack"
        ]

    def extract_features(self, candidate):

        profile = candidate.get("profile", {})
        signals = candidate.get("redrob_signals", {})

        career = candidate.get("career_history", [])
        skills = candidate.get("skills", [])
        education = candidate.get("education", [])

        feature = {}

        feature["candidate_id"] = candidate.get("candidate_id")

        feature["experience"] = profile.get(
            "years_of_experience", 0
        )

        feature["headline"] = profile.get(
            "headline", ""
        ).lower()

        feature["summary"] = profile.get(
            "summary", ""
        ).lower()

        feature["title"] = profile.get(
            "current_title", ""
        ).lower()

        feature["industry"] = profile.get(
            "current_industry", ""
        ).lower()

        feature["company"] = profile.get(
            "current_company", ""
        ).lower()

        feature["location"] = profile.get(
            "location", ""
        ).lower()

        feature["skill_names"] = []

        feature["skill_proficiency"] = 0

        feature["skill_duration"] = 0

        feature["endorsements"] = 0

        proficiency = {
            "beginner":1,
            "intermediate":2,
            "advanced":3,
            "expert":4
        }

        required_count = 0
        bonus_count = 0

        for skill in skills:

            name = skill.get(
                "name",""
            ).lower()

            feature["skill_names"].append(name)

            if name in self.required_skills:
                required_count += 1

            if name in self.bonus_skills:
                bonus_count += 1

            feature["skill_proficiency"] += proficiency.get(
                skill.get(
                    "proficiency",
                    "beginner"
                ).lower(),
                1
            )

            feature["skill_duration"] += skill.get(
                "duration_months",
                0
            )

            feature["endorsements"] += skill.get(
                "endorsements",
                0
            )

        feature["required_skill_count"] = required_count

        feature["bonus_skill_count"] = bonus_count

        feature["career_titles"] = []

        feature["career_product_company"] = 0

        feature["career_duration"] = 0

        for job in career:

            title = job.get(
                "title",""
            ).lower()

            company = job.get(
                "company",""
            ).lower()

            feature["career_titles"].append(title)

            feature["career_duration"] += job.get(
                "duration_months",
                0
            )

            if company in self.product_companies:
                feature["career_product_company"] += 1

        feature["education_count"] = len(
            education
        )

        tiers = []

        for edu in education:

            tiers.append(
                edu.get(
                    "tier",
                    "tier_3"
                )
            )

        feature["education_tiers"] = tiers

        feature["profile_completion"] = signals.get(
            "profile_completeness_score",
            0
        )

        feature["response_rate"] = signals.get(
            "recruiter_response_rate",
            0
        )

        feature["interview_rate"] = signals.get(
            "interview_completion_rate",
            0
        )

        feature["github"] = signals.get(
            "github_activity_score",
            -1
        )

        feature["search_appearance"] = signals.get(
            "search_appearance_30d",
            0
        )

        feature["saved"] = signals.get(
            "saved_by_recruiters_30d",
            0
        )

        feature["notice"] = signals.get(
            "notice_period_days",
            180
        )

        feature["connections"] = signals.get(
            "connection_count",
            0
        )

        feature["verified_email"] = signals.get(
            "verified_email",
            False
        )

        feature["verified_phone"] = signals.get(
            "verified_phone",
            False
        )

        feature["linkedin"] = signals.get(
            "linkedin_connected",
            False
        )

        feature["open_to_work"] = signals.get(
            "open_to_work_flag",
            False
        )

        feature["relocate"] = signals.get(
            "willing_to_relocate",
            False
        )

        assessments = signals.get(
            "skill_assessment_scores",
            {}
        )

        if assessments:

            feature["assessment"] = sum(
                assessments.values()
            ) / len(assessments)

        else:

            feature["assessment"] = 0

        return feature