import streamlit as st
import pandas as pd
from view import View
import time

class ManterAtendimentoItemUI:
    def main():
        st.header("Cadastro de Itens de Atendimento")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterAtendimentoItemUI.listar()
        with tab2:
            ManterAtendimentoItemUI.inserir()
        with tab3:
            ManterAtendimentoItemUI.atualizar()
        with tab4:
            ManterAtendimentoItemUI.excluir()

    def listar():
        itens = View.atendimento_item_listar()
        if len(itens) == 0:
            st.write("Nenhum item de atendimento cadastrado")
        else:
            dic = [obj.__dict__ for obj in itens]
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        id_atendimento = st.number_input("Informe o ID do atendimento", min_value=1)
        id_procedimento = st.number_input("Informe o ID do procedimento", min_value=1)
        if st.button("Inserir"):
            try:
                View.atendimento_item_inserir(id_atendimento, id_procedimento)
                st.success("Item de atendimento inserido com sucesso.")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.error(str(e))

    def atualizar():
        itens = View.atendimento_item_listar()
        if len(itens) == 0:
            st.write("Nenhum item de atendimento cadastrado")
        else:
            op = st.selectbox("Atualização de item de atendimento", itens)
            id_atendimento = st.number_input("Informe o novo ID do atendimento", op.id_atendimento)
            id_procedimento = st.number_input("Informe o novo ID do procedimento", op.id_procedimento)
            if st.button("Atualizar"):
                try:
                    View.atendimento_item_atualizar(op.id, id_atendimento, id_procedimento)
                    st.success("Item de atendimento atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as e:
                    st.error(str(e))

    def excluir():
        itens = View.atendimento_item_listar()
        if len(itens) == 0:
            st.write("Nenhum item de atendimento cadastrado.")
        else:
            descricao_para_item = {f"ID: {c.id} - Atendimento: {c.id_atendimento} - Procedimento: {c.id_procedimento}": c for c in itens}
            descricao_escolhida = st.selectbox("Exclusão de item de atendimento", list(descricao_para_item.keys()))
            item_escolhido = descricao_para_item[descricao_escolhida]
            if st.button("Excluir"):
                try:
                    View.atendimento_item_excluir(item_escolhido.id)
                    st.success("Item de atendimento excluído com sucesso.")
                    time.sleep(2)
                    st.rerun()
                except ValueError as e:
                    st.error(str(e))