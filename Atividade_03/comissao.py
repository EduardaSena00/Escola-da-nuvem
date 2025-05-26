nome_vendedor = input("Digite o nome do vereador: ")
salario_fixo = (input("Salário fixo: "))
total_vendas = (input("Total de vendas:"))

# Cálculo da comissão (15% sobre o total de vendas)
comissao = total_vendas * 0.15

# Cálculo do salário total a receber
salario_total = salario_fixo + comissao

# Impressão do resultado formatado com duas casas decimais
print(f"Comissão: = R$ {comissao:.2f}")
print(f"Valor total: = R$ {salario_total}")