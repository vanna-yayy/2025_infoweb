import streamlit as st
import pandas as pd
import time
from view import View


class ManterClienteUI:
    @staticmethod
    def main():
        st.header("Cadastro de Clientes")

        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with tab1:
            ManterClienteUI.listar()
        with tab2:
            ManterClienteUI.inserir()
        with tab3:
            ManterClienteUI.atualizar()
        with tab4:
            ManterClienteUI.excluir()

    @staticmethod
    def listar():
        clientes = View.cliente_listar()
        if not clientes:
            st.info("Nenhum cliente cadastrado")
            return

        df = pd.DataFrame([c.to_json() for c in clientes])
        st.dataframe(df)

    @staticmethod
    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Informe a senha", type="password")

        if st.button("Inserir"):
            View.cliente_inserir(nome, email, fone, senha)
            st.success("Cliente inserido com sucesso")
            time.sleep(1)
            st.rerun()

    @staticmethod
    def atualizar():
        clientes = View.cliente_listar()
        if not clientes:
            st.info("Nenhum cliente cadastrado")
            return

        op = st.selectbox("Selecione um cliente", clientes, format_func=lambda c: c.get_nome())
        nome = st.text_input("Novo nome", op.get_nome())
        email = st.text_input("Novo e-mail", op.get_email())
        fone = st.text_input("Novo fone", op.get_fone())
        senha = st.text_input("Nova senha", op.get_senha(), type="password")

        if st.button("Atualizar"):
            View.cliente_atualizar(op.get_id(), nome, email, fone, senha)
            st.success("Cliente atualizado com sucesso")

    @staticmethod
    def excluir():
        clientes = View.cliente_listar()
        if not clientes:
            st.info("Nenhum cliente cadastrado")
            return

        op = st.selectbox("Selecione um cliente para excluir", clientes, format_func=lambda c: c.get_nome())

        if st.button("Excluir"):
            View.cliente_excluir(op.get_id())
            st.success("Cliente excluído com sucesso")
            time.sleep(1)
            st.rerun()