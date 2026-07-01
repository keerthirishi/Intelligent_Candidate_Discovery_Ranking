import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

CANDIDATES_FILE = os.path.join(DATA_DIR, "candidates.jsonl")

OUTPUT_DIR = os.path.join(BASE_DIR, "output")

OUTPUT_CSV = os.path.join(OUTPUT_DIR, "submission.csv")
WEIGHTS = {

    "skill_match": 30,

    "experience": 20,

    "behavior": 15,

    "career": 10,

    "python": 5,

    "retrieval": 10,

    "github": 5,

    "location": 5

}
MIN_EXP = 5

MAX_EXP = 9
REQUIRED_SKILLS = [

    "python",

    "machine learning",

    "deep learning",

    "nlp",

    "llm",

    "rag",

    "retrieval",

    "embeddings",

    "vector database",

    "pinecone",

    "milvus",

    "faiss",

    "weaviate",

    "qdrant",

    "elasticsearch",

    "opensearch",

    "ranking",

    "ndcg",

    "map",

    "mrr",

    "evaluation",

    "fine tuning",

    "lora",

    "qlora",

    "peft"

]
BONUS_SKILLS = [

    "docker",

    "kubernetes",

    "aws",

    "azure",

    "gcp",

    "huggingface",

    "langchain",

    "transformers",

    "airflow",

    "spark",

    "tensorflow",

    "pytorch"

]
GOOD_TITLES = [

    "ai engineer",

    "ml engineer",

    "machine learning engineer",

    "research engineer",

    "data scientist",

    "senior ai engineer",

    "applied scientist",

    "nlp engineer",

    "computer vision engineer"

]
VECTOR_DATABASES = [

    "pinecone",

    "faiss",

    "milvus",

    "weaviate",

    "qdrant",

    "chroma",

    "elasticsearch",

    "opensearch"

]
EMBEDDING_KEYWORDS = [

    "embedding",

    "sentence transformer",

    "bge",

    "e5",

    "semantic search",

    "retrieval",

    "vector search"

]
LLM_KEYWORDS = [

    "llm",

    "gpt",

    "bert",

    "transformer",

    "rag",

    "fine tuning",

    "lora",

    "qlora",

    "peft"

]

MIN_GITHUB = 0

GOOD_GITHUB = 50
MAX_NOTICE_PERIOD = 90
TOP_K = 100
RANDOM_STATE = 42