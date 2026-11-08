from sentence_transformers import SentenceTransformer;
import numpy as np;

# Chargement du modèle SBERT
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Textes à vectoriser
textes1 = ["Le chat dort sur le tapis.", "Le chien joue dans le jardin."]
textes2 = ["Le chat orange dort sur le tapis.", "Le chat gris dort sur le tapis."]
textes3 = ["Le chat orange dort sur le tapis.", "Le chat gris dort sur le tapis."]

textes = [textes1, textes2, textes3]
for texte in textes:
    print(f"Textes : {texte}")
    # Obtention des embeddings
    embeddings = model.encode(textes)

    # print(embeddings)

    vec1 = embeddings[0]
    vec2 = embeddings[1]
    similarity = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

    print(f"Similarité : {similarity}")