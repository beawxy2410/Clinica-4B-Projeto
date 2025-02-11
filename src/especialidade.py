from crud import CRUDGeral

class Especialidade:
    def __init__(self, id, nome, preco_por_hora):
        self.id = id
        self.nome = nome
        self.preco_por_hora = preco_por_hora


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
    def preco_por_hora(self):
        return self._preco_por_hora

    @preco_por_hora.setter
    def preco_por_hora(self, value: float):
        if value >= 0:
            self._preco_por_hora = value
        else:
            raise ValueError("O preço por hora deve ser positivo")


    def __str__(self):
        return f"{self.id} - {self.nome} - R${self.preco_por_hora:.2f}/hora"


class Especialidades_CRUD(CRUDGeral):
    nome_arquivo = "Especialidades"

    @classmethod
    def to_dict(cls, obj: Especialidade) -> dict:
        return {
            "id": obj.id,
            "nome": obj.nome,
            "preco_por_hora": obj.preco_por_hora,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Especialidade:
        return Especialidade(
            data["id"],
            data["nome"],
            data["preco_por_hora"],
        )
    
if __name__ == "__main__":
    # Criando algumas especialidades
    especialidade1 = Especialidade(1, "Cardiologista", 200.00)
    especialidade2 = Especialidade(2, "Dermatologista", 180.00)
    especialidade3 = Especialidade(3, "Cardiologista", 210.00)

    # Inserindo as especialidades
    Especialidades_CRUD.inserir(especialidade1)
    Especialidades_CRUD.inserir(especialidade2)
    Especialidades_CRUD.inserir(especialidade3)

    # Listando todas as especialidades
    print("Lista de especialidades:")
    for e in Especialidades_CRUD.listar():
        print(e)

    # Listando as especialidades Cardiologistas
    print("\nEspecialidade com id 2:")
    e = Especialidades_CRUD.listar_id(2)
    print(e)

    # Atualizando uma especialidade
    especialidade1.name = "Cardiologista Pediátrico"
    Especialidades_CRUD.atualizar(especialidade1)

    # Listando as especialidades após atualização
    print("\nLista de especialidades após atualização:")
    for e in Especialidades_CRUD.listar():
        print(e)

    # Excluindo uma especialidade
    Especialidades_CRUD.excluir(especialidade2.id)

    # Listando as especialidades após exclusão
    print("\nLista de especialidades após exclusão:")
    for e in Especialidades_CRUD.listar():
        print(e)
