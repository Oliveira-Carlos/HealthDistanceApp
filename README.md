HealthDistanceApp

HealthDistanceApp é um projeto que utiliza dados de unidades de saúde para calcular distâncias entre elas e o usuário. Este README fornece informações sobre a fonte dos dados e como usar o projeto.

## Fonte dos Dados

Os dados utilizados neste projeto foram obtidos a partir da [Fonte de Dados de Saúde do Governo](https://opendatasus.saude.gov.br/nl/dataset/hospitais-e-leitos/resource/5701f27f-a202-4605-a944-7dbe888c0445), que fornece informações sobre unidades de saúde em todo o país. Os dados foram baixados no formato CSV e foram limpos para análise e cálculo de distâncias.

## Como Usar o Projeto

### Configuração do Ambiente

1. Certifique-se de ter Python 3.11.2 ou superior instalado no seu ambiente.
2. Se preferir crie um ambiente virtual usando `virtualenv`, `pyenv` ou `poetry`.
3. Crie um arquivo `.env` na raiz do seu projeto com as configurações do banco de dados no seguinte formato, modifique com os dados reais do seu banco de dados:

    ```env
    DB_NAME=nome_projeto
    DB_USER=postgres
    DB_PASS=senhadb
    DB_HOST=localhost
    DB_PORT=5432

    ```

### Instale as dependências do projeto a partir do arquivo requirements.txt:

1. ```bash
   pip install -r requirements.txt
   ```
1. ```bash
   python run database/insert_data.py
   ```

### Executar script pricipal do app

1. Execute o projeto com o seguinte comando:

    ```bash
    python main.py
    ```

2. O projeto irá calcular as distâncias entre unidades de saúde e fornecer os resultados.
