from models.funcionario import Funcionario
from models.endereco import endereco

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, crm: str, email: str, endereco: endereco) -> None:
        super().__init__(nome, telefone, crm , email, endereco)
