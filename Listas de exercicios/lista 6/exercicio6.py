print("Digite três valores inteiros")
valores = []
for _ in range(3):
    valor = int(input())
    valores.append(valor)

menor = min(valores)
maior = max(valores)


soma = menor + maior

print(f"A soma do maior com o menor número é {soma}.")
