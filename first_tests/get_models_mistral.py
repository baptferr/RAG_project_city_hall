import os
from mistralai.client import Mistral

# Initialisation du client
client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

# Récupération de la liste complète des modèles
models_list = client.models.list()

# Affichage des identifiants des modèles disponibles
for model in models_list.data:
    print(model.id)