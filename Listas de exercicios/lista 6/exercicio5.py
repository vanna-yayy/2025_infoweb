
meses = {
    1: "janeiro",
    2: "fevereiro",
    3: "março",
    4: "abril",
    5: "maio",
    6: "junho",
    7: "julho",
    8: "agosto",
    9: "setembro",
    10: "outubro",
    11: "novembro",
    12: "dezembro"
}

def obter_trimestre(mes):
    if 1 <= mes <= 3:
        return "primeiro"
    elif 4 <= mes <= 6:
        return "segundo"
    elif 7 <= mes <= 9:
        return "terceiro"
    elif 10 <= mes <= 12:
        return "quarto"
    else:
        return None


print("Informe o número do mês")
numero_mes = int(input())


if 1 <= numero_mes <= 12:
    nome_mes = meses[numero_mes]
    trimestre = obter_trimestre(numero_mes)
    print(f"O mês de {nome_mes} é do {trimestre} trimestre do ano")
else:
    print("Número de mês inválido. Digite um valor entre 1 e 12.")
