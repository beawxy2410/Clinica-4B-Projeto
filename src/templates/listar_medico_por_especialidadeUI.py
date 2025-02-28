import streamlit as st
import pandas as pd
from models.medico import Medicos_CRUD
from models.especialidade import Especialidades_CRUD

class ListarMedicoPorEspecialidadeUI:
    def main():
        st.header("Listar Médicos por Especialidade")
        ListarMedicoPorEspecialidadeUI.listar()

    def listar():
        medicos = Medicos_CRUD.listar()
        especialidades = Especialidades_CRUD.listar()

        if len(medicos) == 0 or len(especialidades) == 0:
            st.write("Nenhum médico ou especialidade cadastrada.")
        else:
            # Cria um dicionário para mapear especialidades por ID
            especialidade_por_id = {esp.id: esp.nome for esp in especialidades}

            # Cria uma lista de dicionários com os dados dos médicos e especialidades
            dados = []
            for med in medicos:
                dados.append({
                    "ID Médico": med.id,
                    "Nome Médico": med.nome,
                    "ID Especialidade": med.id_especialidade,
                })

            # Exibe os dados em um DataFrame
            df = pd.DataFrame(dados)
            st.dataframe(df)

if __name__ == "__main__":
    ListarMedicoPorEspecialidadeUI.main()