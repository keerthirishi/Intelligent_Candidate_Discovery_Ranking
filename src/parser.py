import json
from tqdm import tqdm
class CandidateParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_candidates(self):
        candidates = []

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:

                for line in tqdm(file, desc="Loading Candidates"):

                    line = line.strip()

                    if not line:
                        continue

                    try:
                        candidate = json.loads(line)
                        candidates.append(candidate)

                    except json.JSONDecodeError:
                        continue

            print(f"\nLoaded {len(candidates)} candidates successfully.")

            return candidates

        except FileNotFoundError:
            print(" Candidate file not found.")
            return []

        except Exception as e:
            print(f" Error: {e}")
            return []


def load_candidates(file_path):
    """
    Shortcut function

    Example:
        candidates = load_candidates("data/candidates.jsonl")
    """

    parser = CandidateParser(file_path)

    return parser.load_candidates()