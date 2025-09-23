from models.horarios import Horario, HorarioDAO
class View:
    def horario_inserir(data, confirmado, id_cliente, id_servico):
      c = Horario(0, data)
      c.set_confirmado(confirmado)
      c.set_id_cliente(id_cliente)
      c.set_id_servico(id_servico)
      HorarioDAO.inserir(c)

def horario_listar():
    return HorarioDAO.listar()

def horario_atualizar(id, data, confirmado, id_cliente, id_servico):
    c= Horario(id, data)
    c.set_confirmado(confirmado)
    c.set_id_cliente(id_cliente)
    c.set_id_servico(id_servico)
    HorarioDAO.atualizar(c)

def horario_excluir(id):
    c= Horario(id, None)
    HorarioDAO.excluir(c)