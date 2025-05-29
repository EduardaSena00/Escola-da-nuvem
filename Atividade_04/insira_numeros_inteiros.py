def verificar_par_impar():

    cont_pares = 0
    cont_impares = 0

    print("Digite números inteiros. Digite 'fim' para encerrar.")

    while True:
        entrada = input("Insira um número: ").strip().lower()

        if entrada == 'fim':
            break
        try:
            numero = int(entrada) 
            if numero % 2 == 0:
                print(F"O número {numero} é PAR.")
                cont_pares += 1
            else: 
                print(f"O número {numero} é IMPAR")
                cont_pares += 1
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número inteiro ou 'fim'.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}. Por favor, tente novamente.")

        print("\n--- Resumo ---")
        print(f"Total de números pares inseridos: {cont_pares}")
        print(f"Total de números ímpares inseridos: {cont_impares}")

        if __name__ == "__main__":
            verificar_par_impar()
