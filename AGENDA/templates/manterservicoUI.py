import streamlit as st
import pandas as pd
import time
from views import View


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
            st.info("Nenhum serviço cadastrado.")
            return

        dados = [s.to_json() for s in servicos]
        df = pd.DataFrame(dados)
        st.dataframe(df)

    @staticmethod
    def inserir():
        descricao = st.text_input("Informe a Descrição")
        valor = st.text_input("Informe o Valor (ex: 99,99)")

        if st.button("Inserir"):
            if not descricao or not valor:
                st.error("Por favor, preencha todos os campos.")
                return

            try:
                valor_float = float(valor.replace(",", "."))
                View.servico_inserir(descricao, valor_float)
                st.success("Serviço inserido com sucesso.")
                time.sleep(1.5)
                st.experimental_rerun()
            except ValueError:
                st.error("Valor inválido. Use um número no formato 99,99.")

    @staticmethod
    def atualizar():
        servicos = View.servico_listar()

        if not servicos:
            st.info("Nenhum serviço cadastrado.")
            return

        servico = st.selectbox(
            "Selecione o serviço para atualizar",
            servicos,
            format_func=lambda s: f"{s.get_id()} - {s.get_descricao()}"
        )

        nova_descricao = st.text_input("Nova descrição", servico.get_descricao())
        novo_valor = st.text_input("Novo valor", str(servico.get_valor()).replace(".", ","))

        if st.button("Atualizar"):
            if not nova_descricao or not novo_valor:
                st.error("Todos os campos devem ser preenchidos.")
                return

            try:
                valor_float = float(novo_valor.replace(",", "."))
                View.servico_atualizar(servico.get_id(), nova_descricao, valor_float)
                st.success("Serviço atualizado com sucesso.")
                time.sleep(1.5)
                st.experimental_rerun()
            except ValueError:
                st.error("Valor inválido. Use um número no formato 99,99.")

    @staticmethod
    def excluir():
        servicos = View.servico_listar()

        if not servicos:
            st.info("Nenhum serviço cadastrado.")
            return

        servico = st.selectbox(
            "Selecione o serviço para excluir",
            servicos,
            format_func=lambda s: f"{s.get_id()} - {s.get_descricao()}"
        )

        if st.button("Excluir"):
            View.servico_excluir(servico.get_id())
            st.success("Serviço excluído com sucesso.")
            time.sleep(1.5)
            st.experimental_rerun()