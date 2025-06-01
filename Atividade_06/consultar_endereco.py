import requests # Importa a biblioteca para fazer requisições HTTP
import json     # Importa a biblioteca para trabalhar com JSON (embora requests.json() já faça isso)

def consultar_cep(cep: str) -> dict or None:
    """
    Consulta informações de endereço a partir de um CEP usando a API ViaCEP.

    Parâmetros:
        cep (str): O número do CEP a ser consultado (pode conter ou não hífen).

    Retorna:
        dict: Um dicionário contendo as informações do endereço (logradouro,
              bairro, localidade, uf) se o CEP for válido e a consulta for bem-sucedida.
              Retorna None se o CEP for inválido, não encontrado ou ocorrer um erro.
    """
    # Limpa o CEP, removendo quaisquer caracteres não numéricos (como hífen)
    cep_limpo = ''.join(filter(str.isdigit, cep))

    # Verifica se o CEP limpo tem o tamanho correto (8 dígitos)
    if len(cep_limpo) != 8:
        print("Erro: O CEP deve conter exatamente 8 dígitos.")
        return None

    # URL da API ViaCEP para consulta por CEP
    # Exemplo: https://viacep.com.br/ws/01001000/json/
    api_url = f"https://viacep.com.br/ws/{cep_limpo}/json/"

    print(f"Consultando CEP: {cep_limpo}...")

    try:
        # Faz a requisição GET para a API
        response = requests.get(api_url)

        # Verifica se a requisição foi bem-sucedida (código de status 200 OK)
        response.raise_for_status() # Levanta um erro HTTP para status de erro (4xx ou 5xx)

        # Converte a resposta JSON para um dicionário Python
        dados_cep = response.json()

        # A API ViaCEP retorna um dicionário com a chave 'erro' se o CEP não for encontrado
        if 'erro' in dados_cep and dados_cep['erro'] == True:
            print(f"Erro: CEP '{cep}' não encontrado ou inválido.")
            return None
        else:
            return dados_cep

    except requests.exceptions.ConnectionError:
        print("Erro de conexão: Verifique sua conexão com a internet.")
        return None
    except requests.exceptions.Timeout:
        print("Erro de tempo limite: A requisição demorou muito para responder.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"Erro HTTP ao consultar o CEP: {e}")
        print("Pode ser um problema temporário com a API ou um CEP mal formatado.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro na requisição: {e}")
        return None
    except json.JSONDecodeError:
        print("Erro: A resposta da API não é um JSON válido.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return None

# --- Bloco de execução principal ---
if __name__ == "__main__":
    print("--- Consultor de Endereços por CEP (ViaCEP) ---")
    print("Digite 'fim' a qualquer momento para sair.")

    while True:
        entrada_cep = input("\nDigite o CEP (apenas números ou com hífen): ").strip()

        if entrada_cep.lower() == 'fim':
            break # Sai do loop se o usuário digitar 'fim'

        # Chama a função para consultar o CEP
        dados_endereco = consultar_cep(entrada_cep)

        # Exibe as informações se a consulta foi bem-sucedida
        if dados_endereco:
            print("\n--- Informações do Endereço ---")
            print(f"CEP: {dados_endereco.get('cep', 'Não informado')}")
            print(f"Logradouro: {dados_endereco.get('logradouro', 'Não informado')}")
            print(f"Complemento: {dados_endereco.get('complemento', 'Não informado')}") # Complemento pode ser vazio
            print(f"Bairro: {dados_endereco.get('bairro', 'Não informado')}")
            print(f"Cidade: {dados_endereco.get('localidade', 'Não informado')}") # 'localidade' é o nome da cidade na API
            print(f"Estado (UF): {dados_endereco.get('uf', 'Não informado')}")
            # print(f"DDD: {dados_endereco.get('ddd', 'Não informado')}") # Exemplo de outros campos
            print("-------------------------------")
        else:
            print("Não foi possível obter os dados para o CEP informado.")

    print("\nObrigado por usar o consultor de CEP!")