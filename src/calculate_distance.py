import math
from src.request_cep import CEPRequester


def haversine_distance(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    radius = 6371  # Raio médio da Terra em quilômetros
    dlat = (lat2 - lat1) * (3.141592653589793 / 180)
    dlon = (lon2 - lon1) * (3.141592653589793 / 180)
    a = (pow(math.sin(dlat / 2), 2) + math.cos(lat1 * (3.141592653589793 / 180))
         * math.cos(lat2 * (3.141592653589793 / 180)) * pow(math.sin(dlon / 2), 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius * c
    return distance


def find_closest_locations(user_coordinates, locations):
    # Criar uma instância da classe CEPRequester
    cep_requester = CEPRequester()

    # Calcula a distância entre o usuário e todas as localidades
    distances = []
    for location in locations:
        location_coordinates = (location['latitude'], location['longitude'])

        # Obter coordenadas a partir do CEP se não estiverem disponíveis
        if None in location_coordinates:
            location_coordinates = cep_requester.get_coordinates(
                location['cep'])

        # Calcular a distância se as coordenadas estiverem disponíveis
        if None not in location_coordinates:
            distance = haversine_distance(
                user_coordinates, location_coordinates)
            distances.append((location, distance))

    # Classifica as localidades com base na distância
    distances.sort(key=lambda x: x[1])

    # Retorna as 10 localidades mais próximas
    return distances[:10]
