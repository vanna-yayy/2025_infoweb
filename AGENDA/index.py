from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
import streamlit as st

class IndexUI:

    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()

    def sidebar():
        IndexUI.menu_admin()

    def main():
        IndexUI.sidebar()

IndexUI.main()