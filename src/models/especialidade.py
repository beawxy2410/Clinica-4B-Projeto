from src.models.crud import CRUDGeral

class Especialidade:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value: str):
        if value:
            self._nome = value
        else:
            raise ValueError("Informe o nome do médico")

    def __str__(self):
        return f"{self.id} - {self.nome}"


class Especialidades_CRUD(CRUDGeral):
    nome_arquivo = "especialidades"

    @classmethod
    def to_dict(cls, obj: Especialidade) -> dict:
        return {
            "id": obj.id,
            "nome": obj.nome,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Especialidade:
        return Especialidade(
            data["id"],
            data["nome"],
        )
    