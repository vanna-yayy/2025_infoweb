import streamlit as st
from view import View

class LoginUI:
    @staticmethod
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")

        if st.button("Entrar"):
            user = View.cliente_autenticar(email, senha)
            if user is None:
                user = View.profissional_autenticar(email, senha)

            if user is None:
                st.error("E-mail ou senha inválidos")
            else:
                st.session_state["usuario_id"] = user["id"]
                st.session_state["usuario_nome"] = user["nome"]
                st.session_state["usuario_tipo"] = user["tipo"]
                st.rerun()