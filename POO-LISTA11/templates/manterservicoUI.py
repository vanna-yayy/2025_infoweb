import streamlit as st
import pandas as pd
import time
from view import View

class ManterServicoUI:
    @staticmethod
    def main():
        st.header("Cadastro de Serviços")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterServicoUI.listar()
        with tab2:
            ManterServicoUI.inserir()
        with tab3:
            ManterServicoUI.atualizar()
        with tab4:
            ManterServicoUI.excluir()

    @staticmethod
    def listar():
        servicos = View.servico_listar()
        if not servicos:
            st.info("Nenhum serviço cadastrado")
            return
        df = pd.DataFrame([s.to_json() for s in servicos])
        st.dataframe(df)

    @staticmethod
    def inserir():
        descricao = st.text_input("Informe a descrição")
        valor = st.text_input("Informe o valor (ex: 99,99)")

        if st.button("Inserir"):
            try:
                valor_float = float(valor.replace(",", "."))
                View.servico_inserir(descricao, valor_float)
                st.success("Serviço inserido com sucesso")
                time.sleep(1)
                st.rerun()
            except ValueError:
                st.error("Valor inválido")

    @staticmethod
    def atualizar():
        servicos = View.servico_listar()
        if not servicos:
            st.info("Nenhum serviço cadastrado")
            return

        op = st.selectbox("Selecione um serviço", servicos, format_func=lambda s: s.get_descricao())
        descricao = st.text_input("Nova descrição", op.get_descricao())
        valor = st.text_input("Novo valor", str(op.get_valor()).replace(".", ","))

        if st.button("Atualizar"):
            try:
                valor_float = float(valor.replace(",", "."))
                View.servico_atualizar(op.get_id(), descricao, valor_float)
                st.success("Serviço atualizado com sucesso")
            except ValueError:
                st.error("Valor inválido")

    @staticmethod
    def excluir():
        servicos = View.servico_listar()
        if not servicos:
            st.info("Nenhum serviço cadastrado")
            return

        op = st.selectbox("Selecione um serviço para excluir", servicos, format_func=lambda s: s.get_descricao())
        if st.button("Excluir"):
            View.servico_excluir(op.get_id())
            st.success("Serviço excluído com sucesso")
            time.sleep(1)
            st.rerun()