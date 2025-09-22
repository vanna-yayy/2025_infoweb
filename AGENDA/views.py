from models.cliente import Cliente, ClienteDAO
from models.servico import Servico, servicoDAO

class View:
    @staticmethod
    def cliente_listar():
        return ClienteDAO.listar()

    @staticmethod
    def cliente_inserir(nome, email, fone):
        cliente = Cliente(0, nome, email, fone)
        ClienteDAO.inserir(cliente)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        cliente = Cliente(id, nome, email, fone)
        ClienteDAO.atualizar(cliente)

    @staticmethod
    def cliente_excluir(id):
        cliente = Cliente(id, "", "", "")
        ClienteDAO.excluir(cliente)

    @staticmethod
    def servico_listar():
        return servicoDAO.listar()

    @staticmethod
    def servico_inserir(descricao,valor):
        servico = Servico(0, descricao,valor)
        servicoDAO.inserir(servico)

    @staticmethod
    def servico_atualizar(id, descricao,valor):
        servico = Servico(id, descricao,valor)
        servicoDAO.atualizar(servico)

    @staticmethod
    def servico_excluir(id):
        servico= Servico(id, "", 0)
        servicoDAO.excluir(servico)