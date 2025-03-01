import streamlit as st
import pandas as pd
from view import View
import time

class ManterEspecialidadeUI:
    def main():
        st.header("Cadastro de Especialidades")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterEspecialidadeUI.listar()
        with tab2:
            ManterEspecialidadeUI.inserir()
        with tab3:
            ManterEspecialidadeUI.atualizar()
        with tab4:
            ManterEspecialidadeUI.excluir()

    def listar():
        especialidades = View.especialidade_listar()
        if len(especialidades) == 0:
            st.write("Nenhuma especialidade cadastrada")
        else:
            dic = [obj.__dict__ for obj in especialidades]
            df = pd.DataFrame(dic)
            st.dataframe(df, hide_index=True)

    def inserir():
        nome = st.text_input("Informe o nome da especialidade")
        if st.button("Inserir"):
            try:
                View.especialidade_inserir(nome)
                st.success("Especialidade inserida com sucesso.")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.error(str(e))

    def atualizar():
        especialidades = View.especialidade_listar()
        if len(especialidades) == 0:
            st.write("Nenhuma especialidade cadastrada")
        else:
            op = st.selectbox("Atualização de especialidade", especialidades)
            nome = st.text_input("Informe o novo nome da especialidade", op.nome)
            if st.button("Atualizar"):
                try:
                    View.especialidade_atualizar(op.id, nome)
                    st.success("Especialidade atualizada com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as e:
                    st.error(str(e))

    def excluir():
        especialidades = View.especialidade_listar()
        if len(especialidades) == 0:
            st.write("Nenhuma especialidade cadastrada.")
        else:
            descricao_para_especialidade = {f"ID: {c.id} - Nome: {c.nome}": c for c in especialidades}
            descricao_escolhida = st.selectbox("Exclusão de especialidade", list(descricao_para_especialidade.keys()))
            especialidade_escolhida = descricao_para_especialidade[descricao_escolhida]
            if st.button("Excluir"):
                try:
                    View.especialidade_excluir(especialidade_escolhida.id)
                    st.success("Especialidade excluída com sucesso.")
                    time.sleep(2)
                    st.rerun()
                except ValueError as e:
                    st.error(str(e))