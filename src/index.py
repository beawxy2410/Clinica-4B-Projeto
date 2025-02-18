import streamlit as st
from src.view import View
from templates.manter_pacienteUI import ManterPacienteUI
from templates.manter_medicoUI import ManterMedicoUI
from templates.manter_especialidadeUI import ManterEspecialidadeUI
from templates.manter_procedimentoUI import ManterProcedimentoUI
from templates.manter_atendimentoUI import ManterAtendimentoUI
from templates.manter_atendimentoitemUI import ManterAtendimentoItemUI
from templates.abrir_agendaUI import AbrirAgendaUI
from templates.abrir_contaUI import AbrirContaUI
from templates.listar_atendimentoUI import ListarAtendimentoUI
from templates.loginUI import LoginUI

class IndexUI:
    @staticmethod
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema":
            LoginUI.main()
        if op == "Abrir Conta":
            AbrirContaUI.main()

    @staticmethod
    def menu_admin():
        op = st.sidebar.selectbox(
            "Menu",
            [
                "Cadastro de Pacientes",
                "Cadastro de Médicos",
                "Cadastro de Especialidades",
                "Cadastro de Procedimentos",
                "Cadastro de Atendimentos",
                "Cadastro de Itens de Atendimento",
                "Abrir Agenda do Dia",
            ],
        )
        if op == "Cadastro de Pacientes":
            ManterPacienteUI.main()
        if op == "Cadastro de Médicos":
            ManterMedicoUI.main()
        if op == "Cadastro de Especialidades":
            ManterEspecialidadeUI.main()
        if op == "Cadastro de Procedimentos":
            ManterProcedimentoUI.main()
        if op == "Cadastro de Atendimentos":
            ManterAtendimentoUI.main()
        if op == "Cadastro de Itens de Atendimento":
            ManterAtendimentoItemUI.main()
        if op == "Abrir Agenda do Dia":
            AbrirAgendaUI.main()

    @staticmethod
    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Listar Atendimentos"])
        if op == "Listar Atendimentos":
            ListarAtendimentoUI.main()

    @staticmethod
    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["paciente_id"]
            del st.session_state["paciente_nome"]
            st.rerun()

    @staticmethod
    def sidebar():
        if "paciente_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            admin = st.session_state["paciente_nome"] == "admin"
            st.sidebar.write("Bem-vindo(a), " + st.session_state["paciente_nome"])
            if admin:
                IndexUI.menu_admin()
            else:
                IndexUI.menu_cliente()
            IndexUI.sair_do_sistema()

    @staticmethod
    def main():
        View.paciente_admin()
        IndexUI.sidebar()


IndexUI.main()
