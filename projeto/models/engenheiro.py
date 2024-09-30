from models.funcionario import Funcionario
from models.endereco import Endereco 

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, crea: str, email: str, Endereco: Endereco) -> None:
        super().__init__(nome, telefone, crea , email, Endereco)