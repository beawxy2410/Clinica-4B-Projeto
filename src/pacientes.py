from crud import CRUDGeral

class Paciente:
    def __init__(self, id, nome, idade, fone, cpf, senha):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.fone = fone
        self.cpf = cpf
        self.senha = senha

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
            raise ValueError("Informe o nome do paciente")

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, value: int):
        if value >= 0:
            self._idade = value
        else:
            raise ValueError("Idade deve ser um valor positivo")

    @property
    def fone(self):
        return self._fone

    @fone.setter
    def fone(self, value: str):
        if value:
            self._fone = value
        else:
            raise ValueError("Informe o telefone do paciente")

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value: str):
        if value:
            self._cpf = value
        else:
            raise ValueError("Informe o CPF do paciente")

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, value: str):
        if value:
            self._senha = value
        else:
            raise ValueError("Informe a senha do paciente")

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.idade} - {self.cpf} - {self.fone} - {self.senha}"

class Pacientes_CRUD(CRUDGeral):
    nome_arquivo = "pacientes"

    @classmethod
    def to_dict(cls, obj: Paciente) -> dict:
        return {
            "id": obj.id,
            "nome": obj.nome,
            "idade": obj.idade,
            "fone": obj.fone,
            "cpf": obj.cpf,
            "senha": obj.senha,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Paciente:
        return Paciente(
            data["id"],
            data["nome"],
            data["idade"],
            data["fone"],
            data["cpf"],
            data["senha"],
        )


if __name__ == "__main__":
    # Criando alguns pacientes
    paciente1 = Paciente(None, "João Silva", 30, "1234-5678", "123.456.789-00", "123")
    paciente2 = Paciente(None, "Maria Oliveira", 25, "8765-4321", "987.654.321-00", "456")

    # Inserindo pacientes
    Pacientes_CRUD.inserir(paciente1)
    Pacientes_CRUD.inserir(paciente2)

    # Listando todos os pacientes
    print("Lista de pacientes:")
    for p in Pacientes_CRUD.listar():
        print(p)

    # Atualizando um paciente
    paciente1.nome = "João da Silva"
    Pacientes_CRUD.atualizar(paciente1)

    # Listando após atualização
    print("\nLista de pacientes após atualização:")
    for p in Pacientes_CRUD.listar():
        print(p)

    # Excluindo um paciente
    Pacientes_CRUD.excluir(paciente2.id)

    # Listando após exclusão
    print("\nLista de pacientes após exclusão:")
    for p in Pacientes_CRUD.listar():
        print(p)