from models.funcionario import Funcionario
from models.endereco import Endereco 

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, crea: str, email: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, crea , email, endereco)
        self.crea = crea
        self.validar_dados()
    
    def validar_dados(self):
        if not self.crea:
            raise ValueError("CREA INVÁLIDO: O campo precisa ser preenchido.")
        if len(self.crea) != 8:
            raise ValueError("CREA inválido: Deve conter 8 caracteres.")
        if not self.crea.isdigit():
            raise ValueError("CREA inválido: Deve conter apenas números.")

