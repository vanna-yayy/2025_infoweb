
def calcular_angulo(horas, minutos):
   
    if horas < 0 or horas > 12 or minutos < 0 or minutos >= 60:
        return "Hora Inválida"
    
 
    angulo_horas = 30 * horas + 0.5 * minutos

    angulo_minutos = 6 * minutos
    
    angulo = abs(angulo_horas - angulo_minutos)
    
    if angulo > 180:
        angulo = 360 - angulo
    
    return f"Menor ângulo entre os ponteiros = {angulo:.1f} graus"


print("Digite o horário no formato hh:mm")
horario = input()

try:
    horas, minutos = map(int, horario.split(":"))
    resultado = calcular_angulo(horas, minutos)
    print(resultado)
except ValueError:
    print("Hora Inválida")
