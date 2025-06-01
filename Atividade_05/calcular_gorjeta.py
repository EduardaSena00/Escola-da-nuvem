def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

    Parâmetros:
        valor_conta (float): O valor total da conta.
        porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%).

    Retorna:
        float: O valor da gorjeta calculada.
    """
    if valor_conta < 0:
        raise ValueError("O valor da conta não pode ser negativo.")
    if not 0 <= porcentagem_gorjeta <= 100:
        raise ValueError("A porcentagem da gorjeta deve estar entre 0 e 100.")

    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

# --- Exemplo de uso interativo ---

if __name__ == "__main__":
    print("Bem-vindo à Calculadora de Gorjeta!")

    while True:
        try:
            # Solicita o valor da conta
            entrada_conta = input("Digite o valor total da conta (ou 'fim' para sair): ").strip().replace(',', '.')
            if entrada_conta.lower() == 'fim':
                break

            valor_conta = float(entrada_conta)

            # Solicita a porcentagem da gorjeta
            entrada_porcentagem = input("Digite a porcentagem de gorjeta desejada (ex: 15 para 15%): ").strip().replace(',', '.')
            porcentagem_gorjeta = float(entrada_porcentagem)

            # Calcula a gorjeta usando a função
            gorjeta_calculada = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
            valor_total_com_gorjeta = valor_conta + gorjeta_calculada

            # Exibe os resultados
            print(f"\n--- Resumo ---")
            print(f"Valor da conta: R${valor_conta:.2f}")
            print(f"Porcentagem da gorjeta: {porcentagem_gorjeta:.2f}%")
            print(f"Valor da gorjeta: R${gorjeta_calculada:.2f}")
            print(f"Total a pagar (conta + gorjeta): R${valor_total_com_gorjeta:.2f}")
            print("-" * 20)

        except ValueError as e:
            print(f"Erro: {e}. Por favor, digite um número válido.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}. Por favor, tente novamente.")

    print("Obrigado por usar a calculadora de gorjeta!")