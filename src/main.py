from fastapi.testclient import TestClient
from unittest.mock import patch
from src.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API rodando."}


def test_helloworld():
    response = client.get("/helloworld")
    assert response.status_code == 200
    assert response.json() == {"message": "hello, world! :)"}


def test_funcaoteste():
    with patch("src.main.random.randint", return_value=12345):
        response = client.get("/funcaoteste")
    assert response.status_code == 200
    assert response.json() == {"teste": True, "num_aleatorio": 12345}


def test_create_estudante():
    payload = {
        "name": "Fulano",
        "curso": "Curso XPTO",
        "ativo": False
    }
    response = client.post("/estudantes/cadastro", json=payload)
    assert response.status_code == 200
    assert response.json() == payload 


def test_update_estudante():
    response = client.put("/estudantes/update/10")
    assert response.status_code == 200
    assert response.json() == {"id_estudante": 10, "status": "atualizado"}


def test_delete_estudante():
    response = client.delete("/estudantes/delete/10") 
    assert response.status_code == 200
    assert response.json() == {"deleted": True}