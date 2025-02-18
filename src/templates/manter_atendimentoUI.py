import streamlit as st
import pandas as pd
from view import View
import time

class ManterAtendimentoUI:
    def main():
        st.header("Cadastro de Atendimentos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterAtendimentoUI.listar()
        with tab2:
            ManterAtendimentoUI.inserir()
        with tab3:
            ManterAtendimentoUI.atualizar()
        with tab4:
            ManterAtendimentoUI.excluir()

    def listar():
        atendimentos = View.atendimento_listar()
        if len(atendimentos) == 0:
            st.write("Nenhum atendimento cadastrado")
        else:
            dic = [obj.__dict__ for obj in atendimentos]
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        id_paciente = st.number_input("Informe o ID do paciente", min_value=1)
        id_medico = st.number_input("Informe o ID do médico", min_value=1)
        data = st.date_input("Informe a data do atendimento")
        horario = st.time_input("Informe o horário do atendimento")
        if st.button("Inserir"):
            try:
                View.atendimento_inserir(id_paciente, id_medico, data, horario)
                st.success("Atendimento inserido com sucesso.")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.error(str(e))

    def atualizar():
        atendimentos = View.atendimento_listar()
        if len(atendimentos) == 0:
            st.write("Nenhum atendimento cadastrado")
        else:
            op = st.selectbox("Atualização de atendimento", atendimentos)
            id_paciente = st.number_input("Informe o novo ID do paciente", op.id_paciente)
            id_medico = st.number_input("Informe o novo ID do médico", op.id_medico)
            data = st.date_input("Informe a nova data do atendimento", op.data)
            horario = st.time_input("Informe o novo horário do atendimento", op.horario)
            if st.button("Atualizar"):
                try:
                    View.atendimento_atualizar(op.id, id_paciente, id_medico, data, horario, op.valor_final)
                    st.success("Atendimento atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as e:
                    st.error(str(e))

    def excluir():
        atendimentos = View.atendimento_listar()
        if len(atendimentos) == 0:
            st.write("Nenhum atendimento cadastrado.")
        else:
            descricao_para_atendimento = {f"ID: {c.id} - Paciente: {c.id_paciente} - Médico: {c.id_medico}": c for c in atendimentos}
            descricao_escolhida = st.selectbox("Exclusão de atendimento", list(descricao_para_atendimento.keys()))
            atendimento_escolhido = descricao_para_atendimento[descricao_escolhida]
            if st.button("Excluir"):
                try:
                    View.atendimento_excluir(atendimento_escolhido.id)
                    st.success("Atendimento excluído com sucesso.")
                    time.sleep(2)
                    st.rerun()
                except ValueError as e:
                    st.error(str(e))