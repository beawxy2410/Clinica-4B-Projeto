from models.crud import CRUDGeral

class Paciente:
    def __init__(self, id, nome, fone, email, cpf, senha):
        self.id = id
        self.nome = nome
        self.fone = fone
        self.email = email
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
    def fone(self):
        return self._fone

    @fone.setter
    def fone(self, value: str):
        if value:
            self._fone = value
        else:
            raise ValueError("Informe o telefone do paciente")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value: str):
        if value and "@" in value:  
            self._email = value
        else:
            raise ValueError("Informe um e-mail válido")

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
        return f"{self.id} - {self.nome} - {self.fone} - {self.email} - {self.cpf} - {self.senha}"

class Pacientes_CRUD(CRUDGeral):
    nome_arquivo = "pacientes"

    @classmethod
    def to_dict(cls, obj: Paciente) -> dict:
        return {
            "id": obj.id,
            "nome": obj.nome,
            "fone": obj.fone,
            "email": obj.email,
            "cpf": obj.cpf,
            "senha": obj.senha,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Paciente:
        return Paciente(
            data["id"],
            data["nome"],
            data["fone"],
            data["email"],
            data["cpf"],
            data["senha"],
        )


