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

@app.get("/{user_id}")
def buscar(user_id: int):
    usuario = db.read(user_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

@app.put("/{user_id}")
def atualizar(user_id: int, user: Usuario):
    usuario = db.read(user_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    db.update(user_id, user.name, user.email)
    return {"message": "Usuário atualizado com sucesso!"}


@app.delete("/{user_id}")
def deletar(user_id: int):
    usuario = db.read(user_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    db.delete(user_id)
    return {"message": "Usuário deletado com sucesso!"}