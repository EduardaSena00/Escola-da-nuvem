valor_em_reais = 100
taxa_do_dolar = 5
taxa_do_euro = 6.15

valor_do_dolar = valor_em_reais / taxa_do_dolar

valor_do_euro = valor_em_reais / taxa_do_euro

print(f"Valor em Reais: R$ {valor_em_reais:.2f}")
print(f"Taxa em Dólar: R$ {taxa_do_dolar:.2f}")
print(f"Taxa em Euro: R$ {taxa_do_euro:.2f}")
print(f"Valor em Dólares: US$ {valor_do_dolar:.2f}")
print(f"Valor em Euros: € {valor_do_euro:.2f}")
