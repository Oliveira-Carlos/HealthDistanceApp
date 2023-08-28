import pandas as pd
import os

# Pasta com dados brutos e limpos
raw_data_folder = "database/raw_data"
clean_data_folder = "database/clean_data"

# Nome dos arquivos
raw_filename = os.path.join(raw_data_folder, "leitos_sus_2023.csv")
clean_filename = os.path.join(clean_data_folder, "leitos_sus_2023_clean.csv")

# Ler o arquivo CSV com a codificação ISO-8859-1
df = pd.read_csv(raw_filename, sep=',', encoding='iso-8859-1')

# Selecionar apenas as colunas necessárias
columns_to_keep = ['UF', 'MUNICIPIO',
                   'NOME_ESTABELECIMENTO', 'DS_TIPO_UNIDADE', 'NO_LOGRADOURO', 'NU_ENDERECO', 'NO_BAIRRO', 'CO_CEP', 'NU_TELEFONE']
df_cleaned = df[columns_to_keep]

# Salvar o DataFrame limpo em um novo arquivo CSV
df_cleaned.to_csv(clean_filename, index=False, sep=';', encoding='utf-8')

print(f"Arquivo {clean_filename} salvo com sucesso.")
