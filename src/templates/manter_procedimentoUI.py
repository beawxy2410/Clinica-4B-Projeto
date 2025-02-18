import streamlit as st
import pandas as pd
from src.view import View
import time

class ManterProcedimentoUI:
    def main():
        st.header("Cadastro de Procedimentos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterProcedimentoUI.listar()
        with tab2:
            ManterProcedimentoUI.inserir()
        with tab3:
            ManterProcedimentoUI.atualizar()
        with tab4:
            ManterProcedimentoUI.excluir()

    def listar():
        procedimentos = View.procedimento_listar()
        if len(procedimentos) == 0:
            st.write("Nenhum procedimento cadastrado")
        else:
            dic = [obj.__dict__ for obj in procedimentos]
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        descricao = st.text_input("Informe a descrição do procedimento")
        valor = st.number_input("Informe o valor do procedimento", min_value=0.0)
        if st.button("Inserir"):
            try:
                View.procedimento_inserir(descricao, valor)
                st.success("Procedimento inserido com sucesso.")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.error(str(e))

    def atualizar():
        procedimentos = View.procedimento_listar()
        if len(procedimentos) == 0:
            st.write("Nenhum procedimento cadastrado")
        else:
            op = st.selectbox("Atualização de procedimento", procedimentos)
            descricao = st.text_input("Informe a nova descrição do procedimento", op.descricao)
            valor = st.number_input("Informe o novo valor do procedimento", op.valor)
            if st.button("Atualizar"):
                try:
                    View.procedimento_atualizar(op.id, descricao, valor)
                    st.success("Procedimento atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as e:
                    st.error(str(e))

    def excluir():
        procedimentos = View.procedimento_listar()
        if len(procedimentos) == 0:
            st.write("Nenhum procedimento cadastrado.")
        else:
            descricao_para_procedimento = {f"ID: {c.id} - Descrição: {c.descricao}": c for c in procedimentos}
            descricao_escolhida = st.selectbox("Exclusão de procedimento", list(descricao_para_procedimento.keys()))
            procedimento_escolhido = descricao_para_procedimento[descricao_escolhida]
            if st.button("Excluir"):
                try:
                    View.procedimento_excluir(procedimento_escolhido.id)
                    st.success("Procedimento excluído com sucesso.")
                    time.sleep(2)
                    st.rerun()
                except ValueError as e:
                    st.error(str(e))