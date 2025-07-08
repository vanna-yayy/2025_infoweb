from enum import Enum

class Pagamento(Enum):
    EM_ABERTO = "Em Aberto"
    PAGO_PARCIAL = "Pago Parcial"
    PAGO = "Pago"

class Boleto:
    def __init__(self, codigo_barras, data_emissao, data_vencimento, valor):
        self.__codigo_barras = codigo_barras
        self.__data_emissao = datetime.strptime(data_emissao, "%d/%m/%Y").date()
        self.__data_vencimento = datetime.strptime(data_vencimento, "%d/%m/%Y").date()
        self.__valor = valor
        self.__valor_pago = 0.0

    def pagar(self, valor):
        self.__valor_pago += valor

    def situacao(self):
        if self.__valor_pago == 0:
            return Pagamento.EM_ABERTO.value
        elif self.__valor_pago < self.__valor:
            return Pagamento.PAGO_PARCIAL.value
        else:
            return Pagamento.PAGO.value

    def __str__(self):
        return (f"Código: {self.__codigo_barras}\n"
                f"Emissão: {self.__data_emissao.strftime('%d/%m/%Y')}\n"
                f"Vencimento: {self.__data_vencimento.strftime('%d/%m/%Y')}\n"
                f"Valor: R${self.__valor:.2f}\n"
                f"Pago: R${self.__valor_pago:.2f}\n"
                f"Situação: {self.situacao()}")
