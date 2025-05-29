def verificar_senha_forte():
    """
    Verifica se uma senha é forte de acordo com os seguintes critérios:
    - Pelo menos 8 caracteres
    - Contém pelo menos um número
    O programa continua pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.
    """
    while True:
        senha = input("Digite sua senha (ou 'sair' para encerrar): ")

        if senha.lower() == 'sair':
            print("Programa encerrado.") # Corrigi a vírgula para ponto final para consistência
            break

        if len(senha) < 8:
            print("Senha muito curta. Ela deve ter pelo menos 8 caracteres.") # Corrigi a vírgula para ponto final
            continue

        tem_numero = False
        for char in senha:
            if char.isdigit():
                tem_numero = True
                break

        if not tem_numero:
            # Esta é a parte que estava com a lógica invertida no seu código.
            # Se não tem número, a senha NÃO é forte.
            print("A senha deve conter pelo menos um número.")
            continue # Continua pedindo a senha

        # Se chegou aqui, a senha passou por todas as verificações
        print("Senha forte! Registrada com sucesso.")
        break # Sai do loop porque uma senha válida foi inserida

# Esta parte DEVE ESTAR FORA da função e sem indentação.
if __name__ == "__main__":
    verificar_senha_forte()