from models.funcionario import Funcionario
from models.endereco import endereco

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: endereco, crm : str) -> None:
        super().__init__(nome, telefone,email, endereco)
        self.crm = crm

    def validar_dados(self):
        if not self.crm:
            raise ValueError("CRM INVALIDO: O campo precisa ser preenchido.")
        if len(self.crm) != 8: #Validar tamanho
            raise ValueError("CRM invalido: Deve conter 8 caracteres".)
