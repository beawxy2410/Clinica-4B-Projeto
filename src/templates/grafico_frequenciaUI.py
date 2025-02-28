import streamlit as st
import pandas as pd
from models.atendimento import Atendimentos_CRUD


class GraficoFrequenciaUI:
    def main():
        st.header("Frequência de Atendimentos por Semana")
        GraficoFrequenciaUI.exibir_frequencia()

    def exibir_frequencia():
        atendimentos = Atendimentos_CRUD.listar()
        if len(atendimentos) == 0:
            st.write("Nenhum atendimento cadastrado.")
        else:
            dic = [{"data": atendimento.data} for atendimento in atendimentos]
            df = pd.DataFrame(dic)

            df['data'] = pd.to_datetime(df['data'])

            df['semana'] = df['data'].dt.to_period('W').dt.start_time
            frequencia_semanal = df.groupby('semana').size().reset_index(name='quantidade')

            st.write("Frequência de Atendimentos por Semana")
            st.dataframe(frequencia_semanal)

if __name__ == "__main__":
    GraficoFrequenciaUI.main()