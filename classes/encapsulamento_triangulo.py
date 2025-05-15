class Triangulo:
    def __init__(self):
        self.__b = 0  
        self.__h = 0  

    @property
    def set(self):
        return self.__b

    @set.setter
    def set(self, b):
        if b < 0:
            raise ValueError("Valor inválido para a base")
        self.__b = b

    @property
    def get(self):
        return self.__h

    @get.setter
    def get(self, h):
        if h < 0:
            raise ValueError("Valor inválido para a altura")
        self.__h = h

    def calcular_area(self):
        return (self.__b * self.__h) / 2

    @staticmethod
    def executar():
        x = Triangulo()
        try:
            x.base = int(input("Informe o valor da base: "))
            x.altura = int(input("Informe o valor da altura: "))
            print(f"A área do triângulo é {x.calcular_area()}")
        except ValueError as e:
            print(f"Erro: {e}")
