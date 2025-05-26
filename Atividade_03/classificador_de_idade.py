idade = int(input("Digite sua idade: "))

if 0 <= idade <= 12:
    print("Classificação: Criança")
elif 13 <= idade <= 17:
    print("Classificação: Adolescente")
elif 18 <= idade <= 59:
    print("Classificação: Adulto")
else: idade >= 60
print("Classificação: Idoso")