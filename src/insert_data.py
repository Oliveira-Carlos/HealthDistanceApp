import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

dbname = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")


class DatabaseConnection:
    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cursor = self.conn.cursor()

    def execute_query(self, query, values=None):
        self.cursor.execute(query, values)
        self.conn.commit()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()


# Criação de tabela
create_table_query = """
CREATE TABLE IF NOT EXISTS unidades_saude (
    id SERIAL PRIMARY KEY,
    uf VARCHAR(2),
    municipio VARCHAR(255),
    nome_estabelecimento VARCHAR(255),
    tipo_unidade VARCHAR(255),
    logradouro VARCHAR(255),
    numero VARCHAR(10),
    bairro VARCHAR(255),
    cep VARCHAR(10),
    telefone VARCHAR(20)
);
"""

# Criar conexão com o banco de dados
db = DatabaseConnection(dbname, user, password, host, port)

# Executar a consulta de criação de tabela
db.execute_query(create_table_query)

# Ler CSV com pandas
csv_filename = "database/clean_data/leitos_sus_2023_clean.csv"
df = pd.read_csv(csv_filename, sep=';', encoding='utf-8')

df['TELEFONE'] = df['TELEFONE'].str.slice(0, 20)

# Consulta SQL para inserção dos dados
insert_query = """
INSERT INTO unidades_saude (uf, municipio, nome_estabelecimento, tipo_unidade, logradouro, numero, bairro, cep, telefone)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
"""

# Inserir dados do CSV
for index, row in df.iterrows():
    data = (
        row['UF'], row['MUNICIPIO'], row['NOME_ESTABELECIMENTO'],
        row['TIPO_UNIDADE'], row['LOGRADOURO'], row['NUMERO'],
        row['BAIRRO'], row['CEP'], row['TELEFONE']
    )
    db.execute_query(insert_query, data)

# Fechar a conexão
db.close_connection()
