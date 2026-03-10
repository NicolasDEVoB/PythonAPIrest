from fastapi import FastAPI, HTTPException
import database as db
from models import Usuario


app = FastAPI()

@app.get("/")
def ler_tudo():
    return db.read_all()

@app.post("/")
def inserir(user: Usuario):
    db.insert(user.name, user.email)
    return {"message": "Usuário criado com sucesso!"}

@app.get("/{id}")
def buscar(id: int):
    usuario = db.read(id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

@app.delete("/{id}")
def deletar(id: int):
    if id is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    deletar(id)
    return {"message": "Usuário deletado com sucesso!"}