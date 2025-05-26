# Informações do produto
nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

# Calcular o valor do desconto 
valor_desconto = (preco_original * porcentagem_desconto) / 100

# Calcular o preço final
preco_final = preco_original - valor_desconto

print(f"Produto: {nome_produto}")
print(f"Preço original: R${preco_original:.2f}")
print(f"Porcentagem de desconto: {porcentagem_desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
