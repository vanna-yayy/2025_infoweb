import streamlit as st
import pandas as pd
import time
from view import View


class ManterProfissionalUI:
    @staticmethod
    def main():
        st.header("Cadastro de Profissionais")

        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with tab1:
            ManterProfissionalUI.listar()
        with tab2:
            ManterProfissionalUI.inserir()
        with tab3:
            ManterProfissionalUI.atualizar()
        with tab4:
            ManterProfissionalUI.excluir()

    @staticmethod
    def listar():
        profissionais = View.profissional_listar()
        if not profissionais:
            st.info("Nenhum profissional cadastrado")
            return

        df = pd.DataFrame([p.to_json() for p in profissionais])
        st.dataframe(df)

    @staticmethod
    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        especialidade = st.text_input("Informe a especialidade")
        conselho = st.text_input("Informe a conselho")
        senha = st.text_input("Informe a senha", type="password")

        if st.button("Inserir"):
            View.profissional_inserir(nome, email, especialidade,conselho,senha)
            st.success("Profissional inserido com sucesso")
            time.sleep(1)
            st.rerun()

    @staticmethod
    def atualizar():
        profissionais = View.profissional_listar()
        if not profissionais:
            st.info("Nenhum profissional cadastrado")
            return

        op = st.selectbox("Selecione um profissional", profissionais, format_func=lambda p: p.get_nome())
        nome = st.text_input("Novo nome", op.get_nome())
        email = st.text_input("Novo e-mail", op.get_email())
        especialidade = st.text_input("Nova especialidade", op.get_especialidade())
        conselho = st.text_input("Novo conselho", op.get_conselho())
        senha = st.text_input("Nova senha", op.get_senha(), type="password")

        if st.button("Atualizar"):
            View.profissional_atualizar(op.get_id(), nome, email, especialidade,conselho, senha)
            st.success("Profissional atualizado com sucesso")

    @staticmethod
    def excluir():
        profissionais = View.profissional_listar()
        if not profissionais:
            st.info("Nenhum profissional cadastrado")
            return

        op = st.selectbox(
            "Selecione um profissional para excluir",
            profissionais,
            format_func=lambda p: p.get_nome()
        )

        if st.button("Excluir"):
            View.profissional_excluir(op.get_id())
            st.success("Profissional excluído com sucesso")
            time.sleep(1)
            st.rerun()