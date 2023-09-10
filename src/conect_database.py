import os
import psycopg2


class DatabaseConnector:
    def __init__(self):
        self.conn = None

    def connect(self):
        try:
            # Informações de conexão com o banco de dados
            dbname = os.getenv("DB_NAME")
            user = os.getenv("DB_USER")
            password = os.getenv("DB_PASS")
            host = os.getenv("DB_HOST")
            port = os.getenv("DB_PORT")

            # Conectar ao banco de dados
            self.conn = psycopg2.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
                port=port
            )
        except psycopg2.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def close_connection(self):
        # Fechar a conexão com o banco de dados
        if self.conn is not None:
            self.conn.close()
