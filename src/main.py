from fastapi import FastAPI
import random
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API rodando."}

class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool

@app.get("/funcaoteste")
async def funcaoteste():
    return {
        "teste": True,
        "num_aleatorio": random.randint(0, 10000)
    }

@app.get("/helloworld")
async def helloworld():
    return {"message": "hello, world! :)"}

@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante

@app.put("/estudantes/update/{id_estudante}")
async def update_estudante(id_estudante: int):
    return {"id_estudante": id_estudante, "status": "atualizado"}

@app.delete("/estudantes/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
    return {"deleted": id_estudante > 0}