# ETL em Python

## Descrição
Este projeto de ETL (Extract, Transform, Load) em Python tem como objetivo extrair dados de arquivos Excel em uma determinada pasta, transformá-los e carregá-los em um novo arquivo Excel. O processo de ETL é realizado da seguinte maneira:

1. **Extração (Extract):** Os dados são extraídos dos arquivos Excel na pasta especificada usando a biblioteca Glob.

2. **Transformação (Transform):** Durante a transformação, o código realiza as seguintes operações:

    - Adiciona uma coluna com o nome do arquivo Excel de origem.

    - Determina a localização com base no nome do arquivo e adiciona uma coluna com a localização.

    - Extrai o nome da campanha a partir de uma coluna chamada utm_link e adiciona uma coluna com o nome da campanha.

    - Combina todos os DataFrames resultantes em um único DataFrame.

3. **Carregamento (Load):** O DataFrame resultante da transformação é salvo em um novo arquivo Excel na pasta de saída especificada.

## Tecnologias Utilizadas
    - Python
    - Pandas
    - os
    - glob

## Estrutura do Projeto
- **src/:** Pasta principal do projeto

    - **data/:** Pasta onde os arquivos de entrada e saída estão localizados

        - **raw/:** Pasta contendo os arquivos Excel de entrada

        - **ready/:** Pasta onde o arquivo Excel resultante será salvo

    - **main.py:** Script Python contendo o código do ETL

## Execução do Projeto
Para executar o projeto, basta rodar o script main.py. Certifique-se de ter os arquivos Excel de entrada na pasta data/raw e de ter permissão de escrita na pasta data/ready para salvar o arquivo resultante.

## Observações
Este é um exemplo simplificado de um processo ETL em Python.
O código pode ser expandido para lidar com mais transformações e fontes de dados, dependendo dos requisitos do projeto.