from tqdm import tqdm

from src.feature_engineering import FeatureEngineer
from src.scoring import CandidateScorer


class CandidateRanker:

    def __init__(self):

        self.engineer = FeatureEngineer()
        self.scorer = CandidateScorer()

    def rank_candidates(self, candidates):

        ranked = []

        for candidate in tqdm(
            candidates,
            desc="Ranking Candidates"
        ):

            try:

                feature = self.engineer.extract_features(
                    candidate
                )

                score = self.scorer.calculate_score(
                    feature
                )

                ranked.append({

                    "candidate_id": candidate.get(
                        "candidate_id"
                    ),

                    "score": score,

                    "feature": feature,

                    "candidate": candidate

                })

            except Exception:

                continue

        ranked.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return ranked

    def get_top_candidates(
        self,
        candidates,
        top_k=100
    ):

        ranked = self.rank_candidates(
            candidates
        )

        return ranked[:top_k]