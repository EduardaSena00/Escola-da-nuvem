import random
import string

def gerar_senha_aleatoria(tamanho: int) -> str:
    """
    Gera uma senha aleatória com base no tamanho especificado,
    incluindo letras (maiúsculas e minúsculas), números e caracteres especiais.

    Parâmetros:
        tamanho (int): O comprimento desejado para a senha.

    Retorna:
        str: A senha aleatória gerada.

    Levanta:
        ValueError: Se o tamanho da senha for menor que 4.
    """
    if tamanho < 4:
        raise ValueError("O tamanho da senha deve ser de no mínimo 4 caracteres.")

    # Define os conjuntos de caracteres disponíveis
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits # '0123456789'
    caracteres_especiais = string.punctuation # '!@#$%^&*().,..' etc.

    # Combina todos os tipos de caracteres
    todos_caracteres = letras_maiusculas + letras_minusculas + numeros + caracteres_especiais

    # Garante que a senha tenha pelo menos um de cada tipo de caractere
    # Isso melhora a força da senha, garantindo variedade.
    senha = [
        random.choice(letras_maiusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(caracteres_especiais)
    ]

    # Preenche o restante da senha com caracteres aleatórios dos conjuntos combinados
    for _ in range(tamanho - 4): # -4 porque já adicionamos 4 caracteres iniciais
        senha.append(random.choice(todos_caracteres))

    # Embaralha a lista de caracteres para garantir que a ordem seja aleatória
    # (senão, os primeiros 4 caracteres seriam sempre um de cada tipo)
    random.shuffle(senha)

    # Converte a lista de caracteres em uma string e a retorna
    return "".join(senha)

if __name__ == "__main__":
    print("--- Gerador de Senhas Aleatórias Seguras ---")
    print("Sua senha incluirá letras maiúsculas, minúsculas, números e caracteres especiais.")

    while True:
        try:
            entrada_tamanho = input("\nDigite o comprimento desejado para a senha (mínimo 4, ou 'fim' para sair): ").strip()

            if entrada_tamanho.lower() == 'fim':
                break

            tamanho_senha = int(entrada_tamanho)

            # Chama a função para gerar a senha
            senha_gerada = gerar_senha_aleatoria(tamanho_senha)

            print(f"Sua nova senha aleatória: **{senha_gerada}**")
            print("-" * 40)

        except ValueError as e:
            # Captura erros de validação da função e de conversão para int
            print(f"Erro: {e}. Por favor, digite um número válido.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}. Por favor, tente novamente.")

    print("\nObrigado por usar o gerador de senhas!")
