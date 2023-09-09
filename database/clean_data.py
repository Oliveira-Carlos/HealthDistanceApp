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

# Substituir valores nulos em 'NU_TELEFONE' por 'S/N'
df['NU_TELEFONE'].fillna('S/N', inplace=True)

# Dicionário de renomeação de colunas
col_rename_mapping = {
    'NO_LOGRADOURO': 'LOGRADOURO',
    'NO_BAIRRO': 'BAIRRO',
    'CO_CEP': 'CEP',
    'NU_TELEFONE': 'TELEFONE',
    'NU_ENDERECO': 'NUMERO',
    'DS_TIPO_UNIDADE': 'TIPO_UNIDADE',
}

# Renomear colunas somente se as colunas antigas existirem
for old_col, new_col in col_rename_mapping.items():
    if old_col in df.columns:
        df.rename(columns={old_col: new_col}, inplace=True)

# Selecionar apenas as colunas necessárias (usando os nomes renomeados)
columns_to_keep = ['UF', 'MUNICIPIO',
                   'NOME_ESTABELECIMENTO', 'TIPO_UNIDADE', 'LOGRADOURO', 'NUMERO', 'BAIRRO', 'CEP', 'TELEFONE']
df_cleaned = df[columns_to_keep]

# Salvar o DataFrame limpo em um novo arquivo CSV
df_cleaned.to_csv(clean_filename, index=False, sep=';', encoding='utf-8')

print(f"Arquivo {clean_filename} salvo com sucesso.")
