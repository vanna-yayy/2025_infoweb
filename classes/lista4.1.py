
class Viagem: 
    def __init__(self):
        self.__destino = ""
        self.__distancia = 0
        self.__litros = 0
    def set_destino(self, valor):
        if valor.strip() == "" or valor == None:raise ValueError()
        else: self.__destino = valor
    def set_distancia(self,valor):
        if valor >= 0: self.__distancia = valor
        else: raise ValueError()
    def set_litros(self, valor):
        if valor >= 0: self.__litros = valor
        else: raise ValueError()

    def get_destino(self):
        return self.__destino
    def get_distancia(self):
        return self.__distancia
    def get_litros(self):
        return self.__litros
    
    def calc_consumo(self):
        return self.__distancia/self.__litros
    
class UI:
    @staticmethod
    def main():
        opcao = UI.menu()
        x= Viagem ()
        x.set_destino = input("coloque seu destino:")
        x.set_distancia = input("coloque s")

        match opcao:
            case 1:
              
            case 2:
                print ("tchau")
    
    @staticmethod
    def menu() -> int:
        while True:
            print("1 - Calcular\n2 - Fim")
            opcao = int(input("Escolha uma das opções acima: "))

            if 1 <= opcao <= 2: return opcao

            print("Opcao Inválida")


UI.main()