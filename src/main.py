import pandas as pd
import os # para manipula diretórios
import glob # para manipular diretórios e nomes de arquivos em massa.

# caminho para ler os arquivos
folder_path = "src\\data\\raw"

# lista os arquivos de excel
excel_files = glob.glob(os.path.join(folder_path, '*.xlsx'))

if not excel_files:
    print("Nenhum arquivo compatível encontrado!")

else:
    # dataframe - tabela na memória para guardar os conteúdos dos arquivos
    dfs = []

    for excel_file in excel_files:
        # Tratativa de erro
        try:
            # leio o arquivo de excel
            df_temp = pd.read_excel(excel_file)

            # pego o nome do arquivo
            file_name = os.path.basename(excel_file)

            # crio a coluna chamada "file_name" com o nome dos arquivos no dataframe df_temp
            df_temp["file_name"] = file_name
            
            # crio a coluna chamada "location" com o nome de cada país dos arquivos no dataframe df_temp
            if "brasil" in file_name.lower():
                df_temp["location"] = "br"
            elif "france" in file_name.lower():
                df_temp["location"] = "fr"
            elif "italian" in file_name.lower():
                df_temp["location"] = "it"
            
            # crio uma nova coluna chamada "campanha" pegando os nomes das campanhas nos links da coluna utm_link
            df_temp["campaign"] = df_temp["utm_link"].str.extract(r"utm_campaign=(.*)")

            # guardo dados tratados dentro de um dataframe
            dfs.append(df_temp)


        except Exception as e:
            print(f"Erro ao ler o arquivo {excel_file} : {e}")

# se o dfs não estiver vazio...
if dfs:

    # concatena todas as tabelas salvas no dfs em uma única tabela
    result = pd.concat(dfs, ignore_index=True)

    # caminho de saída
    output_file = os.path.join("src", "data", "ready", "clean.xlsx")

    # configuro o motor de escrita
    writer = pd.ExcelWriter(output_file, engine="xlsxwriter")

    # leva os dados do resultado a serem escritos no motor de excel configurado
    result.to_excel(writer, index=False)

    # salva o arquivo de excel
    writer._save()

else:
    print("Nenhum dado para ser salvo!")