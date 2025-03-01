import streamlit as st
from view import View
import time

class AtualizarValorAtendimentoUI:
    def main():
        st.header("Atualizar Valor de Atendimento")
        AtualizarValorAtendimentoUI.atualizar_valor()

    def atualizar_valor():
        atendimentos = View.atendimento_listar()
        atendimentos_em_andamento = [atendimento for atendimento in atendimentos if atendimento.valor_final is None]

        if len(atendimentos_em_andamento) == 0:
            st.write("Nenhum atendimento em andamento.")
        else:
            op = st.selectbox("Selecione o atendimento para atualizar o valor", atendimentos_em_andamento, format_func=lambda x: f"ID: {x.id} - Paciente: {x.id_paciente} - Médico: {x.id_medico} - Data: {x.data.strftime('%d/%m/%Y')} - Horário: {x.horario.strftime('%H:%M')}")

            novo_valor = st.number_input("Informe o valor final do atendimento", min_value=0.0, format="%.2f")

            if st.button("Atualizar Valor"):
                try:
                    View.atendimento_atualizar(op.id, op.id_paciente, op.id_medico, op.data, op.horario, novo_valor)
                    st.success("Valor do atendimento atualizado com sucesso.")
                    time.sleep(2)
                    st.rerun()
                except ValueError as e:
                    st.error(str(e))