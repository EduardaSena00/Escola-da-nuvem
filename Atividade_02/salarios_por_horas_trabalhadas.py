numero_funcionario = int(input("Digite o número de funcionarios:"))
horas_trabalhadas = int(input("Digite o número de horas trabalhadas:"))
valor_por_hora = float(input("Digite o valor por hora:"))

# Cálculo do salário
salario = horas_trabalhadas * valor_por_hora

# Exibição dos resultados formatados
print(f"Número de funcionarios = {numero_funcionario}")
print(f"Salário = R$ {salario:.2f}")