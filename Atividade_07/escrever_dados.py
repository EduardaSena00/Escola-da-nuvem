import csv

def escrever_dados_csv(nome_arquivo, pessoas):
    """
    Escreve uma lista de dicionários em um arquivo CSV.

    Args:
        nome_arquivo (str): O caminho para o arquivo CSV a ser criado/escrito.
        pessoas (list): Uma lista de dicionários, onde cada dicionário
                        representa uma pessoa com as chaves 'Nome', 'Idade' e 'Cidade'.
    """
    # Define os nomes das colunas, que serão o cabeçalho do seu arquivo CSV
    nomes_colunas = ['Nome', 'Idade', 'Cidade']

    try:
        # Abre o arquivo CSV no modo de escrita ('w').
        # 'newline=''' é importante para evitar linhas em branco extras no CSV.
        # 'encoding='utf-8'' garante que caracteres especiais (acentos, ç) sejam tratados corretamente.
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as csvfile:
            # Cria um objeto DictWriter. Ele mapeia os dicionários (suas 'pessoas')
            # para linhas no arquivo CSV, usando 'fieldnames' como cabeçalho.
            writer = csv.DictWriter(csvfile, fieldnames=nomes_colunas)

            # Escreve a primeira linha do CSV (o cabeçalho)
            writer.writeheader()

            # Escreve todas as linhas de dados do seu dicionário
            writer.writerows(pessoas)

        print(f"Dados escritos com sucesso em '{nome_arquivo}'")

    except IOError as e:
        print(f"Erro de Entrada/Saída ao escrever o arquivo '{nome_arquivo}': {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    # Lista de dicionários, onde cada dicionário é uma pessoa
    # e as chaves correspondem aos 'nomes_colunas' definidos acima.
    dados_pessoas = [
        {'Nome': 'Alice Silva', 'Idade': 30, 'Cidade': 'São Paulo'},
        {'Nome': 'Bruno Costa', 'Idade': 25, 'Cidade': 'Rio de Janeiro'},
        {'Nome': 'Carla Santos', 'Idade': 35, 'Cidade': 'Belo Horizonte'},
        {'Nome': 'Diego Pereira', 'Idade': 28, 'Cidade': 'Igarassu'}, # Sua localização atual!
        {'Nome': 'Fernanda Lima', 'Idade': 22, 'Cidade': 'Olinda'}
    ]

    # Nome do arquivo CSV que será criado
    nome_arquivo_csv = 'pessoas.csv'

    # Chama a função para escrever os dados no arquivo
    escrever_dados_csv(nome_arquivo_csv, dados_pessoas)
    