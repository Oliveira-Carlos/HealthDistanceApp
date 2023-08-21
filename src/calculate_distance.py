import pandas as pd
import os
import math

# Função para calcular a distância em quilômetros entre duas coordenadas geográficas


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


# Pasta com dados limpos
clean_data_folder = "database/clean_data"

# Nome do arquivo com dados limpos
clean_filename = os.path.join(clean_data_folder, "municipios_clean.csv")

# Carregar o DataFrame com os dados limpos
df = pd.read_csv(clean_filename)

# Solicitar ao usuário para inserir os nomes das cidades
cidade1_nome = input("Digite o nome da primeira cidade: ")
cidade2_nome = input("Digite o nome da segunda cidade: ")

# Verificar se as cidades existem no DataFrame
cidade1_data = df[df['nome'].str.lower() == cidade1_nome]
cidade2_data = df[df['nome'].str.lower() == cidade2_nome]

if cidade1_data.empty or cidade2_data.empty:
    print("Pelo menos uma das cidades não foi encontrada no CSV.")
else:
    # Selecionar coordenadas das cidades
    cidade1_coord = cidade1_data[['latitude', 'longitude']].values[0]
    cidade2_coord = cidade2_data[['latitude', 'longitude']].values[0]

    # Calcular a distância
    distance = haversine_distance(cidade1_coord, cidade2_coord)
    print(
        f"A distância pela fórmula de haversine entre {cidade1_nome} e {cidade2_nome} é: {distance:.2f} km.")
