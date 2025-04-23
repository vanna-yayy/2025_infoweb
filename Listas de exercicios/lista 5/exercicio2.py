def maior(x, y,z):
    if x > y and x > z:
        return x
    elif z > y and z > x:
        return z
    else:
        return y

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))


resultado = maior(num1, num2, num3)
print(f"O maior valor entre {num1}, {num2} e {num3} é: {resultado}")