import requests
from geopy.geocoders import Nominatim


class CEPRequester:
    def __init__(self):
        self.locator = Nominatim(user_agent="myGeocoder")

    def get_coordinates(self, address):
        location = self.locator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None

    def request_cep(self, cep):
        link = f'https://viacep.com.br/ws/{cep}/json/'

        try:
            req_cep = requests.get(link)
            data = req_cep.json()

            cidade = data.get('localidade', '')  # 'localidade' é a cidade
            estado = data.get('uf', '')          # 'uf' é o estado
            if cidade and estado:
                # Ordem correta: "cidade, estado"
                endereco = f"{cidade}, {estado}"
                latitude, longitude = self.get_coordinates(endereco)
                return cidade, estado, latitude, longitude
        except requests.exceptions.RequestException as e:
            print(f"Erro de requisição: {e}")

        return None, None, None, None
