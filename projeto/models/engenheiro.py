from models.funcionario import Funcionario
from models.endereco import endereco 

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, crea: str, email: str, endereco: endereco) -> None:
        super().__init__(nome, telefone, crea , email, endereco)