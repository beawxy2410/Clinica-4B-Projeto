import streamlit as st
from models.atendimento import Atendimentos_CRUD
from models.medico import Medicos_CRUD
from models.paciente import Pacientes_CRUD
from datetime import date, time
import time

class AgendarAtendimentoUI:
    def main():
        st.header("Agendar Atendimento")
        AgendarAtendimentoUI.agendar()

    def agendar():
        # Lista de médicos e pacientes
        medicos = Medicos_CRUD.listar()
        pacientes = Pacientes_CRUD.listar()

        if len(medicos) == 0 or len(pacientes) == 0:
            st.write("Nenhum médico ou paciente cadastrado.")
        else:
            # Selecionar paciente
            paciente_para_descricao = {f"ID: {pac.id} - Nome: {pac.nome}": pac for pac in pacientes}
            descricao_paciente = st.selectbox("Selecione o paciente", list(paciente_para_descricao.keys()))
            paciente_escolhido = paciente_para_descricao[descricao_paciente]

            # Selecionar médico
            medico_para_descricao = {f"ID: {med.id} - Nome: {med.nome}": med for med in medicos}
            descricao_medico = st.selectbox("Selecione o médico", list(medico_para_descricao.keys()))
            medico_escolhido = medico_para_descricao[descricao_medico]

            # Selecionar data e horário
            data = st.date_input("Selecione a data", min_value=date.today())
            horario = st.time_input("Selecione o horário")

            # Inserir valor final
            valor_final = st.number_input("Informe o valor final", min_value=0.0, format="%.2f")

            if st.button("Agendar"):
                try:
                    # Cria um novo atendimento
                    novo_atendimento = Atendimentos_CRUD.inserir(
                        id=None,  # O ID será gerado automaticamente
                        id_paciente=paciente_escolhido.id,
                        id_medico=medico_escolhido.id,
                        data=data,
                        horario=horario,
                        valor_final=valor_final
                    )
                    st.success("Atendimento agendado com sucesso.")
                    time.sleep(2)
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao agendar atendimento: {str(e)}")

if __name__ == "__main__":
    AgendarAtendimentoUI.main()