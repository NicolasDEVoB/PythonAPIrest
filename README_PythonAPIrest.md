# API de Usuários

API REST para gerenciamento de usuários, desenvolvida com **FastAPI** e **SQLite**. Com documentação interativa automática via Swagger.

---

##  Funcionalidades

- Cadastro, listagem, busca, atualização e remoção de usuários (CRUD completo)
- Banco de dados criado automaticamente na primeira execução
- Validação de dados com **Pydantic**
- Documentação interativa automática em `/docs` (Swagger UI)

---

##  Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python 3.13 | Linguagem principal |
| FastAPI | Framework da API REST |
| SQLite | Banco de dados local |
| Pydantic | Validação dos dados |
| uv | Gerenciador de dependências |

---

##  Como rodar o projeto

### Pré-requisitos

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) instalado

### Execução

1. Clone o repositório:
```bash
git clone https://github.com/NicolasDEVoB/PythonAPIrest.git
cd PythonAPIrest
```

2. Instale as dependências:
```bash
uv add fastapi uvicorn
```

3. Rode o servidor:
```bash
uv run uvicorn main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`

 Documentação interativa (Swagger): `http://127.0.0.1:8000/docs`

---

##  Endpoints

| Método | Rota | Descrição |
|---|---|---|
| GET | `/` | Lista todos os usuários |
| POST | `/` | Cria um novo usuário |
| GET | `/{user_id}` | Busca um usuário pelo ID |
| PUT | `/{user_id}` | Atualiza um usuário pelo ID |
| DELETE | `/{user_id}` | Deleta um usuário pelo ID |

---

##  Exemplos de uso

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

---

##  Estrutura do projeto

```
projeto/
├── main.py        # Rotas da API
├── database.py    # Conexão e queries SQL
├── models.py      # Modelos Pydantic
└── banco.db       # Banco de dados (gerado automaticamente)
```

---

##  Aprendizados

Este projeto foi desenvolvido para praticar:
- Criação de APIs REST com FastAPI
- Modelagem e validação de dados com Pydantic
- Operações CRUD com SQLite
- Organização de projetos Python em camadas (routes, models, database)

---

##  Autor

**Nicolas** — [@NicolasDEVoB](https://github.com/NicolasDEVoB)
