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
            dic = []
            for obj in medicos:
                dic.append(
                    {
                        "ID": obj.id,
                        "Médico": obj.nome,
                        "ID Especialidade": obj.id_especialidade,
                        "Especialidade": obj.nome_especialidade,
                    }
                )
            df = pd.DataFrame(dic)
            st.dataframe(df, hide_index=True)

    def inserir():
        nome = st.text_input("Informe o nome do médico")
        id_especialidade = st.number_input("Informe o ID da especialidade", min_value=1)
        nome_especialidade = st.text_input("Informe o nome da especialidade")
        if st.button("Inserir"):
            try:
                especialidade = View.especialidade_listar_id(id_especialidade)
                if not especialidade:
                    raise ValueError("Especialidade não encontrada")
                
                View.medico_inserir(nome, id_especialidade, nome_especialidade)
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
            nome_especialidade = st.text_input("Informe o nome da especialidade", value= op.nome_especialidade)
            if st.button("Atualizar"):
                try:
                    especialidade = View.especialidade_listar_id(id_especialidade)
                    if not especialidade:
                        raise ValueError("Especialidade não encontrada")
                    
                    View.medico_atualizar(op.id, nome, id_especialidade, nome_especialidade)
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
            descricao_para_medico = {f"ID: {c.id} - Nome: {c.nome} - Especialidade ID: {c.id_especialidade} - Especialidade: {c.nome_especialidade}": c for c in medicos}
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