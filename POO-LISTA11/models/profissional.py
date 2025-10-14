import json

class Profissional:
    def __init__(self, id, nome, email,  especialidade,conselho,senha):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__especialidade = especialidade
        self.__conselho= conselho
        self.__senha = senha

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_especialidade(self): return self.__especialidade
    def get_conselho(self): return self.__conselho
    def get_senha(self): return self.__senha

    def set_id(self, id): self.__id = id
    def set_nome(self, nome): self.__nome = nome
    def set_email(self, email): self.__email = email
    def set_fone(self, especialidade): self.__especialidade= especialidade
    def set_conselho(self,conselho): self.__conselho=conselho
    def set_senha(self, senha): self.__senha = senha

    def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "email": self.__email,
            "especialidade": self.__especialidade,
            "conselho": self.__conselho,
            "senha": self.__senha
        }

    @staticmethod
    def from_json(dic):
        return Profissional(dic.get("id", 0), dic.get("nome", ""), dic.get("email", ""), dic.get("especialidade", ""),dic.get("conselho", ""), dic.get("senha", ""))

    def __str__(self):
        return f"{self.__id} - {self.__nome}"


class ProfissionalDAO:
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
            with open("profissional.json", mode="r", encoding="utf-8") as arquivo:
                lista = json.load(arquivo)
                for dic in lista:
                    cls.objetos.append(Profissional.from_json(dic))
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("profissional.json", mode="w", encoding="utf-8") as arquivo:
            json.dump(
                [p.to_json() for p in cls.objetos],
                arquivo,
                ensure_ascii=False,
                indent=4
            )