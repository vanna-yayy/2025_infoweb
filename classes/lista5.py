from datetime import datetime, date

class Paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__nascimento = datetime.strptime(nascimento, "%d/%m/%Y").date()

    def set_nome(self, nome):
        if nome == "": raise ValueError
        self.__nome = nome
    def set_cpf(self, cpf):
        if cpf > 0 : raise ValueError
    def set_telefone(self, telefone):
        if telefone > 0: raise ValueError
    def set_nascimento(self, nascimento):
        self.__nascimento = datetime.strptime(nascimento, "%d/%m/%Y").date()


    def get_nome(self):
        return self.__nome
    def get_cpf(self): 
        return self.__cpf
    def get_telefone(self): 
        return self.__telefone
    def get_nascimento(self):
        return self.__nascimento


    def idade(self):
        hoje = date.today()
        anos = hoje.year - self.__nascimento.year
        meses = hoje.month - self.__nascimento.month
        if hoje.day < self.__nascimento.day:
            meses -= 1
        if meses < 0:
            anos -= 1
            meses += 12
        return f"{anos} anos e {meses} meses"

    def __str__(self):
        return f"Nome: {self.__nome}\nCPF: {self.__cpf}\nTelefone: {self.__telefone}\nNascimento: {self.__nascimento.strftime('%d/%m/%Y')}\nIdade: {self.idade()}"
    

