from models.crud  import CRUDGeral

class AtendimentoItem:
    def __init__(self, id, id_atendimento, id_procedimento):
        self.id = id
        self.id_atendimento = id_atendimento
        self.id_procedimento = id_procedimento

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def id_atendimento(self):
        return self._id_atendimento

    @id_atendimento.setter
    def id_atendimento(self, value: int):
        self._id_atendimento = value

    @property
    def id_procedimento(self):
        return self._id_procedimento

    @id_procedimento.setter
    def id_procedimento(self, value: int):
        self._id_procedimento = value

    def __str__(self):
        return f"{self.id} - Atendimento: {self.id_atendimento}, Procedimento: {self.id_procedimento}"


class AtendimentoItens_CRUD(CRUDGeral):
    nome_arquivo = "atendimento_itens"

    @classmethod
    def to_dict(cls, obj: AtendimentoItem) -> dict:
        return {
            "id": obj.id,
            "id_atendimento": obj.id_atendimento,
            "id_procedimento": obj.id_procedimento,
        }

    @classmethod
    def from_dict(cls, data: dict) -> AtendimentoItem:
        return AtendimentoItem(
            data["id"],
            data["id_atendimento"],
            data["id_procedimento"],
        )
