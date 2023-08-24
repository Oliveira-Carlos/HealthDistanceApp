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
cep = '62250000'

link = f'https://viacep.com.br/ws/CE/Ipu/rua 1/json/'

try:
    req_cep = requests.get(link)
    data = req_cep.json()

    if isinstance(data, list) and len(data) > 0:
        # A API retorna uma lista, usamos o primeiro item da lista
        first_item = data[0]
        cidade = first_item.get('localidade', '')
        estado = first_item.get('uf', '')
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
    else:
        print("Resposta da API não está no formato esperado ou está vazia.")
except requests.exceptions.RequestException as e:
    print(f"Erro de requisição: {e}")
