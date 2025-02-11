from crud import CRUDGeral

class Atendimento:
    def __init__(self, id, id_paciente, id_medico):
        self.id = id
        self.id_paciente = id_paciente
        self.id_medico = id_medico

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

    def __str__(self):
        return f"{self.id} - Paciente: {self.id_paciente}, Médico: {self.id_medico}"


class Atendimentos_CRUD(CRUDGeral):
    nome_arquivo = "atendimentos"

    @classmethod
    def to_dict(cls, obj: Atendimento) -> dict:
        return {
            "id": obj.id,
            "id_paciente": obj.id_paciente,
            "id_medico": obj.id_medico,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Atendimento:
        return Atendimento(
            data["id"],
            data["id_paciente"],
            data["id_medico"],
        )


if __name__ == "__main__":
    # Criando atendimentos
    atendimento1 = Atendimento(None, 1, 101)  # Criando o atendimento 1
    atendimento2 = Atendimento(None, 2, 102)  # Criando o atendimento 2
    
    # Inserindo atendimentos
    Atendimentos_CRUD.inserir(atendimento1)
    Atendimentos_CRUD.inserir(atendimento2)

    # Listando todos os atendimentos
    print("Lista de atendimentos:")
    for atendimento in Atendimentos_CRUD.listar():
        print(atendimento)

    # Atualizando um atendimento (alterando o médico)
    atendimento1.id_medico = 103  # Mudando o médico do atendimento 1
    Atendimentos_CRUD.atualizar(atendimento1)

    # Listando após a atualização
    print("\nLista de atendimentos após atualização:")
    for atendimento in Atendimentos_CRUD.listar():
        print(atendimento)

    # Excluindo atendimento
    Atendimentos_CRUD.excluir(atendimento2.id)

    # Listando após a exclusão
    print("\nLista de atendimentos após exclusão:")
    for atendimento in Atendimentos_CRUD.listar():
        print(atendimento)

