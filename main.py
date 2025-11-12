from fastapi import FastAPI

# cria a aplicação
app = FastAPI()

# rota raiz
@app.get("/")

def read_root():
    return {"mensagem": "Olá, mundo! 🚀"}

# rota com parâmetro
@app.get("/usuarios/{usuario_id}")
def read_usuario(usuario_id: int):
    return {"usuario_id": usuario_id, "nome": f"Usuário {usuario_id}"}

# rota POST
@app.post("/usuarios/")
def criar_usuario(usuario: dict):
    return {"mensagem": "Usuário criado com sucesso!", "dados": usuario}
