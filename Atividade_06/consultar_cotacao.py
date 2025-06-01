import requests
import json
from datetime import datetime

def consultar_cotacao_moeda(codigo_moeda: str) -> dict or None:
    """
    Consulta a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL)
    usando a API AwesomeAPI.

    Parâmetros:
        codigo_moeda (str): O código da moeda desejada (ex: "USD", "EUR", "GBP").

    Retorna:
        dict: Um dicionário com os dados da cotação (valor atual, máximo, mínimo,
              data/hora de atualização) se a consulta for bem-sucedida.
              Retorna None se a moeda não for encontrada, a API retornar erro,
              ou ocorrer um problema de conexão.
    """
    # A AwesomeAPI usa o formato {MOEDA}-BRL para cotações em relação ao Real
    api_url = f"https://economia.awesomeapi.com.br/json/last/{codigo_moeda.upper()}-BRL"

    print(f"Consultando cotação para {codigo_moeda.upper()}/BRL...")

    try:
        response = requests.get(api_url, timeout=10) # Adiciona um timeout de 10 segundos

        response.raise_for_status() # Levanta um erro HTTP para status de erro (4xx ou 5xx)

        data = response.json()

        # A estrutura da resposta da AwesomeAPI é:
        # {"USDBRL": { ...dados da cotacao... }}
        # Precisamos da chave dinâmica baseada no código da moeda.
        chave_cotacao = f"{codigo_moeda.upper()}BRL"

        if chave_cotacao not in data:
            print(f"Erro: Cotação para '{codigo_moeda.upper()}/BRL' não encontrada na resposta da API.")
            print("Verifique se o código da moeda está correto (ex: USD, EUR, GBP).")
            return None

        cotacao = data[chave_cotacao]

        # Extrai os dados relevantes
        valor_atual = float(cotacao['bid'])      # Valor de compra (bid)
        valor_maximo = float(cotacao['high'])   # Valor máximo das últimas 24h
        valor_minimo = float(cotacao['low'])    # Valor mínimo das últimas 24h
        timestamp = int(cotacao['timestamp'])   # Timestamp da última atualização

        # Converte o timestamp Unix para um objeto datetime
        data_hora_atualizacao = datetime.fromtimestamp(timestamp)

        # Retorna um dicionário com as informações formatadas
        return {
            "moeda": codigo_moeda.upper(),
            "valor_atual": valor_atual,
            "valor_maximo": valor_maximo,
            "valor_minimo": valor_minimo,
            "data_hora_atualizacao": data_hora_atualizacao
        }

    except requests.exceptions.ConnectionError:
        print("Erro de conexão: Verifique sua conexão com a internet.")
        return None
    except requests.exceptions.Timeout:
        print("Erro de tempo limite: A requisição demorou muito para responder.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"Erro HTTP ao consultar a API: {e}")
        print("Pode ser um problema temporário com a API ou um código de moeda inválido.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro na requisição à API: {e}")
        return None
    except json.JSONDecodeError:
        print("Erro: A resposta da API não é um JSON válido. A API pode estar com problemas.")
        return None
    except ValueError as e:
        print(f"Erro ao converter valores numéricos da API: {e}. A estrutura dos dados pode ter mudado.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return None

# --- Bloco de execução principal ---
if __name__ == "__main__":
    print("--- Consultor de Cotação de Moedas (AwesomeAPI) ---")
    print("Códigos de moeda comuns: USD (Dólar Americano), EUR (Euro), GBP (Libra Esterlina), ARS (Peso Argentino), JPY (Iene Japonês).")
    print("Digite 'fim' a qualquer momento para sair.")

    while True:
        entrada_moeda = input("\nDigite o código da moeda estrangeira (ex: USD): ").strip().upper()

        if entrada_moeda == 'FIM':
            break # Sai do loop se o usuário digitar 'fim'

        if not entrada_moeda:
            print("Por favor, digite um código de moeda.")
            continue

        # Chama a função para consultar a cotação
        dados_cotacao = consultar_cotacao_moeda(entrada_moeda)

        # Exibe as informações se a consulta foi bem-sucedida
        if dados_cotacao:
            print(f"\n--- Cotação {dados_cotacao['moeda']}/BRL ---")
            print(f"Valor Atual (Compra): R$ {dados_cotacao['valor_atual']:.4f}")
            print(f"Valor Máximo (24h): R$ {dados_cotacao['valor_maximo']:.4f}")
            print(f"Valor Mínimo (24h): R$ {dados_cotacao['valor_minimo']:.4f}")
            print(f"Última Atualização: {dados_cotacao['data_hora_atualizacao'].strftime('%d/%m/%Y %H:%M:%S')}")
            print("--------------------------------------")
        else:
            print("Não foi possível obter a cotação para a moeda informada.")

    print("\nObrigado por usar o consultor de cotação de moedas!")