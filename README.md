HealthDistanceApp

HealthDistanceApp é um projeto que utiliza dados de unidades de saúde para calcular distâncias entre elas. Este README fornece informações sobre a fonte dos dados e como usar o projeto.

## Fonte dos Dados

Os dados utilizados neste projeto foram obtidos a partir da [Fonte de Dados de Saúde do Governo](https://exemplo.gov.br/dados-de-saude), que fornece informações sobre unidades de saúde em todo o país. Os dados foram baixados no formato CSV e foram limpos para análise e cálculo de distâncias.

## Como Usar o Projeto

### Configuração do Ambiente

1. Certifique-se de ter Python 3.11.2 instalado no seu sistema.

2. Se preferir crie um ambiente virtual usando `virtualenv`, `pyenv` ou `poetry`. Você pode criar um ambiente virtual.

3. Crie um arquivo `.env` na raiz do seu projeto com as configurações do banco de dados no seguinte formato, modifique com os dados reais do seu banco de dados:

    ```env
    DB_NAME=nome_projeto
    DB_USER=postgres
    DB_PASS=senhadb
    DB_HOST=localhost
    DB_PORT=5432

    ```

### Instale as dependências do projeto a partir do arquivo requirements.txt:

1.  ```bash
    pip install -r requirements.txt
    ```

### !! Daqui para baixo ainda em produção

2.  Execute o projeto com o seguinte comando:

    ```bash
    python main.py
    ```

3.  O projeto irá calcular as distâncias entre unidades de saúde e fornecer os resultados.
