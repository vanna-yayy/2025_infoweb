def somar_horarios(h1, h2):
    h1_horas, h1_minutos = map(int, h1.split(':'))
    h2_horas, h2_minutos = map(int, h2.split(':'))

    total_minutos = h1_minutos + h2_minutos
    total_horas = h1_horas + h2_horas

    if total_minutos >= 60:
        total_minutos -= 60
        total_horas += 1

    return f"{total_horas:02d}:{total_minutos:02d}"


print("Digite o primeiro horário no formato hh:mm")
horario1 = input()

print("Digite o segundo horário no formato hh:mm")
horario2 = input()

resultado = somar_horarios(horario1, horario2)
print("Total de horas =", resultado)
