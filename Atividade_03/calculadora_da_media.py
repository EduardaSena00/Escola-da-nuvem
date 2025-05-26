# Leitura das quatro notas do aluno
# As notas são de ponto flutuante, com uma casa decimal.
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
n4 = float(input("Digite o quarto número: "))

# Cálculo da média ponderada
# Pesos: N1=2, N2=3, N3=4, N4=1
# A soma dos pesos é 2+3+4+1 = 10
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10

# Imprime a média inicial com uma casa decimal
print(f"Media: {media:.1f}")

# Verifica a situação do aluno com base na média inicial
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:  # Se a média estiver entre 5.0 e 6.9 (inclusive)
    print("Aluno em exame.")
    
    # Solicita a nota do exame
    nota_exame = float(input())
    
    # Imprime a nota do exame com uma casa decimal
    print(f"Nota do exame: {nota_exame:.1f}")
    
    # Recalcula a média final (média inicial + nota do exame) / 2
    media_final = (media + nota_exame) / 2
    
    # Verifica a situação final após o exame
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
        
    # Imprime a média final com uma casa decimal
    print(f"Media final: {media_final:.1f}")