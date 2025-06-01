from datetime import date, timedelta

def calcular_idaide_em_dias(ano_nascimento: int) -> int:
     """
    Calcula a idade de uma pessoa em dias, assumindo o dia 1º de janeiro
    do ano de nascimento e a data atual para o cálculo.

    Parâmetros:
        ano_nascimento (int): O ano em que a pessoa nasceu.

    Retorna:
        int: A idade aproximada da pessoa em dias.
    """
     data_nasc_base = date(ano_nascimento, 1, 1)

     data_atual = date.today()

     diferenca_em_dias = data_atual - data_nasc_base

     return diferenca_em_dias.days

if __name__ == "__main__":
    print("--- Calculadora de idade em dias (baseado no ano de nascimento)---")
    print(f"Considerando a data atual: {date.today().strftime('%d/%m/%Y')}")

    while True:
         try:
              entrada = input("\nDigite o ano de nascimento (ex:1990) ou 'fim' para sair: ")

              if entrada.lower() == 'fim':
                   break
              
              ano_nascimento_str = entrada
              ano_nascimento = int(ano_nascimento_str)
              
              ano_atual = date.today().year
              if not (1900 <= ano_nascimento <= ano_atual):
               print(f"Erro: O ano de nascimento deve ser entre 1900 e {ano_atual}")
              continue
         
         
              idade_em_dias = calcular_idaide_em_dias(ano_nascimento)

              print(f"Uma pessoa nascida em {ano_nascimento} (assumindo 01/01) tem aproximadamente {calcular_idaide_em_dias} dias de vida ")


         except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um ano válido ou 'fim'. ")
         except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}. Por favor, tente novamete.")

print("\nObrigado por usar a calculadora!")


