from crud import CRUDGeral

class Procedimento:
    def __init__(self, id, descricao, valor):
        self.id = id
        self.descricao = descricao
        self.valor = valor

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value: str):
        if value:
            self._descricao = value
        else:
            raise ValueError("Informe a descrição do procedimento")

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, value: float):
        if value >= 0:
            self._valor = value
        else:
            raise ValueError("O valor deve ser positivo")

    def __str__(self):
        return f"{self.id} - {self.descricao} - R${self.valor:.2f}"


class Procedimentos_CRUD(CRUDGeral):
    nome_arquivo = "procedimentos"

    @classmethod
    def to_dict(cls, obj: Procedimento) -> dict:
        return {
            "id": obj.id,
            "descricao": obj.descricao,
            "valor": obj.valor,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Procedimento:
        return Procedimento(
            data["id"],
            data["descricao"],
            data["valor"],
        )
    

if __name__ == "__main__":
    # Criando alguns procedimentos
    procedimento1 = Procedimento(None, "Consulta médica", 100.00)
    procedimento2 = Procedimento(None, "Exame de sangue", 50.00)
    procedimento3 = Procedimento(None, "Raio-X", 150.00)

    # Inserindo procedimentos
    Procedimentos_CRUD.inserir(procedimento1)
    Procedimentos_CRUD.inserir(procedimento2)
    Procedimentos_CRUD.inserir(procedimento3)

    # Listando todos os procedimentos
    print("Lista de procedimentos:")
    for p in Procedimentos_CRUD.listar():
        print(p)

    # Atualizando um procedimento
    procedimento1.descricao = "Consulta médica geral"
    procedimento1.valor = 120.00
    Procedimentos_CRUD.atualizar(procedimento1)

    # Listando após atualização
    print("\nLista de procedimentos após atualização:")
    for p in Procedimentos_CRUD.listar():
        print(p)

    # Excluindo um procedimento
    Procedimentos_CRUD.excluir(procedimento2.id)

    # Listando após exclusão
    print("\nLista de procedimentos após exclusão:")
    for p in Procedimentos_CRUD.listar():
        print(p)
