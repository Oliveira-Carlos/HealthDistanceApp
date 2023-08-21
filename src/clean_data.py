import pandas as pd
import os

# Pasta com dados brutos e limpos
raw_data_folder = "database/raw_data"
clean_data_folder = "database/clean_data"

# Nome dos arquivos
raw_filename = os.path.join(raw_data_folder, "municipios.csv")
clean_filename = os.path.join(clean_data_folder, "municipios_clean.csv")

# Carregar o arquivo CSV em um DataFrame
df = pd.read_csv(raw_filename, sep=',', encoding='utf-8')

# Selecionar apenas as colunas "nome", "latitude" e "longitude"
selected_columns = ["nome", "latitude", "longitude"]
clean_df = df[selected_columns]

# Salvar o DataFrame limpo em um novo arquivo CSV
clean_df.to_csv(clean_filename, index=False)

print(f"Dados limpos salvos em {clean_filename}")
