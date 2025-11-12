# apiBasicaPython
## Criar Venv:
python -m venv venv

## Ativar Venv Windows:
venv\Scripts\activate

## Mac / Linux:
source venv/bin/activate

## Salvar as dependências no requirements.txt
pip freeze > requirements.txt

Assim, outras pessoas (ou você em outro computador) podem recriar o ambiente com:

pip install -r requirements.txt

GET / → retorna “Olá, mundo!”

GET /usuarios/{id} → retorna dados simulados de um usuário

POST /usuarios/ → recebe dados JSON e retorna uma resposta

## Pra rodar
uvicorn main:app --reload
Use:

🧱 1. Rodar o servidor ouvindo em todas as interfaces
uvicorn main:app --host 0.0.0.0 --port 8000 --reload


🔹 --host 0.0.0.0 faz o servidor aceitar conexões de qualquer IP.
🔹 --port 8000 define a porta (pode mudar se quiser).
