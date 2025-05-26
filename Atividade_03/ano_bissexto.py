def verificar_ano_bissexto():
    """
    Solicita um ano ao usuário e determina se ele é bissexto ou não.
    Um ano é bissexto se for divisível por 4, exceto anos centenários
    (divisíveis por 100) que não são divisíveis por 400.
    """
    try:
        ano = int(input("Digite um ano para verificar se é bissexto: "))

        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            print(f"O ano {ano} É bissexto.")
        else:
            print(f"O ano {ano} NÃO é bissexto.")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro para o ano.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    