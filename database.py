import psycopg2
from psycopg2.pool import SimpleConnectionPool
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager
from pprint import pprint
from dotenv import load_dotenv
import os


load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "port": os.getenv("DB_PORT")
}

pool = SimpleConnectionPool(minconn=1, maxconn=10, **DB_CONFIG)

@contextmanager
# Criar ou conectar um banco de dados
def get_conn():
    conn = pool.getconn()
    try:
        yield conn, conn.cursor(cursor_factory=RealDictCursor)
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        pool.putconn(conn)


# Criar tabela (se não existir ainda)
def execute():
    with get_conn() as (conn, cursor):
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                user_id SERIAL PRIMARY KEY,
                nome TEXT,
                email TEXT
    )
    """)


execute()


# Inserir dados (INSERT)
def insert(name, email) -> None:
    with get_conn() as (conn, cursor):
        cursor.execute(
            "INSERT INTO usuarios (nome, email) VALUES (%s, %s)",
            (name, email)
        )


# Buscar todos os dados
def read_all() -> list[dict]:
    with get_conn() as (conn, cursor):
        cursor.execute("SELECT * FROM usuarios")
        return cursor.fetchall()


# Buscar dado específico (por id)
def read(user_id: int) -> dict | None:
    with get_conn() as (conn, cursor):
        cursor.execute(
            "SELECT * FROM usuarios WHERE user_id = %s", (user_id,)
        )
        return cursor.fetchone()  # já retorna dict ou None


def delete(user_id: int) -> None:
    with get_conn() as (conn, cursor):
        cursor.execute(
            "DELETE FROM usuarios WHERE user_id = %s", (user_id,)
        )


# Atualiza usuário
def update(user_id: int, name: str, email: str) -> None:
    with get_conn() as (conn, cursor):
        cursor.execute(
            "UPDATE usuarios SET nome = %s, email = %s WHERE user_id = %s",
            (name, email, user_id)
        )