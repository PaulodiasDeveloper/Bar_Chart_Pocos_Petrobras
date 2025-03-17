import os
import pandas as pd

# Define a pasta onde estão os arquivos
data_arquivo_folder = 'data'

# Inicializa uma lista para armazenar os DataFrames
df = []

# Percorre todos os arquivos na pasta
for file in os.listdir(data_arquivo_folder):
    # Verifica se o arquivo termina com a extensão .xlsx
    if file.endswith('.xlsx'):
        print('Carregando arquivo {0}...'.format(file))
        try:
            # Lê o conteúdo do arquivo e adiciona à lista de DataFrames
            df.append(pd.read_excel(os.path.join(data_arquivo_folder, file)))
        except Exception as e:
            print(f'Erro ao carregar o arquivo {file}: {e}')

# Verifica se carregou algum arquivo
if len(df) == 0:
    print("Nenhum arquivo .xlsx encontrado na pasta.")
else:
    print(f'Total de arquivos carregados: {len(df)}')

    try:
        # Junta todos os DataFrames em um único DataFrame principal
        df_principal = pd.concat(df, axis=0)

        # Salva o DataFrame final em um novo arquivo Excel
        output_file = 'data/master_store.xlsx'
        df_principal.to_excel(output_file, index=False)
        print(f'Dados consolidados salvos em {output_file}')
    
    except Exception as e:
        print(f'Erro ao salvar o arquivo consolidado: {e}')
