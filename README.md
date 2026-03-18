# API de Usuários

API REST simples para gerenciamento de usuários, desenvolvida com FastAPI e SQLite.

## Tecnologias

- Python 3.10+
- FastAPI
- SQLite

## Como rodar

**1. Clone o repositório**
```bash
git clone https://github.com/NicolasDEVoB/PythonAPIrest.git
cd seu-repositorio
```

**2. Instale as dependências com uv**
```bash
uv init
uv add fastapi uvicorn
```

**3. Rode o servidor**
```bash
uv run uvicorn main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`.

A documentação interativa estará disponível em `http://127.0.0.1:8000/docs`.

## Endpoints

| Método | Rota | Descrição |
|---|---|---|
| GET | `/` | Lista todos os usuários |
| POST | `/` | Cria um novo usuário |
| GET | `/{user_id}` | Busca um usuário pelo ID |
| PUT | `/{user_id}` | Atualiza um usuário pelo ID |
| DELETE | `/{user_id}` | Deleta um usuário pelo ID |

## Exemplo de uso

**Criar um usuário**
```json
POST /
{
  "name": "Jefferson",
  "email": "jefferson@gmail.com"
}
```

**Atualizar um usuário**
```json
PUT /1
{
  "name": "Jefferson Novo",
  "email": "novo@gmail.com"
}
```

## Estrutura do projeto

```
projeto/
├── main.py        # Rotas da API
├── database.py    # Conexão e queries SQL
├── models.py      # Modelos Pydantic
└── banco.db       # Banco de dados (gerado automaticamente)
```