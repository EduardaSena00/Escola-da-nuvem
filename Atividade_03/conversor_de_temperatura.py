def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_para_kelvin(fahrenheit):
    return celsius_para_kelvin(fahrenheit_para_celsius(fahrenheit))

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def kelvin_para_fahrenheit(kelvin):
    return celsius_para_fahrenheit(kelvin_para_celsius(kelvin))

def converter_temperatura():
    print("--- Conversor de Temperatura ---")
    
    try:
        temperatura = float(input("Digite a temperatura: "))
        
        unidade_origem = input("Qual a unidade de origem? (C/F/K): ").upper()
        if unidade_origem not in ['C', 'F', 'K']:
            print("Unidade de origem inválida. Por favor, use C, F ou K.")
            return

        unidade_destino = input("Para qual unidade deseja converter? (C/F/K): ").upper()
        if unidade_destino not in ['C', 'F', 'K']:
            print("Unidade de destino inválida. Por favor, use C, F ou K.")
            return

        if unidade_origem == unidade_destino:
            print(f"A temperatura já está na unidade desejada: {temperatura:.2f} {unidade_origem}")
            return

        resultado = None
        
        # Lógica de conversão
        if unidade_origem == 'C':
            if unidade_destino == 'F':
                resultado = celsius_para_fahrenheit(temperatura)
            elif unidade_destino == 'K':
                resultado = celsius_para_kelvin(temperatura)
        
        elif unidade_origem == 'F':
            if unidade_destino == 'C':
                resultado = fahrenheit_para_celsius(temperatura)
            elif unidade_destino == 'K':
                resultado = fahrenheit_para_kelvin(temperatura)
                
        elif unidade_origem == 'K':
            if unidade_destino == 'C':
                resultado = kelvin_para_celsius(temperatura)
            elif unidade_destino == 'F':
                resultado = kelvin_para_fahrenheit(temperatura)
        
        if resultado is not None:
            print(f"\n{temperatura:.2f} {unidade_origem} é igual a {resultado:.2f} {unidade_destino}")
        else:
            print("Ocorreu um erro na conversão. Verifique as entradas.")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número para a temperatura.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Chama a função principal para iniciar o programa
converter_temperatura()