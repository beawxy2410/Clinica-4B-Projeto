import streamlit as st
from view import View
from datetime import date, time
import time


class AgendarAtendimentoUI:
    def main():
        st.header("Agendar Atendimento")
        AgendarAtendimentoUI.agendar()

    def agendar():
        medicos = View.medico_listar()
        atendimentos = View.atendimento_listar()
        atendimentos_livres = []
        for at in atendimentos:
            if at.id_medico is 0:
                atendimentos_livres.append(at)

        if len(medicos) == 0 or len(atendimentos_livres) == 0:
            st.write("Nenhum médico ou atendimento cadastrado.")
        else:
            descricoes_medicos = {
                f"ID: {med.id} - Nome: {med.nome}": med for med in medicos
            }
            descricao_medico = st.selectbox(
                "Selecione o médico", list(descricoes_medicos.keys())
            )
            medico_escolhido = descricoes_medicos[descricao_medico]

            descricoes_atendimentos = {
                f"ID: {at.id} - Data: {at.data.strftime('%d/%m/%Y')} - Horário: {at.horario.strftime('%H:%M')}": at
                for at in atendimentos_livres
            }
            descricao_atendimento = st.selectbox(
                "Selecione o atendimento", list(descricoes_atendimentos.keys())
            )
            atendimento_escolhido = descricoes_atendimentos[descricao_atendimento]

            if st.button("Agendar"):
                try:
                    View.atendimento_atualizar(
                        id=atendimento_escolhido.id,
                        id_paciente=st.session_state["paciente_id"],
                        id_medico=medico_escolhido.id,
                        data=atendimento_escolhido.data,
                        horario=atendimento_escolhido.horario,
                        valor_final=atendimento_escolhido.valor_final,
                    )
                    st.success("Atendimento agendado com sucesso.")
                    time.sleep(2)
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao agendar atendimento: {str(e)}")
