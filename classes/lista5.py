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
    
class UI:
    def __init__(self):
        self.pacientes = []

    def exibir_menu(self):
        print("\n--- Menu ---")
        print("1. Cadastrar paciente")
        print("2. Listar pacientes")
        print("3. Sair")

    def cadastrar_paciente(self):
        try:
            nome = input("Nome: ").strip()
            cpf = input("CPF: ").strip()
            telefone = input("Telefone: ").strip()
            nascimento = input("Data de nascimento (DD/MM/AAAA): ").strip()
            nascimento_date = datetime.strptime(nascimento, "%d/%m/%Y").date()
            
            paciente = Paciente(nome, cpf, telefone, nascimento_date)
            self.pacientes.append(paciente)
            print("\nPaciente cadastrado com sucesso!")

        except ValueError as e:
            print(f"Erro: {e}")

    def listar_pacientes(self):
        if not self.pacientes:
            print("Nenhum paciente cadastrado.")
        else:
            print("\n--- Lista de Pacientes ---")
            for i, paciente in enumerate(self.pacientes, start=1):
                print(f"\nPaciente {i}:")
                print(paciente)

    def main(self):
        while True:
            self.exibir_menu()
            opcao = input("Escolha uma opção: ").strip()

            if opcao == '1':
                self.cadastrar_paciente()
            elif opcao == '2':
                self.listar_pacientes()
            elif opcao == '3':
                print("Saindo do programa.")
                break
            else:
                print("Opção inválida. Tente novamente.")
                
if __name__ == "__main__":
    ui = UI()
    ui.main()
