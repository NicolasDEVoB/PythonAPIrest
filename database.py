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
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT
)
""")
    conn.commit()


execute()


# Inserir dados (INSERT)
def insert(name, email):
    conn, cursor = get_conn()
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)",(name, email))
    conn.commit()


# Buscar todos os dados
def read_all():
    conn, cursor = get_conn()
    cursor.execute("SELECT * FROM usuarios")
    rows = cursor.fetchall()
    return [{"id": row[0], "nome": row[1], "email": row[2]} for row in rows]


# Buscar dado específico (por id)
def read(id):
    conn, cursor = get_conn()
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
    row = cursor.fetchone()
    if row is None:
        return None
    return {"id": row[0], "nome": row[1], "email": row[2]}


# Deleta um usuário pelo id
def delete(id):
    conn, cursor = get_conn()
    cursor.execute("DELETE FROM usuarios WHERE id = ?",(id,))
    conn.commit()
