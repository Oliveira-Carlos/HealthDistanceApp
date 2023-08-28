import requests
from geopy.geocoders import Nominatim

# Função para obter as coordenadas de latitude e longitude a partir de um endereço


def get_coordinates(address):
    locator = Nominatim(user_agent="myGeocoder")
    location = locator.geocode(address)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None


# Viacep
cep = '54505560'

link = f'https://viacep.com.br/ws/{cep}/json/'

try:
    req_cep = requests.get(link)
    data = req_cep.json()

    cidade = data.get('localidade', '')  # 'localidade' é a cidade
    estado = data.get('uf', '')          # 'uf' é o estado
    if cidade and estado:
        endereco = f"{cidade}, {estado}"  # Ordem correta: "cidade, estado"
        latitude, longitude = get_coordinates(endereco)
        if latitude is not None and longitude is not None:
            print(f"Coordenadas de {cidade}, {estado}:")
            print(f"Latitude: {latitude}")
            print(f"Longitude: {longitude}")
        else:
            print("Não foi possível obter as coordenadas do endereço.")
    else:
        print("Dados incompletos na resposta da API.")
except requests.exceptions.RequestException as e:
    print(f"Erro de requisição: {e}")
