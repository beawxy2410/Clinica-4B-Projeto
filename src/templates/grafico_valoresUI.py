import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from view import View


class GraficoValoresUI:
    @staticmethod
    def main():
        st.header("Gráfico de Ganhos por Médico")

        medicos = View.medico_listar()
        procedimentos = View.procedimento_listar()
        atendimentos = View.atendimento_listar()
        atendimento_itens = View.atendimento_item_listar()

        procedimento_valores = {}
        for procedimento in procedimentos:
            procedimento_valores[procedimento.id] = procedimento.valor

        medicos_nomes = {}
        for medico in medicos:
            medicos_nomes[medico.id] = medico.nome

        atendimentos_medicos = {}
        for atendimento in atendimentos:
            atendimentos_medicos[atendimento.id] = atendimento.id_medico

        dados = {}
        for medico in medicos_nomes.values():
            dados[medico] = 0

        for item in atendimento_itens:
            dados[
                medicos_nomes[atendimentos_medicos[item.id_atendimento]]
            ] += procedimento_valores[item.id_procedimento]

        data = {
            "Nome do Médico": list(dados.keys()),
            "Valor": list(dados.values()),
        }

        df = pd.DataFrame(data)

        fig, ax = plt.subplots()
        ax.bar(df["Nome do Médico"], df["Valor"], color="skyblue")
        ax.set_xlabel("Nome do Médico")
        ax.set_ylabel("Valor")
        ax.set_title("Valor por Médico")
        ax.tick_params(axis="x", rotation=45)

        st.pyplot(fig)
