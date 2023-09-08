from dotenv import load_dotenv
import os
import psycopg2
from geopy.geocoders import Nominatim

# Função para obter as coordenadas de latitude e longitude a partir de um endereço


def get_coordinates(address):
    locator = Nominatim(user_agent="myGeocoder")
    location = locator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None


load_dotenv()

dbname = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")

# Solicitar ao usuário que insira o CEP
cep = input("Digite o CEP: ")

# Consulta SQL para obter informações do CEP
query = f"SELECT municipio, uf FROM unidades_saude WHERE cep = '{cep}'"

try:
    # Conectar ao banco de dados
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )

    # Criar um cursor
    cur = conn.cursor()

    # Executar a consulta SQL
    cur.execute(query)

    # Obter os resultados da consulta
    result = cur.fetchone()

    # Verificar se o CEP foi encontrado no banco de dados
    if result:
        cidade, estado = result

        # Construir o endereço a partir da cidade e estado
        endereco = f"{cidade}, {estado}"

        # Obter as coordenadas
        latitude, longitude = get_coordinates(endereco)

        if latitude is not None and longitude is not None:
            print(f"Coordenadas de {cidade}, {estado}:")
            print(f"Latitude: {latitude}")
            print(f"Longitude: {longitude}")
        else:
            print("Não foi possível obter as coordenadas do endereço.")
    else:
        print("CEP não encontrado no banco de dados.")

except psycopg2.Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")

finally:
    # Fechar a conexão com o banco de dados
    if conn is not None:
        conn.close()
