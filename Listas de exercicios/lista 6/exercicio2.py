print("Digite quatro valores inteiros")
valores = []
for _ in range(4):
    valor = int(input())
    valores.append(valor)


media = sum(valores) // 4 
print("Média =", media)


menores = []
maiores_ou_iguais = []

for valor in valores:
    if valor < media:
        menores.append(valor)
    else:
        maiores_ou_iguais.append(valor)


print("Números menores que a média")
for num in menores:
    print(num)
    
print("Números maiores ou iguais à média")
for num in maiores_ou_iguais:
    print(num)
