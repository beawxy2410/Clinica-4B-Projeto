
from crud import CRUDGeral

class Medico:
    def __init__(self, id, nome, id_especialidade):
        self.id = id
        self.nome = nome
        self.id_especialidade = id_especialidade

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

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.id_especialidade}"


class Medicos_CRUD(CRUDGeral):
    nome_arquivo = "medicos"

    @classmethod
    def to_dict(cls, obj: Medico) -> dict:
        return {
            "id": obj.id,
            "nome": obj.nome,
            "id_especialidade": obj.id_especialidade,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Medico:
        return Medico(
            data["id"],
            data["nome"],
            data["id_especialidade"],
        )

    @classmethod
    def listar_por_id_especialidade(cls, id_especialidade: str) -> list[Medico]:
        medicos = cls.listar()  
        return [medico for medico in medicos if medico.id_especialidade == id_especialidade]


if __name__ == "__main__":
    # Criando alguns médicos
    medico1 = Medico(None, "Dr. João", "Cardiologista")
    medico2 = Medico(None, "Dra. Maria", "Dermatologista")
    medico3 = Medico(None, "Dr. Pedro", "Cardiologista")

    # Inserindo médicos
    Medicos_CRUD.inserir(medico1)
    Medicos_CRUD.inserir(medico2)
    Medicos_CRUD.inserir(medico3)

    # Listando todos os médicos
    print("Lista de médicos:")
    for m in Medicos_CRUD.listar():
        print(m)

    # Listando os médicos cardiologistas
    print("\nLista de médicos Cardiologistas:")
    for m in Medicos_CRUD.listar_por_id_especialidade("Cardiologista"):
        print(m)

    # Listando os médicos dermatologistas
    print("\nLista de médicos Dermatologistas:")
    for m in Medicos_CRUD.listar_por_id_especialidade("Dermatologista"):
        print(m)

    # Atualizando um médico
    medico1.nome = "Dr. Jésse"
    Medicos_CRUD.atualizar(medico1)

    # Listando os médicos após atualização
    print("\nLista de médicos após atualização:")
    for m in Medicos_CRUD.listar():
        print(m)

    # Excluindo um médico
    Medicos_CRUD.excluir(medico2.id)

    # Listando os médicos após exclusão
    print("\nLista de médicos após exclusão:")
    for m in Medicos_CRUD.listar():
        print(m)
