from datetime import datetime, timedelta
from models.especialidade import Especialidade, Especialidades_CRUD
from models.medico import Medico, Medicos_CRUD
from models.procedimento import Procedimento, Procedimentos_CRUD
from models.pacientes import Paciente, Pacientes_CRUD
from models.atendimento_item import AtendimentoItem, AtendimentoItens_CRUD
from models.atendimento import Atendimento, Atendimentos_CRUD


class View:
    @staticmethod
    def abrir_cruds():
        Especialidades_CRUD.abrir()
        Medicos_CRUD.abrir()
        Procedimentos_CRUD.abrir()
        Pacientes_CRUD.abrir()
        Atendimentos_CRUD.abrir()
        AtendimentoItens_CRUD.abrir()
    
    @staticmethod
    def paciente_admin():
        for paciente in Pacientes_CRUD.listar():
            if paciente.email == "@admin":
                return

        admin_paciente = Paciente(
            None, "admin", "000000000", "@admin", "00000000000", "1234"
        )
        Pacientes_CRUD.inserir(admin_paciente)

    @staticmethod
    def especialidade_inserir(nome):
        especialidade = Especialidade(None, nome)
        Especialidades_CRUD.inserir(especialidade)

    @staticmethod
    def especialidade_listar():
        return Especialidades_CRUD.listar()

    @staticmethod
    def especialidade_listar_id(id):
        return Especialidades_CRUD.listar_id(id)

    @staticmethod
    def especialidade_atualizar(id, nome):
        especialidade = Especialidade(id, nome)
        Especialidades_CRUD.atualizar(especialidade)

    @staticmethod
    def especialidade_excluir(id):
        Especialidades_CRUD.excluir(id)

    @staticmethod
    def medico_inserir(nome, id_especialidade):
        medico = Medico(None, nome, id_especialidade)
        Medicos_CRUD.inserir(medico)

    @staticmethod
    def medico_listar():
        return Medicos_CRUD.listar()

    @staticmethod
    def medico_listar_id(id):
        return Medicos_CRUD.listar_id(id)

    @staticmethod
    def medico_listar_por_especialidade(id_especialidade):
        return Medicos_CRUD.listar_por_id_especialidade(id_especialidade)

    @staticmethod
    def medico_atualizar(id, nome, id_especialidade):
        medico = Medico(id, nome, id_especialidade)
        Medicos_CRUD.atualizar(medico)

    @staticmethod
    def medico_excluir(id):
        Medicos_CRUD.excluir(id)

    @staticmethod
    def procedimento_inserir(descricao, valor):
        procedimento = Procedimento(None, descricao, valor)
        Procedimentos_CRUD.inserir(procedimento)

    @staticmethod
    def procedimento_listar():
        return Procedimentos_CRUD.listar()

    @staticmethod
    def procedimento_listar_id(id):
        return Procedimentos_CRUD.listar_id(id)

    @staticmethod
    def procedimento_atualizar(id, descricao, valor):
        procedimento = Procedimento(id, descricao, valor)
        Procedimentos_CRUD.atualizar(procedimento)

    @staticmethod
    def procedimento_excluir(id):
        Procedimentos_CRUD.excluir(id)

    @staticmethod
    def paciente_inserir(nome, fone, email, cpf, senha):
        paciente = Paciente(None, nome, fone, email, cpf, senha)
        Pacientes_CRUD.inserir(paciente)

    @staticmethod
    def paciente_listar():
        return Pacientes_CRUD.listar()

    @staticmethod
    def paciente_listar_id(id):
        return Pacientes_CRUD.listar_id(id)

    @staticmethod
    def paciente_atualizar(id, nome, fone, email, cpf, senha):
        paciente = Paciente(id, nome, fone, email, cpf, senha)
        Pacientes_CRUD.atualizar(paciente)

    @staticmethod
    def paciente_excluir(id):
        Pacientes_CRUD.excluir(id)

    @staticmethod
    def atendimento_item_inserir(id_atendimento, id_procedimento):
        item = AtendimentoItem(None, id_atendimento, id_procedimento)
        AtendimentoItens_CRUD.inserir(item)

    @staticmethod
    def atendimento_item_listar():
        return AtendimentoItens_CRUD.listar()

    @staticmethod
    def atendimento_item_listar_id(id):
        return AtendimentoItens_CRUD.listar_id(id)

    @staticmethod
    def atendimento_item_atualizar(id, id_atendimento, id_procedimento):
        item = AtendimentoItem(id, id_atendimento, id_procedimento)
        AtendimentoItens_CRUD.atualizar(item)

    @staticmethod
    def atendimento_item_excluir(id):
        AtendimentoItens_CRUD.excluir(id)

    @staticmethod
    def atendimento_inserir(id_paciente, id_medico, data, horario, valor_final=None):
        atendimento = Atendimento(
            None, id_paciente, id_medico, data, horario, valor_final
        )
        Atendimentos_CRUD.inserir(atendimento)

    @staticmethod
    def atendimento_listar():
        return Atendimentos_CRUD.listar()

    @staticmethod
    def atendimento_listar_id(id):
        return Atendimentos_CRUD.listar_id(id)

    @staticmethod
    def atendimento_atualizar(id, id_paciente, id_medico, data, horario, valor_final):
        atendimento = Atendimento(
            id, id_paciente, id_medico, data, horario, valor_final
        )
        Atendimentos_CRUD.atualizar(atendimento)

    @staticmethod
    def atendimento_excluir(id):
        Atendimentos_CRUD.excluir(id)

    @staticmethod
    def paciente_autenticar(email, senha):
        pacientes = Pacientes_CRUD.listar()
        for paciente in pacientes:
            if paciente.email == email and paciente.senha == senha:
                return {"id": paciente.id, "nome": paciente.nome}
        return None

    @staticmethod
    def abrir_agenda(data, hora_inicio, hora_fim, intervalo):
        try:
            di = datetime.combine(data, hora_inicio)
            df = datetime.combine(data, hora_fim)

            if di >= df:
                raise ValueError("A hora inicial deve ser anterior à hora final.")
            if intervalo <= 0:
                raise ValueError("O intervalo deve ser maior que zero.")
            if df - di < timedelta(minutes=intervalo):
                raise ValueError("O intervalo é maior que o período especificado.")

            x = di
            horarios = []
            while x <= df:
                horarios.append(x.strftime("%d/%m/%Y %H:%M"))
                x += timedelta(minutes=intervalo)
            return horarios

        except ValueError as e:
            raise ValueError(f"Erro nos parâmetros fornecidos: {e}")

    @staticmethod
    def listar_itens_por_atendimento(id_atendimento: int) -> list[AtendimentoItem]:
        itens = AtendimentoItens_CRUD.listar()
        return [item for item in itens if item.id_atendimento == id_atendimento]

    @staticmethod
    def listar_medicos_por_especialidade(id_especialidade: int) -> list[Medico]:
        medicos = Medicos_CRUD.listar()
        return [medico for medico in medicos if medico.id_especialidade == id_especialidade]


    @staticmethod
    def calcular_valor_final_atendimento(id_atendimento: int) -> float:
        itens_atendimento = View.listar_itens_por_atendimento(id_atendimento)
        valor_final = 0.0
        for item in itens_atendimento:
            procedimento = Procedimentos_CRUD.listar_id(item.id_procedimento)
            if procedimento:
                valor_final += procedimento.valor
        atendimento = Atendimentos_CRUD.listar_id(id_atendimento)
        if atendimento:
            atendimento.valor_final = valor_final
            Atendimentos_CRUD.atualizar(atendimento)
        
        return valor_final
