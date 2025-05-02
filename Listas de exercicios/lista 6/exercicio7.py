import math


print("Digite os coeficientes a, b, e c de uma equação do II grau")
a = float(input())
b = float(input())
c = float(input())


if a == 0:
    print("Impossível calcular: coeficiente 'a' não pode ser zero.")
else:
    delta = b**2 - 4*a*c

    if delta < 0:
        print("Impossível calcular")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)

        if raiz1 == raiz2:
            print(f"A única raiz real é {raiz1}")
        else:
            print(f"As raízes são {raiz1:.0f} e {raiz2:.0f}")
