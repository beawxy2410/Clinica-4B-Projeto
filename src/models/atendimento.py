from datetime import date, time
from src.models.crud import CRUDGeral

class Atendimento:
    def __init__(self, id, id_paciente, id_medico, data: date, horario: time, valor_final: float ):
        self.id = id
        self.id_paciente = id_paciente
        self.id_medico = id_medico
        self.data = data
        self.horario = horario
        self.valor_final = valor_final  

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def id_paciente(self):
        return self._id_paciente

    @id_paciente.setter
    def id_paciente(self, value: int):
        self._id_paciente = value

    @property
    def id_medico(self):
        return self._id_medico

    @id_medico.setter
    def id_medico(self, value: int):
        self._id_medico = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value: date):
        self._data = value

    @property
    def horario(self):
        return self._horario

    @horario.setter
    def horario(self, value: time):
        self._horario = value

    @property
    def valor_final(self):
        return self._valor_final

    @valor_final.setter
    def valor_final(self, value: float):
        self._valor_final = value

    def __str__(self):
        return f"{self.id} - Paciente: {self.id_paciente}, Médico: {self.id_medico}, Data: {self.data}, Horário: {self.horario}, Valor Final: {self.valor_final}"

class Atendimentos_CRUD(CRUDGeral):
    nome_arquivo = "atendimentos"

    @classmethod
    def to_dict(cls, obj: Atendimento) -> dict:
        return {
            "id": obj.id,
            "id_paciente": obj.id_paciente,
            "id_medico": obj.id_medico,
            "data": obj.data.isoformat(),
            "horario": obj.horario.isoformat(),
            "valor_final": obj.valor_final, 
        }

    @classmethod
    def from_dict(cls, data: dict) -> Atendimento:
        return Atendimento(
            data["id"],
            data["id_paciente"],
            data["id_medico"],
            date.fromisoformat(data["data"]),
            time.fromisoformat(data["horario"]),
            data["valor_final"], 
        )

