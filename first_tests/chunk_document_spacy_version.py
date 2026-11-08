import spacy;

municipal_bylaws_path = "inputs_markdown/intances/RÈGLEMENT MUNICIPAL.md"

# 1. Lire le fichier Markdown sous forme de texte brut
with open(municipal_bylaws_path, "r", encoding="utf-8") as f:
    municipal_bylaws_md = f.read()
print(f"Type de municipal_bylaws_md : {type(municipal_bylaws_md)}")
print(f"Longueur de municipal_bylaws_md : {len(municipal_bylaws_md)} caractères")

# Charger le modèle français de spaCy
nlp = spacy.load("fr_core_news_sm")

def semantic_chunking(text, max_chunk_size=2000):
    doc = nlp(text)
    chunks = []
    current_chunk = []
    
    for sent in doc.sents:
        if len(" ".join(current_chunk)) + len(sent.text) <= max_chunk_size:
            current_chunk.append(sent.text)
        else:
            chunks.append(" ".join(current_chunk))
            current_chunk = [sent.text]
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks

chunks = semantic_chunking(municipal_bylaws_md)

print(f"Longueur de chunks : {len(chunks)}")
    
# Affichage des chunks
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:\n{chunk}\n")