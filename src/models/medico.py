from models.crud import CRUDGeral
# from models.especialidade import Especialidade, Especialidades_CRUD

class Medico:
    def __init__(self, id, nome, id_especialidade, nome_especialidade):
        self.id = id
        self.nome = nome
        self.idEspecialidade = id_especialidade
        self.nomeEspecialidade = nome_especialidade 

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

    @property
    def id_especialidade(self):
        return self._id_especialidade

    @id_especialidade.setter
    def id_especialidade(self, value: int):
        self._id_especialidade = value

    @property
    def nome_especialidade(self):
        return self._nome_especialidade

    @nome_especialidade.setter
    def nome_especialidade(self, value: str):
        if value:
            self._nome_especialidade = value
        else:
            raise ValueError("Informe o nome da especialidade")

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.id_especialidade} - {self.nome_especialidade}"


class Medicos_CRUD(CRUDGeral):
    nome_arquivo = "medicos"

    @classmethod
    def to_dict(cls, obj: Medico) -> dict:
        return {
            "id": obj.id,
            "nome": obj.nome,
            "id_especialidade": obj.id_especialidade,
            "nome_especialidade": obj.nome_especialidade,  
        }

    @classmethod
    def from_dict(cls, data: dict) -> Medico:
        return Medico(
            data["id"],
            data["nome"],
            data["id_especialidade"],
            data["nome_especialidade"],  
        )

