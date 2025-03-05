import streamlit as st
from view import View
from datetime import datetime, time
import time


class AbrirAgendaUI:
    @staticmethod
    def main():
        st.header("Abrir Agenda de Atendimentos")
        AbrirAgendaUI.abrir_atendimento()

    @staticmethod
    def abrir_atendimento():
        data_str = st.text_input(
            "Informe a data no formato *dd/mm/aaaa*",
            datetime.now().strftime("%d/%m/%Y"),
        )

        hinicio_str = st.text_input("Informe o horário inicial no formato *HH:MM*")
        hfim_str = st.text_input("Informe o horário final no formato *HH:MM*")
        intervalo_str = st.text_input(
            "Informe o intervalo entre os atendimentos (minutos)"
        )

        if st.button("Inserir Atendimentos"):
            try:
                data = datetime.strptime(data_str, "%d/%m/%Y").date()
                hinicio = datetime.strptime(hinicio_str, "%H:%M").time()
                hfim = datetime.strptime(hfim_str, "%H:%M").time()
                intervalo = int(intervalo_str)

                horarios = View.abrir_agenda(data, hinicio, hfim, intervalo)

                for horario in horarios:
                    horario = datetime.strptime(horario, "%d/%m/%Y %H:%M")
                    View.atendimento_inserir(0, 0, horario.date(), horario.time(), 0)

                st.success("Atendimento(s) inserido(s) com sucesso!")
                time.sleep(2)
                st.rerun()

            except ValueError as e:
                st.error(f"Erro ao abrir agenda de atendimentos: {str(e)}")
