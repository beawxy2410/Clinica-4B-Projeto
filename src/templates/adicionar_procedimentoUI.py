import streamlit as st
from view import View
import time


class AdicionarProcedimentoUI:
    def main():
        st.header("Adicionar Procedimento em Atendimento")
        AdicionarProcedimentoUI.adicionar()

    def adicionar():
        atendimentos = View.atendimento_listar()
        atendimentos_em_andamento = [
            atendimento
            for atendimento in atendimentos
            if atendimento.id_paciente is not 0
        ]

        if len(atendimentos_em_andamento) == 0:
            st.write("Nenhum atendimento em andamento.")
        else:
            op = st.selectbox(
                "Selecione o atendimento para adicionar o procedimento",
                atendimentos_em_andamento,
                format_func=lambda x: f"ID: {x.id} - Paciente: {x.id_paciente} - Médico: {x.id_medico} - Data: {x.data.strftime('%d/%m/%Y')} - Horário: {x.horario.strftime('%H:%M')} - Valor Final: R${x.valor_final:.2f}",
            )

            procedimento = st.selectbox(
                "Selecione o procedimento",
                View.procedimento_listar(),
                format_func=lambda x: f"ID: {x.id} - Nome: {x.descricao} - Valor: R${x.valor:.2f}",
            )

            if st.button("Adicionar"):
                try:
                    View.atendimento_item_inserir(op.id, procedimento.id)
                    View.atendimento_atualizar_preco(op.id)
                    st.success("Procedimento adicionado ao atendimento com sucesso.")
                    time.sleep(2)
                    st.rerun()
                except ValueError as e:
                    st.error(str(e))
