import json
from datetime import datetime

class Horario:
    def __init__(self, id, data):
        self.__id = id
        self.__data = data
        self.__confirmado = False
        self.__id_cliente = 0
        self.__id_servico = 0
        self.__id_profissional = 0

    def __str__(self):
        return f"{self.__id} - {self.__data.strftime('%d/%m/%Y %H:%M')} - {'Sim' if self.__confirmado else 'Não'}"

    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_confirmado(self): return self.__confirmado
    def get_id_cliente(self): return self.__id_cliente
    def get_id_servico(self): return self.__id_servico
    def get_id_profissional(self): return self.__id_profissional

    def set_id(self, id): self.__id = id
    def set_data(self, data): self.__data = data
    def set_confirmado(self, confirmado): self.__confirmado = confirmado
    def set_id_cliente(self, id_cliente): self.__id_cliente = id_cliente
    def set_id_servico(self, id_servico): self.__id_servico = id_servico
    def set_id_profissional(self, id_profissional): self.__id_profissional = id_profissional

    def to_json(self):
        return {
            "id": self.__id,
            "data": self.__data.strftime("%d/%m/%Y %H:%M"),
            "confirmado": self.__confirmado,
            "id_cliente": self.__id_cliente,
            "id_servico": self.__id_servico,
            "id_profissional": self.__id_profissional
        }

    @staticmethod
    def from_json(dic):
        data = datetime.strptime(dic["data"], "%d/%m/%Y %H:%M")
        h = Horario(dic.get("id", 0), data)
        h.set_confirmado(dic.get("confirmado", False))
        h.set_id_cliente(dic.get("id_cliente", 0))
        h.set_id_servico(dic.get("id_servico", 0))
        h.set_id_profissional(dic.get("id_profissional", 0))
        return h

class HorarioDAO:
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        _id = max([h.get_id() for h in cls.objetos], default=0)
        obj.set_id(_id + 1)
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        for h in cls.objetos:
            if h.get_id() == obj.get_id():
                cls.objetos.remove(h)
                cls.objetos.append(obj)
                cls.salvar()
                return

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        for h in cls.objetos:
            if h.get_id() == obj.get_id():
                cls.objetos.remove(h)
                cls.salvar()
                return

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("horarios.json", mode="r", encoding="utf-8") as arquivo:
                lista = json.load(arquivo)
                for dic in lista:
                    cls.objetos.append(Horario.from_json(dic))
        except FileNotFoundError:
            with open("horarios.json", mode="w", encoding="utf-8") as arquivo:
                json.dump([], arquivo)

    @classmethod
    def salvar(cls):
        with open("horarios.json", mode="w", encoding="utf-8") as arquivo:
            json.dump([h.to_json() for h in cls.objetos], arquivo, ensure_ascii=False, indent=4)