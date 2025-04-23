def maior(x, y):
    if x > y:
        return x
    else:
        return y

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))


resultado = maior(num1, num2)
print(f"O maior valor entre {num1} e {num2} é: {resultado}")
