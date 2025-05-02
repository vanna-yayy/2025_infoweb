from datetime import datetime


def validar_data(data):
    try:
       
        data_obj = datetime.strptime(data, "%d/%m/%Y")
        
        if 1900 <= data_obj.year <= 2100:
            return "A data informada é válida"
        else:
            return "A data informada não é válida"
    
    except ValueError:
      
        return "A data informada não é válida"

print("Digite uma data no formato dd/mm/aaaa")
data = input()


resultado = validar_data(data)
print(resultado)
