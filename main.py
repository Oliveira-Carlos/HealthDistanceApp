from dotenv import load_dotenv
import os
import psycopg2
from geopy.geocoders import Nominatim
from src.calculate_distance import haversine_distance

# Carregue as variáveis de ambiente
load_dotenv()

# Solicitar ao usuário que insira o CEP
cep = input("Digite o CEP: ")

# Extrair os três primeiros dígitos do CEP do usuário
user_prefix = cep[:2]

# Criar uma conexão com o banco de dados
connection = psycopg2.connect(
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

# Criar um cursor
cur = connection.cursor()

# Consulta SQL para selecionar todos os CEPs com os três primeiros dígitos iguais
query = """
    SELECT cep, municipio, nome_estabelecimento, bairro, logradouro, numero, telefone
    FROM unidades_saude
    WHERE LEFT(cep, 2) = %s;
"""

# Execute a consulta SQL usando psycopg2
cur.execute(query, (user_prefix,))

# Recupere todos os CEPs com os três primeiros dígitos iguais
ceps_with_prefix = cur.fetchall()

# Se houver candidatos, calcule as distâncias
if ceps_with_prefix:
    # Inicialize o geocodificador
    geolocator = Nominatim(user_agent="myGeocoder")

    # Lista para armazenar as informações dos CEPs mais próximos
    closest_ceps = []

    # Obtenha as coordenadas para cada CEP e suas informações
    for cep_info in ceps_with_prefix:
        cep_candidate = cep_info[0]
        location = geolocator.geocode(cep_candidate)
        if location:
            coordinates = (location.latitude, location.longitude)
            closest_ceps.append((cep_candidate, coordinates, *cep_info[1:]))

    # Agora você tem a lista dos CEPs com coordenadas e informações

    # Obtenha as coordenadas do CEP do usuário
    user_geocoder = Nominatim(user_agent="myGeocoder")
    user_location = user_geocoder.geocode(cep)

    if user_location:
        user_lat, user_lng = user_location.latitude, user_location.longitude

        # Calcule as distâncias e classifique-as
        candidate_distances = []
        for candidate_cep, candidate_coordinates, *candidate_info in closest_ceps:
            distance = haversine_distance(
                (user_lat, user_lng), candidate_coordinates)
            candidate_distances.append(
                (candidate_cep, distance, *candidate_info))

        candidate_distances.sort(key=lambda x: x[1])

        # Exiba os 10 CEPs mais próximos com informações adicionais
        print("Os 10 CEPs mais próximos são:")
        for candidate_cep, distance, *candidate_info in candidate_distances[:10]:
            print(f"CEP: {candidate_cep}, Distância: {distance} km")
            print(f"Município: {candidate_info[0]}")
            print(f"Estabelecimento: {candidate_info[1]}")
            print(f"Bairro: {candidate_info[2]}")
            print(f"Logradouro: {candidate_info[3]}")
            print(f"Número: {candidate_info[4]}")
            print(f"Telefone: {candidate_info[5]}")
            print("---------")

# Feche o cursor e a conexão
cur.close()
connection.close()
