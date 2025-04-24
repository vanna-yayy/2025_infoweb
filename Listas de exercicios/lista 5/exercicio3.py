def iniciais(nome):
    partes = nome.strip().split()
    resultado = " "
    for parte in partes:
        resultado += parte[0].upper()
    return resultado

nome_completo = input("Digite seu nome completo: ")
print("Suas iniciais são:", iniciais(nome_completo))
