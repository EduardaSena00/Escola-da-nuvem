import json
import os # Para verificar se o arquivo existe

def escrever_dados_json(nome_arquivo, dados_pessoa):
    """
    Escreve um dicionário Python (dados de uma pessoa) em um arquivo JSON.

    Args:
        nome_arquivo (str): O caminho para o arquivo JSON a ser criado/escrito.
        dados_pessoa (dict): Um dicionário contendo 'nome', 'idade' e 'cidade'.
    """
    try:
        # Abre o arquivo no modo de escrita ('w').
        # 'encoding='utf-8'' é importante para caracteres especiais.
        with open(nome_arquivo, 'w', encoding='utf-8') as jsonfile:
            # json.dump serializa (converte) o dicionário Python para uma string JSON
            # e escreve essa string no arquivo.
            # 'indent=4' formata o JSON com indentação para facilitar a leitura humana.
            # 'ensure_ascii=False' permite que caracteres não-ASCII (como acentos) sejam gravados diretamente.
            json.dump(dados_pessoa, jsonfile, indent=4, ensure_ascii=False)
        print(f"Dados escritos com sucesso em '{nome_arquivo}'")
    except IOError as e:
        print(f"Erro de Entrada/Saída ao escrever o arquivo '{nome_arquivo}': {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado na escrita JSON: {e}")

def ler_dados_json(nome_arquivo):
    """
    Lê dados de uma pessoa de um arquivo JSON e os exibe na tela.

    Args:
        nome_arquivo (str): O caminho para o arquivo JSON a ser lido.
    Returns:
        dict: O dicionário com os dados da pessoa lida, ou None se ocorrer um erro.
    """
    # Primeiro, verificamos se o arquivo existe antes de tentar lê-lo
    if not os.path.exists(nome_arquivo):
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        print("Por favor, certifique-se de que o arquivo existe.")
        return None

    try:
        # Abre o arquivo no modo de leitura ('r').
        with open(nome_arquivo, 'r', encoding='utf-8') as jsonfile:
            # json.load desserializa (converte) o conteúdo JSON do arquivo para um dicionário Python.
            dados = json.load(jsonfile)
            print(f"\n--- Conteúdo do arquivo '{nome_arquivo}' ---")
            # Usamos .get() para acessar os campos, fornecendo um valor padrão 'N/D'
            # caso o campo não exista no JSON lido (evita KeyError).
            print(f"Nome: {dados.get('nome', 'N/D')}")
            print(f"Idade: {dados.get('idade', 'N/D')}")
            print(f"Cidade: {dados.get('cidade', 'N/D')}")
            return dados
    except FileNotFoundError:
        # Esta exceção é capturada caso 'os.path.exists' não tenha evitado um erro de concorrência
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado durante a tentativa de leitura.")
    except json.JSONDecodeError as e:
        # Este erro ocorre se o arquivo não contiver JSON válido.
        print(f"Erro de decodificação JSON no arquivo '{nome_arquivo}'. O arquivo pode estar corrompido ou mal formatado: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado na leitura JSON: {e}")
    return None

if __name__ == "__main__":
    # 1. Definir os dados da pessoa que queremos salvar
    minha_pessoa = {
        "nome": "João da Silva",
        "idade": 42,
        "cidade": "Igarassu" # Sua localização atual!
    }

    nome_arquivo_json = 'pessoa.json'

    print("--- Escrevendo dados no arquivo JSON ---")
    # Chama a função para escrever os dados no arquivo JSON
    escrever_dados_json(nome_arquivo_json, minha_pessoa)

    print("\n--- Lendo dados do arquivo JSON ---")
    # Chama a função para ler os dados do arquivo JSON
    dados_lidos = ler_dados_json(nome_arquivo_json)

    # Você pode usar os dados lidos para outras operações
    if dados_lidos:
        print("\nDados lidos com sucesso:")
        print(f"Nome lido: {dados_lidos['nome']}")
        print(f"Idade lida: {dados_lidos['idade']} anos")