import math


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
