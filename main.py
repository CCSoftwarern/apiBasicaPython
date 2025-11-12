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


# rota get com 2 parametros
@app.get("/calcular/{vr1}/{vr2}")
def calcular(vr1: int, vr2:int):
    total = vr1 * vr2
    return {"mensagem": "Calculo", "resultado": total}