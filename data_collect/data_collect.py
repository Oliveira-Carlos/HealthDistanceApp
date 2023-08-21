import pandas as pd
import os

# URL do arquivo CSV
csv_url = "https://raw.githubusercontent.com/kelvins/Municipios-Brasileiros/main/csv/municipios.csv"

# Pasta para salvar os dados brutos
raw_data_folder = "database/raw_data"

# Crie a pasta se ela não existir
if not os.path.exists(raw_data_folder):
    os.makedirs(raw_data_folder)

# arquivo a ser baixado
local_filename = os.path.join(raw_data_folder, "municipios.csv")

# Baixar o arquivo CSV


def download_csv(url, filename):
    df = pd.read_csv(url, sep=',', encoding='utf-8')
    df.to_csv(filename, index=False)
    print(f"Arquivo {filename} baixado com sucesso.")


# Chama a função para baixar e salvar o arquivo
download_csv(csv_url, local_filename)
