
print("Digite quatro valores inteiros")
soma_pares = 0
soma_impares = 0

for _ in range(4):
    valor = int(input())
    if valor % 2 == 0:
        soma_pares += valor
    else:
        soma_impares += valor

print("Soma dos pares =", soma_pares)
print("Soma dos ímpares =", soma_impares)
