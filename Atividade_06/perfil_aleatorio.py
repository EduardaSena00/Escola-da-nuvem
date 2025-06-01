import requests # Importa a biblioteca para fazer requisições HTTP

def gerar_perfil_usuario_aleatorio():
    """
    Gera e exibe um perfil de usuário aleatório usando a API 'Random User Generator'.
    Exibe o nome completo, e-mail e país do usuário gerado.
    """
    api_url = "https://randomuser.me/api/"

    print("Gerando um perfil de usuário aleatório...")

    try:
        # Faz a requisição GET para a API
        response = requests.get(api_url)

        # Verifica se a requisição foi bem-sucedida (código de status 200)
        response.raise_for_status() # Levanta um erro HTTP para status de erro (4xx ou 5xx)

        # Converte a resposta JSON para um dicionário Python
        data = response.json()

        # A API retorna uma lista de 'results', onde cada item é um usuário
        # Pegamos o primeiro (e único, por padrão) usuário gerado
        usuario = data['results'][0]

        # Extrai as informações desejadas
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        # Exibe as informações
        print("\n--- Perfil de Usuário Aleatório ---")
        print(f"Nome: {nome}")
        print(f"Email: {email}")
        print(f"País: {pais}")
        print("-----------------------------------")

    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar à API ou fazer a requisição: {e}")
        print("Verifique sua conexão com a internet ou o endereço da API.")
    except KeyError as e:
        print(f"Erro ao processar os dados da API: Chave não encontrada - {e}")
        print("A estrutura da resposta da API pode ter mudado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# --- Execução do Programa ---
if __name__ == "__main__":
    gerar_perfil_usuario_aleatorio()

    # Você pode adicionar um loop para gerar múltiplos usuários se quiser
    # while True:
    #     gerar_perfil_usuario_aleatorio()
    #     resposta = input("\nGerar outro perfil? (s/n): ").strip().lower()
    #     if resposta != 's':
    #         break
    # print("Programa encerrado.")