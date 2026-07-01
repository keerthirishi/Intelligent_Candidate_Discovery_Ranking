import os
import pandas as pd


class SubmissionExporter:

    def export(self, ranked_candidates, output_file):

        rows = []

        for rank, item in enumerate(ranked_candidates, start=1):

            rows.append({

                "rank": rank,

                "candidate_id": item["candidate_id"],

                "score": round(item["score"], 2),

                "reasoning": item["reasoning"]

            })

        os.makedirs(
            os.path.dirname(output_file),
            exist_ok=True
        )

        df = pd.DataFrame(rows)

        df.to_csv(
            output_file,
            index=False
        )

        print("\nSubmission generated successfully.")
        print(output_file)