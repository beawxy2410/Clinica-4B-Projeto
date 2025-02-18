import streamlit as st
import pandas as pd
from view import View

class ListarAtendimentoUI:
    def main():
        st.header("Listar Atendimentos")
        ListarAtendimentoUI.listar_atendimentos()

    def listar_atendimentos():
        atendimentos = View.atendimento_listar()

        if len(atendimentos) == 0:
            st.write("Nenhum atendimento cadastrado.")
        else:
            dic = []
            for atendimento in atendimentos:
                dic.append({
                    "ID": atendimento.id,
                    "Paciente": atendimento.id_paciente,
                    "Médico": atendimento.id_medico,
                    "Data": atendimento.data.strftime("%d/%m/%Y"),
                    "Horário": atendimento.horario.strftime("%H:%M"),
                    "Valor Final": f"R$ {atendimento.valor_final:.2f}"
                })

            df = pd.DataFrame(dic)
            st.dataframe(df)

