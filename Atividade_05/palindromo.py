import re # Importa o módulo de expressões regulares para limpar o texto

def verificar_palindromo(texto: str) -> str:
    """
    Verifica se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente,
    ignorando espaços, pontuação e acentuação).

    Parâmetros:
        texto (str): A palavra ou frase a ser verificada.

    Retorna:
        str: "Sim" se for um palíndromo, "Não" caso contrário.
    """
    # 1. Normalizar o texto:
    # Converter para minúsculas
    texto_normalizado = texto.lower()

    # Remover acentuação (opcional, mas melhora a verificação de palíndromos com acentos)
    # Mapeia caracteres acentuados para suas versões não acentuadas
    substituicoes_acentos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
        'ã': 'a', 'õ': 'o',
        'â': 'a', 'ê': 'e', 'î': 'i', 'ô': 'o', 'û': 'u',
        'ç': 'c'
    }
    for acentuado, sem_acento in substituicoes_acentos.items():
        texto_normalizado = texto_normalizado.replace(acentuado, sem_acento)

    # Remover caracteres não alfanuméricos (espaços, pontuação, etc.)
    # [^a-z0-9] significa "qualquer coisa que NÃO seja uma letra de 'a' a 'z' ou um dígito de '0' a '9'"
    texto_limpo = re.sub(r'[^a-z0-9]', '', texto_normalizado)

    # 2. Verificar se é um palíndromo:
    # Compara a string limpa com ela mesma invertida
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

# --- Parte interativa do código ---
if __name__ == "__main__":
    print("--- Verificador de Palíndromos ---")
    print("Digite uma palavra ou frase para verificar se é um palíndromo.")
    print("Digite 'fim' para sair.")

    while True:
        entrada_usuario = input("\nDigite aqui: ").strip()

        if entrada_usuario.lower() == 'fim':
            break # Sai do loop se o usuário digitar 'fim'

        if not entrada_usuario: # Verifica se a entrada está vazia
            print("Por favor, digite algo para verificar.")
            continue

        resultado = verificar_palindromo(entrada_usuario)
        print(f"'{entrada_usuario}' é um palíndromo? **{resultado}**")

    print("\nObrigado por usar o verificador de palíndromos!")