import streamlit as st
import pandas as pd
from view import View
import time

class ManterMedicoUI:
    def main():
        st.header("Cadastro de Médicos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterMedicoUI.listar()
        with tab2:
            ManterMedicoUI.inserir()
        with tab3:
            ManterMedicoUI.atualizar()
        with tab4:
            ManterMedicoUI.excluir()

    def listar():
        medicos = View.medico_listar()
        if len(medicos) == 0:
            st.write("Nenhum médico cadastrado")
        else:
            dic = [obj.__dict__ for obj in medicos]
            df = pd.DataFrame(dic)
            st.dataframe(
            df,
            column_config={
                "id": "ID",
                "nome": "Nome",
                "fone": "Telefone",
                "email": "E-mail",
                "cpf": "CPF",
                "senha": "Senha"
            },
            hide_index=True
        )

    def inserir():
        nome = st.text_input("Informe o nome do médico")
        id_especialidade = st.number_input("Informe o ID da especialidade", min_value=1)
        if st.button("Inserir"):
            try:
                View.medico_inserir(nome, id_especialidade)
                st.success("Médico inserido com sucesso.")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.error(str(e))

    def atualizar():
        medicos = View.medico_listar()
        if len(medicos) == 0:
            st.write("Nenhum médico cadastrado")
        else:
            op = st.selectbox("Atualização de médico", medicos, format_func=lambda x: f"ID: {x.id} - Nome: {x.nome} - Especialidade ID: {x.id_especialidade}")
            nome = st.text_input("Informe o novo nome do médico", value=op.nome)
            id_especialidade = st.number_input("Informe o novo ID da especialidade", value=op.id_especialidade)
            if st.button("Atualizar"):
                try:
                    View.medico_atualizar(op.id, nome, id_especialidade)
                    st.success("Médico atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as e:
                    st.error(str(e))

    def excluir():
        medicos = View.medico_listar()
        if len(medicos) == 0:
            st.write("Nenhum médico cadastrado.")
        else:
            descricao_para_medico = {f"ID: {c.id} - Nome: {c.nome} - Especialidade ID: {c.id_especialidade}": c for c in medicos}
            descricao_escolhida = st.selectbox("Exclusão de médico", list(descricao_para_medico.keys()))
            medico_escolhido = descricao_para_medico[descricao_escolhida]
            if st.button("Excluir"):
                try:
                    View.medico_excluir(medico_escolhido.id)
                    st.success("Médico excluído com sucesso.")
                    time.sleep(2)
                    st.rerun()
                except ValueError as e:
                    st.error(str(e))