import streamlit as st
import pandas as pd
from view import View
import time

class ManterPacienteUI:
    def main():
        st.header("Cadastro de Pacientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterPacienteUI.listar()
        with tab2:
            ManterPacienteUI.inserir()
        with tab3:
            ManterPacienteUI.atualizar()
        with tab4:
            ManterPacienteUI.excluir()

    def listar():
        pacientes = View.paciente_listar()
        if len(pacientes) == 0:
            st.write("Nenhum paciente cadastrado")
        else:
            dic = [obj.__dict__ for obj in pacientes]
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome do paciente")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o telefone")
        cpf = st.text_input("Digite o CPF")
        senha = st.text_input("Informe a senha", type="password")

        if st.button("Inserir"):
            try:
                View.paciente_inserir(nome, fone, email, cpf, senha)
                st.success("Paciente inserido com sucesso.")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.error(str(e))

    def atualizar():
        pacientes = View.paciente_listar()
        if len(pacientes) == 0:
            st.write("Nenhum paciente cadastrado")
        else:
            op = st.selectbox("Atualização de paciente", pacientes)
            nome = st.text_input("Informe o novo nome do paciente", op.nome)
            email = st.text_input("Informe o novo e-mail", op.email)
            fone = st.text_input("Informe o novo telefone", op.fone)
            cpf = st.text_input("Informe o CPF", op.cpf)
            senha = st.text_input("Informe a nova senha", op.senha, type="password")
            if st.button("Atualizar"):
                try:
                    View.paciente_atualizar(op.id, nome, fone, email, cpf, senha)
                    st.success("Paciente atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as e:
                    st.error(str(e))

    def excluir():
        pacientes = View.paciente_listar()
        if len(pacientes) == 0:
            st.write("Nenhum paciente cadastrado.")
        else:
            descricao_para_paciente = {f"ID: {c.id} - Nome: {c.nome}": c for c in pacientes}
            descricao_escolhida = st.selectbox("Exclusão de paciente", list(descricao_para_paciente.keys()))
            paciente_escolhido = descricao_para_paciente[descricao_escolhida]
            if st.button("Excluir"):
                try:
                    View.paciente_excluir(paciente_escolhido.id)
                    st.success("Paciente excluído com sucesso.")
                    time.sleep(2)
                    st.rerun()
                except ValueError as e:
                    st.error(str(e))