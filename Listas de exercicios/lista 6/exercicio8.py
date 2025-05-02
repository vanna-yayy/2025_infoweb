
print("Digite quatro valores inteiros")
valores = []

for _ in range(4):
    valor = int(input())
    valores.append(valor)


if len(set(valores)) != 4:
    print("Erro: os valores devem ser diferentes.")
else:

    valores_ordenados = sorted(valores)
    
    menor = valores_ordenados[0]
    segundo_menor = valores_ordenados[1]
    segundo_maior = valores_ordenados[2]
    maior = valores_ordenados[3]

    soma_segundos = segundo_maior + segundo_menor


    print(f"Maior valor = {maior}")
    print(f"Menor valor = {menor}")
    print(f"A soma do segundo maior valor com o segundo menor = {soma_segundos}")
