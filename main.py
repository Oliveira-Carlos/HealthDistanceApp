from dotenv import load_dotenv
import os
import psycopg2
from geopy.geocoders import Nominatim
from src.calculate_distance import haversine_distance

# Carregue as variáveis de ambiente
load_dotenv()

# Solicitar ao usuário que insira o CEP
cep = input("Digite o CEP: ")

# Inicialize o geocodificador para obter coordenadas do CEP do usuário
user_geocoder = Nominatim(user_agent="myGeocoder")
user_location = user_geocoder.geocode(cep)
if user_location:
    user_lat, user_lng = user_location.latitude, user_location.longitude
else:
    print("Não foi possível encontrar coordenadas para o CEP inserido.")

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

# Extrair os primeiros 5, 4, 3, ... dígitos do CEP do usuário e procurar no banco de dados
cep_prefix = cep[:5]
found_results = False  # Variável para rastrear se resultados foram encontrados

while cep_prefix:
    # Consulta SQL para selecionar todos os CEPs com os dígitos iguais ao prefixo
    query = """
        SELECT cep, municipio, nome_estabelecimento, bairro, logradouro, numero, telefone
        FROM unidades_saude
        WHERE LEFT(cep, %s) = %s;
    """

    # Execute a consulta SQL usando psycopg2
    cur.execute(query, (len(cep_prefix), cep_prefix))

    # Recupere todos os CEPs com os dígitos iguais ao prefixo
    ceps_with_prefix = cur.fetchall()

    # Se houver candidatos, calcule as distâncias
    if ceps_with_prefix:
        # Lista para armazenar as informações dos CEPs mais próximos
        closest_ceps = []

        # Obtenha as coordenadas e informações para cada CEP
        for cep_info in ceps_with_prefix:
            cep_candidate = cep_info[0]
            location = user_geocoder.geocode(cep_candidate)

            # Verifique se a localização foi encontrada
            if location:
                coordinates = (location.latitude, location.longitude)
                closest_ceps.append(
                    (cep_candidate, coordinates, *cep_info[1:]))
            else:
                # Se não encontrou as coordenadas pelo CEP, tente pelo endereço
                # Concatena todas as informações de endereço
                address = ", ".join(cep_info[1:])
                location = user_geocoder.geocode(address)
                if location:
                    coordinates = (location.latitude, location.longitude)
                    closest_ceps.append(
                        (cep_candidate, coordinates, *cep_info[1:]))
                else:
                    print(
                        f"Coordenadas não encontradas para CEP ou endereço: {cep_candidate} - {address}")
                    closest_ceps.append((cep_candidate, None, *cep_info[1:]))

        # Calcule as distâncias e classifique-as
        candidate_distances = []
        for candidate_cep, candidate_coordinates, *candidate_info in closest_ceps:
            if candidate_coordinates:
                distance = haversine_distance(
                    (user_lat, user_lng), candidate_coordinates)
                candidate_distances.append(
                    (candidate_cep, distance, *candidate_info))
            else:
                candidate_distances.append(
                    (candidate_cep, None, *candidate_info))

        # Remova os candidatos que não têm coordenadas
        candidate_distances = [
            c for c in candidate_distances if c[1] is not None]

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

        found_results = True  # Resultados encontrados
        break  # Saia do loop, pois encontrou resultados
    else:
        # Remova o último dígito do prefixo e continue a busca
        cep_prefix = cep_prefix[:-1]

# Mensagem para o caso de não encontrar resultados
if not found_results:
    print("Não foram encontrados resultados para nenhum CEP semelhante.")

# Feche o cursor e a conexão
cur.close()
connection.close()
