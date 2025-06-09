import csv
import os # Importamos 'os' para verificar se o arquivo existe antes de tentar lê-lo

def ler_dados_csv(nome_arquivo):
    """
    Lê um arquivo CSV com informações de pessoas (Nome, Idade, Cidade)
    e exibe seus dados na tela.

    Args:
        nome_arquivo (str): O caminho para o arquivo CSV a ser lido.
    """
    # Primeiro, verificamos se o arquivo realmente existe
    if not os.path.exists(nome_arquivo):
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado no diretório atual.")
        print("Por favor, certifique-se de que o arquivo existe e o caminho está correto.")
        print("Se você usou o script anterior, o arquivo 'pessoas.csv' deve estar na mesma pasta.")
        return

    try:
        # Abre o arquivo CSV no modo de leitura ('r').
        # 'newline=''' ainda é importante para garantir a leitura correta em diferentes SOs.
        # 'encoding='utf-8'' é crucial para lidar com caracteres especiais (acentos, ç).
        with open(nome_arquivo, 'r', newline='', encoding='utf-8') as csvfile:
            # csv.DictReader lê cada linha como um dicionário.
            # As chaves do dicionário serão os nomes das colunas do CSV (a primeira linha).
            reader = csv.DictReader(csvfile)

            print(f"\n--- Conteúdo do arquivo '{nome_arquivo}' ---")
            
            # Iteramos sobre cada linha lida pelo DictReader
            for linha in reader:
                # Acessamos os dados usando os nomes das colunas como chaves
                # .get() é usado para evitar KeyError se uma coluna não existir na linha
                nome = linha.get('Nome', 'N/D') # 'N/D' = Não Disponível, caso a coluna não exista
                idade = linha.get('Idade', 'N/D')
                cidade = linha.get('Cidade', 'N/D')
                
                print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")

    except FileNotFoundError:
        # Esta exceção é capturada caso 'os.path.exists' não tenha evitado um erro de concorrência
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado durante a tentativa de leitura.")
    except KeyError as e:
        # Este erro ocorre se o cabeçalho do CSV não tiver as colunas esperadas
        print(f"Erro: Coluna '{e}' não encontrada no arquivo CSV. Verifique se o cabeçalho está correto (Nome, Idade, Cidade).")
    except Exception as e:
        # Captura qualquer outro erro inesperado
        print(f"Ocorreu um erro inesperado ao ler o arquivo: {e}")

if __name__ == "__main__":
    # Nome do arquivo CSV que esperamos ler
    nome_arquivo_csv = 'pessoas.csv'

    # Chama a função para ler e exibir os dados
    ler_dados_csv(nome_arquivo_csv)

    print("\nLeitura do arquivo CSV finalizada.")
    