while True:
        num1_str = input("Digite o primeiro número: ")
        num1 = float(num1_str)

        num2_str = input("Digite o segundo núemro: ")
        num2 = float(num2_str)

        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
             resultado = num1 * num2
        elif operacao == '/':
             if num2 == 0:
                  raise ZeroDivisionError("Erro: Divisão por zero não é permitida")
             resultado = num1 / num2
        else:
             raise ValueError("Erro: Operação inválida. use +, -, *, ou /.")
        
        print(f"Resultado: {resultado}")
        break # Encerrar o programa após uma operação bem-sucedida
        