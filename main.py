import psycopg2
from dotenv import load_dotenv
import os
from src.conect_database import DatabaseConnector
from src.request_cep import CEPRequester
from src.calculate_distance import haversine_distance

load_dotenv()

# Solicitar ao usuário que insira o CEP
cep = input("Digite o CEP: ")

# Criar uma instância da classe CEPRequester e obter as coordenadas do CEP
cep_requester = CEPRequester()
user_coordinates = cep_requester.get_coordinates(cep)

if user_coordinates:
    print(f"Coordenadas do CEP {cep}:")
    print(f"Latitude: {user_coordinates[0]}")
    print(f"Longitude: {user_coordinates[1]}")

    # Criar uma instância da classe DatabaseConnector e conectar ao banco de dados
    db_connector = DatabaseConnector()
    db_connector.connect()
