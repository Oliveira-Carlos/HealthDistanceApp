import os
import requests

# URL do arquivo CSV com os dados de locais de atendimento da saúde
csv_url = "https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/Leitos_SUS/Leitos_2023.csv"

# Pasta para salvar os dados brutos
raw_data_folder = "database/raw_data"

# Crie a pasta se ela não existir
if not os.path.exists(raw_data_folder):
    os.makedirs(raw_data_folder)

# Caminho para o arquivo a ser baixado
local_filename = os.path.join(raw_data_folder, "leitos_sus_2023.csv")

# Baixar o arquivo CSV


def download_csv(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"Arquivo {filename} baixado com sucesso.")


# Chama a função para baixar e salvar o arquivo
download_csv(csv_url, local_filename)
