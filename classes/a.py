class Triangulo:
    def __init__(self):
        self.__b = 0
        self.__h = 0
    
    def set_base(self, valor):
        self.__b = valor
    def set_altura(self, valor):
        self.__h = valor
    
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h

    def calc_area(self):
        return self.__b * self.__h / 2 

class UI:
    @staticmethod
    def menu():
        op = int(input("1-Água, 2-Triângulo, 9-Fim: "))
        return op
    
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.contaagua()
            if op == 2: UI.triangulo()

    @staticmethod
    def contaagua():    
        x = Agua()
        #print(f"Conta de água do mês {x.mes} do ano {x.ano}. Foi consumido é {x.consumo}")
        print(f"Conta de água do mês {x.get_mes()} do ano {x.get_ano()}. Foi consumido é {x.get_consumo()}")
        #x.mes = int(input("Informe o mês da conta: "))
        x.set_mes(int(input("Informe o mês da conta: ")))
        #x.ano = int(input("informe o ano: "))
        x.set_ano(int(input("informe o ano: ")))
        #x.consumo = int(input("informe o consumo em m3: "))
        x.set_consumo(int(input("informe o consumo em m3: ")))
        #print(f"O valor da conta de água do mês {x.mes} do ano {x.ano} é {x.valor()}")
        print(f"O valor da conta de água do mês {x.get_mes()} do ano {x.get_ano()} é {x.valor()}")
 
    @staticmethod
    def triangulo():
        x = Triangulo()
        x.set_base(int(input("Informe o valor da base: ")))
        x.set_altura(int(input("Informe o valor da altura: ")))
        print(f"A área do triângulo é {x.calc_area()}"