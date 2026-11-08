from mistralai.client import Mistral
# from mistralai.models.chat_completion import ChatMessage
import os
from dotenv import load_dotenv
import faiss
import numpy as np

# Initialisation du client avec votre clé API
load_dotenv()  # Charge le fichier .env
api_key = os.getenv("MISTRAL_API_KEY")
client = Mistral(api_key=api_key)

def embed_text(text):
    # Appel de l'API d'embedding
    embeddings_batch = client.embeddings.create(
    model="mistral-embed",
    inputs=text)
    return embeddings_batch.data[0].embedding

# documents est une liste de textes
documents = [
    "La mairie est ouverte du lundi au vendredi de 9h à 17h.",
    "Le règlement municipal interdit les stationnements devant les écoles.",
    "Les horaires des déchetteries varient selon les saisons.",
    "Les demandes de passeport se font uniquement sur rendez-vous.",
    "Les aides sociales sont disponibles sous conditions de revenus.",
    "Le projet de rénovation de la mairie avance.",
    "Une nouvelle école sera inaugurée le mois prochain.",
    "Les travaux de la route principale sont terminés.",
    "La bibliothèque municipale organise une exposition.",
    "Un plan de développement durable a été adopté.",
    "Texte du document 1",
    "Texte du document 2",
    "Texte du document 6",
]

# Génération des embeddings pour chaque document
embeddings = np.array([embed_text([doc]) for doc in documents])
print(f'Shape of embeddings: {embeddings.shape}')

# Initialisation de l'index Faiss
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

# Ajout des embeddings à l'index
index.add(embeddings)

# Sauvegarde de l'index sur le disque
faiss.write_index(index, "faiss_index.idx")

# Requête utilisateur
query_1 = "Informations sur les horaires d'ouverture de la mairie"
query_2 = "Informations sur les horaires d'ouverture de la mairie du 6ème arrondissement"


# Génération de l'embedding de la requête
query_embedding_1 = embed_text([query_1])
query_embedding_2 = embed_text([query_2])

# Recherche des k documents les plus similaires
print(f"Résultats pour la requête '{query_1}':")
k = 3
distances, indices = index.search(np.array([query_embedding_1]), k)

# Affichage des résultats
for idx in indices[0]:
    print(f"Document {idx}: {documents[idx]}")

print(f"Résultats pour la requête '{query_2}':")
distances, indices = index.search(np.array([query_embedding_2]), k)

# Affichage des résultats
for idx in indices[0]:
    print(f"Document {idx}: {documents[idx]}")