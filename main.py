from config import (
    CANDIDATES_FILE,
    OUTPUT_CSV,
    TOP_K
)

from src.parser import load_candidates
from src.ranker import CandidateRanker
from src.reasoning import ReasoningGenerator
from src.exporter import SubmissionExporter


def main():

    print("Loading candidates...")

    candidates = load_candidates(
        CANDIDATES_FILE
    )

    ranker = CandidateRanker()

    top_candidates = ranker.get_top_candidates(
        candidates,
        TOP_K
    )

    reasoning = ReasoningGenerator()

    for item in top_candidates:

        item["reasoning"] = reasoning.generate(
            item["candidate"],
            item["feature"],
            item["score"]
        )

    exporter = SubmissionExporter()

    exporter.export(
        top_candidates,
        OUTPUT_CSV
    )

    print("\nTop 10 Candidates\n")

    for index, candidate in enumerate(top_candidates[:10], start=1):

        print(
            f"{index}. {candidate['candidate_id']}  Score: {candidate['score']}"
        )


if __name__ == "__main__":
    main()