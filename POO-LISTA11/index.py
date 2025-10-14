import streamlit as st
from templates.manterclienteUI import ManterClienteUI
from templates.manterprofissionalUI import ManterProfissionalUI
from templates.manterservicoUI import ManterServicoUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.abrircontaUI import AbrirContaUI
from templates.loginUI import LoginUI
from templates.perfilclientesUI import PerfilclientesUI

st.set_page_config(layout="wide")

if "usuario_id" not in st.session_state:
    st.session_state["usuario_id"] = None
    st.session_state["usuario_nome"] = None
    st.session_state["usuario_tipo"] = None


def logout():
    st.session_state["usuario_id"] = None
    st.session_state["usuario_nome"] = None
    st.session_state["usuario_tipo"] = None
    st.rerun()


menu_visitante = ["Login", "Abrir Conta"]
menu_cliente = ["Perfil", "Agendar Horário", "Logout"]
menu_profissional = ["Perfil", "Gerenciar Horários", "Logout"]
menu_admin = ["Clientes", "Profissionais", "Serviços", "Horários", "Logout"]

tipo = st.session_state["usuario_tipo"]

if tipo is None:
    op = st.sidebar.selectbox("Menu", menu_visitante)

    if op == "Login":
        LoginUI.main()
    elif op == "Abrir Conta":
        AbrirContaUI.main()

elif tipo == "cliente":
    op = st.sidebar.selectbox(
        f"Cliente: {st.session_state['usuario_nome']}",
        menu_cliente
    )

    if op == "Perfil":
        PerfilclientesUI.main()
    elif op == "Agendar Horário":
        ManterHorarioUI.main()
    elif op == "Logout":
        logout()

elif tipo == "profissional":
    op = st.sidebar.selectbox(
        f"Profissional: {st.session_state['usuario_nome']}",
        menu_profissional
    )

    if op == "Perfil":
        PerfilclientesUI.main()
    elif op == "Gerenciar Horários":
        ManterHorarioUI.main()
    elif op == "Logout":
        logout()

elif tipo == "admin":
    op = st.sidebar.selectbox(
        f"Admin: {st.session_state['usuario_nome']}",
        menu_admin
    )

    if op == "Clientes":
        ManterClienteUI.main()
    elif op == "Profissionais":
        ManterProfissionalUI.main()
    elif op == "Serviços":
        ManterServicoUI.main()
    elif op == "Horários":
        ManterHorarioUI.main()
    elif op == "Logout":
        logout()