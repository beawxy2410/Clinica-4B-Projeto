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
            especialidade = View.especialidade_listar_id(medico.id_especialidade)
            medicos_nomes[medico.id] = f"{medico.nome} - {especialidade.nome}"

        atendimentos_medicos = {}
        for atendimento in atendimentos:
            atendimentos_medicos[atendimento.id] = atendimento.id_medico

        dados = {}
        for medico in medicos_nomes.values():
            dados[medico] = 0.0

        for item in atendimento_itens:
            id_medico = atendimentos_medicos[item.id_atendimento]
            descricao = medicos_nomes[id_medico]
            valor = procedimento_valores[item.id_procedimento]

            dados[descricao] += valor

        data = {
            "medico": list(dados.keys()),
            "valor": list(dados.values()),
        }

        df = pd.DataFrame(data)

        fig, ax = plt.subplots()
        ax.bar(df["medico"], df["valor"], color="skyblue")
        ax.set_xlabel("Médicos")
        ax.set_ylabel("Valor")
        ax.set_title("Valor por Médico")
        ax.tick_params(axis="x", rotation=45)

        st.pyplot(fig)
