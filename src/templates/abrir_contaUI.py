import streamlit as st
import time
from view import View

class AbrirContaUI:
    @staticmethod
    def main():
        st.header("Abrir Conta no Sistema")
        AbrirContaUI.inserir()

    @staticmethod
    def inserir():
        nome = st.text_input("Informe o nome")
        fone = st.text_input("Informe o telefone")
        email = st.text_input("Informe o e-mail")
        cpf = st.text_input("Informe o CPF")
        senha = st.text_input("Informe a senha", type="password")

        if st.button("Inserir"):
            try:
                View.paciente_inserir(nome, fone, email, cpf, senha)
                st.success("Conta criada com sucesso!")
                time.sleep(2)  
                st.rerun()  
            except ValueError as e:
                st.error(f"Erro ao criar conta: {str(e)}")
