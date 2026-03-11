import sqlite3

DB = "banco.db"

# Criar ou conectar um banco de dados
def get_conn():
    conn = sqlite3.connect(DB)
    return conn, conn.cursor()


# Criar tabela (se não existir ainda)
def execute():
    conn, cursor = get_conn()
    cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT
)
""")
    conn.commit()


execute()


# Inserir dados (INSERT)
def insert(name, email) -> None:
    conn, cursor = get_conn()
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)",(name, email))
    conn.commit()


# Buscar todos os dados
def read_all() -> list[dict]:
    conn, cursor = get_conn()
    cursor.execute("SELECT * FROM usuarios")
    rows = cursor.fetchall()
    return [{"user_id": row[0], "nome": row[1], "email": row[2]} for row in rows]


# Buscar dado específico (por id)
def read(user_id: int) -> dict | None:
    conn, cursor = get_conn()
    cursor.execute("SELECT * FROM usuarios WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    if row is None:
        return None
    return {"user_id": row[0], "nome": row[1], "email": row[2]}


# Deleta um usuário pelo id
def delete(user_id: int) -> None:
    conn, cursor = get_conn()
    cursor.execute("DELETE FROM usuarios WHERE user_id = ?",(user_id,))
    conn.commit()


# Atualiza usuário
def update(user_id: int, name: str, email: str) -> None:
    conn, cursor = get_conn()
    cursor.execute(
        "UPDATE usuarios SET nome = ?, email = ? WHERE user_id = ?",
        (name, email, user_id)
    )
    conn.commit()