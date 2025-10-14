import json

class Servico:
    def __init__(self, id, descricao, valor):
        self.__id = id
        self.__descricao = descricao
        self.__valor = valor

    def get_id(self): return self.__id
    def get_descricao(self): return self.__descricao
    def get_valor(self): return self.__valor

    def set_id(self, id): self.__id = id
    def set_descricao(self, descricao): self.__descricao = descricao
    def set_valor(self, valor): self.__valor = valor

    def to_json(self):
        return {"id": self.__id, "descricao": self.__descricao, "valor": self.__valor}

    @staticmethod
    def from_json(dic):
        return Servico(dic.get("id", 0), dic.get("descricao", ""), dic.get("valor", 0))

    def __str__(self):
        return f"{self.__id} - {self.__descricao}"

class ServicoDAO:
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        _id = 0
        for aux in cls.objetos:
            if aux.get_id() > _id:
                _id = aux.get_id()
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
        aux = cls.listar_id(obj.get_id())
        if aux is not None:
            cls.objetos.remove(aux)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux is not None:
            cls.objetos.remove(aux)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("servico.json", mode="r", encoding="utf-8") as arquivo:
                lista = json.load(arquivo)
                for dic in lista:
                    cls.objetos.append(Servico.from_json(dic))
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("servico.json", mode="w", encoding="utf-8") as arquivo:
            json.dump([s.to_json() for s in cls.objetos], arquivo, ensure_ascii=False, indent=4)