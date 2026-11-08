from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from pathlib import Path

# 1. Lire le fichier Markdown sous forme de texte brut
municipal_bylaws_filepath = "inputs_markdown/intances/"
municipal_bylaws_filename = "RÈGLEMENT MUNICIPAL.md"
municipal_bylaws_path = Path (municipal_bylaws_filepath + municipal_bylaws_filename)
municipal_bylaws_md = municipal_bylaws_path.read_text(encoding="utf-8")
print(f"Type de municipal_bylaws_md : {type(municipal_bylaws_md)}")
print(f"Longueur de municipal_bylaws_md : {len(municipal_bylaws_md)} caractères")

# 2. Configuration du MarkdownHeaderTextSplitter
# On définit quels titres (Headers) déclenchent une découpe et le nom de la clé en métadonnée
headers_to_split_on = [
    ("#", "Header_1"),
    ("##", "Header_2"),
    ("###", "Header_3"),
    ]

markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on, strip_headers=False)

sections = markdown_splitter.split_text(municipal_bylaws_md )

for section in sections:
    section.metadata["source"] = str(municipal_bylaws_filename)

# 3. Configuration du RecursiveCharacterTextSplitter
# On définit le nombre de caractères max et l'overlap

size_splitter = RecursiveCharacterTextSplitter(
    chunk_size=2000, # Caractères, ici
    chunk_overlap=100,
)

chunks = size_splitter.split_documents(sections)

# 4. Découpage du texte en chunks
print(f"Longueur de chunks : {len(chunks)}")
for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:\n{chunk}\n")