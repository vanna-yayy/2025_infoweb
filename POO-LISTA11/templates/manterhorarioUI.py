import streamlit as st
from datetime import datetime
import time
import pandas as pd
from view import View

class ManterHorarioUI:
    @staticmethod
    def main():
        st.header("Cadastro de Horários")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterHorarioUI.listar()
        with tab2:
            ManterHorarioUI.inserir()
        with tab3:
            ManterHorarioUI.atualizar()
        with tab4:
            ManterHorarioUI.excluir()


    @staticmethod
    def listar():
        horarios = View.horario_listar()
        if not horarios:
            st.info("Nenhum horário cadastrado")
            return

        clientes = {c.get_id(): c.get_nome() for c in View.cliente_listar()}
        servicos = {s.get_id(): s.get_descricao() for s in View.servico_listar()}
        profissionais = {p.get_id(): p.get_nome() for p in View.profissional_listar()}

        # Monta tabela de dados
        dados = []
        for h in horarios:
            dados.append({
                "ID": h.get_id(),
                "Data e Hora": h.get_data().strftime("%d/%m/%Y %H:%M"),
                "Confirmado": "Sim" if h.get_confirmado() else "Não",
                "Cliente": clientes.get(h.get_id_cliente(), "N/A"),
                "Serviço": servicos.get(h.get_id_servico(), "N/A"),
                "Profissional": profissionais.get(h.get_id_profissional(), "N/A")
            })

        df = pd.DataFrame(dados)
        st.dataframe(df, use_container_width=True)

    @staticmethod
    def inserir():
        clientes = View.cliente_listar()
        servicos = View.servico_listar()
        profissionais = View.profissional_listar()

        if not clientes or not servicos or not profissionais:
            st.warning("É necessário ter pelo menos um cliente, um serviço e um profissional cadastrados")
            return

        st.subheader("Novo Horário")

        data = st.text_input(
            "Data e hora (dd/mm/yyyy HH:MM)",
            datetime.now().strftime("%d/%m/%Y %H:%M"),
            key="data_inserir"
        )
        confirmado = st.checkbox("Confirmado", key="confirmado_inserir")
        cliente = st.selectbox("Cliente", clientes, format_func=lambda c: c.get_nome(), key="cliente_inserir")
        servico = st.selectbox("Serviço", servicos, format_func=lambda s: s.get_descricao(), key="servico_inserir")
        profissional = st.selectbox("Profissional", profissionais, format_func=lambda p: p.get_nome(), key="profissional_inserir")

        if st.button("Inserir", key="btn_inserir"):
            try:
                data_fmt = datetime.strptime(data, "%d/%m/%Y %H:%M")
                if cliente and servico and profissional:
                    View.horario_inserir(data_fmt, confirmado, cliente.get_id(), servico.get_id(), profissional.get_id())
                    st.success("Horário inserido com sucesso")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("Selecione cliente, serviço e profissional")
            except ValueError:
                st.error("Data inválida. Use o formato dd/mm/yyyy HH:MM")

    @staticmethod
    def atualizar():
        horarios = View.horario_listar()
        if not horarios:
            st.info("Nenhum horário cadastrado")
            return

        clientes = View.cliente_listar()
        servicos = View.servico_listar()
        profissionais = View.profissional_listar()

        st.subheader("Atualizar Horário")

        op = st.selectbox(
            "Selecione um horário",
            horarios,
            format_func=lambda h: f"{h.get_id()} - {h.get_data().strftime('%d/%m/%Y %H:%M')}",
            key="select_horario_atualizar"
        )

        data = st.text_input(
            "Nova data e hora (dd/mm/yyyy HH:MM)",
            op.get_data().strftime("%d/%m/%Y %H:%M"),
            key=f"data_{op.get_id()}"
        )
        confirmado = st.checkbox(
            "Confirmado",
            value=op.get_confirmado(),
            key=f"confirmado_{op.get_id()}"
        )
        cliente = st.selectbox(
            "Cliente",
            clientes,
            index=next((i for i, c in enumerate(clientes) if c.get_id() == op.get_id_cliente()), 0),
            format_func=lambda c: c.get_nome(),
            key=f"cliente_{op.get_id()}"
        )
        servico = st.selectbox(
            "Serviço",
            servicos,
            index=next((i for i, s in enumerate(servicos) if s.get_id() == op.get_id_servico()), 0),
            format_func=lambda s: s.get_descricao(),
            key=f"servico_{op.get_id()}"
        )
        profissional = st.selectbox(
            "Profissional",
            profissionais,
            index=next((i for i, p in enumerate(profissionais) if p.get_id() == op.get_id_profissional()), 0),
            format_func=lambda p: p.get_nome(),
            key=f"profissional_{op.get_id()}"
        )

        if st.button("Atualizar", key=f"btn_atualizar_{op.get_id()}"):
            try:
                data_fmt = datetime.strptime(data, "%d/%m/%Y %H:%M")
                View.horario_atualizar(
                    op.get_id(),
                    data_fmt,
                    confirmado,
                    cliente.get_id(),
                    servico.get_id(),
                    profissional.get_id()
                )
                st.success("Horário atualizado com sucesso")
                time.sleep(1)
                st.rerun()
            except ValueError:
                st.error("Data inválida. Use o formato dd/mm/yyyy HH:MM")

    @staticmethod
    def excluir():
        horarios = View.horario_listar()
        if not horarios:
            st.info("Nenhum horário cadastrado")
            return

        st.subheader("Excluir Horário")

        op = st.selectbox(
            "Selecione um horário para excluir",
            horarios,
            format_func=lambda h: f"{h.get_id()} - {h.get_data().strftime('%d/%m/%Y %H:%M')}",
            key="select_excluir"
        )

        if st.button("Excluir", key=f"btn_excluir_{op.get_id()}"):
            View.horario_excluir(op.get_id())
            st.success("Horário excluído com sucesso")
            time.sleep(1)
            st.rerun()