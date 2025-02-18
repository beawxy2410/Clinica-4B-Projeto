import streamlit as st
from src.view import View

class LoginUI:
    @staticmethod
    def main():
        st.header("Entrar no Sistema")
        LoginUI.entrar()

    @staticmethod
    def entrar():
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Entrar"):
            paciente = View.paciente_autenticar(email, senha)
            if paciente is None:
                st.error("E-mail ou senha inválidos")
            else:
                st.session_state["paciente_id"] = paciente["id"]
                st.session_state["paciente_nome"] = paciente["nome"]
                st.success("Login realizado com sucesso!")
                st.rerun()  

