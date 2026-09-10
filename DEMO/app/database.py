import psycopg2
from psycopg2.extras import RealDictCursor

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "demo01",
    "user": "postgres",
    "password": "1234",
}


def get_connection():
    """Crée et retourner une nouvelle connexion à PostgreSQL"""
    return psycopg2.connect(**DB_CONFIG, cursor_factory=RealDictCursor)


def init_db():
    """Crée la table si elle n'existe pas déjà"""
    conn = get_connection()
    cur = conn.cursor()  # permet de tapé et executer du SQL

    cur.execute(
        """
                CREATE TABLE IF NOT EXISTS items(
                    id  SERIAL PRIMARY KEY,
                    name VARCHAR(100),
                    description VARCHAR(255),
                    price FLOAT
                );
                """
    )
    conn.commit()
    cur.close()
    conn.close()
