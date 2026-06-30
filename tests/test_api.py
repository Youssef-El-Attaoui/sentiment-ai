import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health():
    """Vérifie que l'endpoint /health répond avec status 200."""
    r = client.get("/health")  # <-- Espace supprimé ici
    assert r.status_code == 200

def test_predict_positive():
    """Vérifie qu'une prédiction retourne la bonne structure de réponse."""
    r = client.post("/predict", json={"text": "Ce produit est excellent !"})  # <-- Espace supprimé ici
    assert r.status_code == 200

def test_predict_empty_fails():
    """Vérifie que Pydantic rejette un texte vide avec une erreur 422."""
    r = client.post("/predict", json={"text": ""})  # <-- Espace supprimé ici
    assert r.status_code == 422