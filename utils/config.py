from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
if not MISTRAL_API_KEY:
    print("⚠️ Attention: La clé API Mistral (MISTRAL_API_KEY) n'est pas définie dans le fichier .env")
    raise ValueError("Clé API Mistral manquante. Veuillez la définir dans le fichier .env")

# Mistral models
EMBEDDING_MODEL = "mistral-embed"
CHAT_MODEL = "mistral-small-latest"

# Configuration de l'Indexation
PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUTS_ORIGINAL_DIR = PROJECT_ROOT / "inputs_original"
INPUTS_MARKDOWN_DIR = PROJECT_ROOT / "inputs_markdown"
# INPUT_DIR = "inputs"                # Dossier pour les données sources après extraction
VECTOR_DB_DIR = PROJECT_ROOT / "vector_db"         # Dossier pour stocker l'index Faiss et les chunks
FAISS_INDEX_FILE = os.path.join(VECTOR_DB_DIR, "faiss_index.idx")
DOCUMENT_CHUNKS_FILE = os.path.join(VECTOR_DB_DIR, "document_chunks.pkl")

CHUNK_SIZE = 1500
CHUNK_OVERLAP = 150
EMBEDDING_BATCH_SIZE = 32

# Search configuration
SEARCH_K = 5

# Database configuration
DATABASE_DIR = PROJECT_ROOT / "database"
DATABASE_FILE = os.path.join(DATABASE_DIR, "interactions.db")
DATABASE_URL = f"sqlite:///{DATABASE_FILE}" # URL pour SQLAlchemy

# Configuration de l'Application
APP_TITLE = "Assistant RAG"
COMMUNE_NAME = "Triffouillis-sur-Loire"