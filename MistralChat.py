# app.py
import streamlit as st
from mistralai.client import Mistral
import logging
import datetime
from streamlit_feedback import streamlit_feedback # Importez le composant

# Importer nos modules locaux
from utils.config import APP_TITLE, COMMUNE_NAME, MISTRAL_API_KEY
from utils.vector_store import VectorStoreManager
from utils.database import log_interaction, update_feedback # Importez update_feedback
from utils.query_classifier import QueryClassifier

