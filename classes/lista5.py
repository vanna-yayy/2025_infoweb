from datetime import datetime, date

class Paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__nascimento = nascimento

    def set_nome(self, nome):
        if nome == "": raise ValueError
        self.__nome = nome

    def set_cpf(self, cpf):
        if not cpf or not isinstance(cpf, str):
            raise ValueError("CPF inválido.")
        self.__cpf = cpf

    def set_telefone(self, telefone):
        if not telefone or not isinstance(telefone, str):
            raise ValueError("Telefone inválido.")
        self.__telefone = telefone

    def set_nascimento(self, nascimento):
        try:
            self.__nascimento = datetime.strptime(nascimento, "%d/%m/%Y").date() 
        except ValueError:
            raise ValueError("Data de nascimento inválida. Use o formato DD/MM/AAAA.")


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
    

class UI():
     def main
        
