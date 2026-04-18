from fastapi import FastAPI
import random
from pydantic import BaseModel

app = FastAPI()


# rota básica
@app.get("/")
def home():
    return {"message": "API rodando."}


# modelo
class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool


# endpoint com random correto
@app.get("/funcaoteste")
async def funcaoteste():
    return {
        "teste": True,
        "num_aleatorio": random.randint(0, 10000)
    }


# hello world
@app.get("/helloworld")
async def helloworld():
    return {"message": "hello, world! :)"}


# create estudante
@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante


# update estudante
@app.put("/estudantes/update/{id_estudante}")
async def update_estudante(id_estudante: int):
    return {"id_estudante": id_estudante, "status": "atualizado"}


# delete estudante (rota corrigida!)
@app.delete("/estudantes/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
    return {"deleted": id_estudante > 0}