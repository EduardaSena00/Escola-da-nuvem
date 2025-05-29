def calcular_media_turma():
    """
    Permite a um professor registrar as notas de uma turma, calcula e exibe a média.
    O programa solicita notas até que o professor digite 'fim'.
    Notas válidas são de 0 a 10. Notas inválidas são ignoradas.
    """
    notas = []
    while True:
        entrada = input("Digite a nota (ou 'fim' para encerrar): ").strip().lower()

        if entrada == 'fim':
            break

        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Por favor, digite uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número ou 'fim'.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"\nNotas registradas: {notas}")
        print(f"A média da turma é: {media:.2f}")
    else:
        print("Nenhuma nota válida foi inserida.")

if __name__ == "__main__":
    calcular_media_turma()
