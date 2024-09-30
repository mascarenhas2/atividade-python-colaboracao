from models.funcionario import Funcionario
from models.endereco import Endereco  # Corrigi para 'Endereco' com E maiúsculo

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crm: str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm = crm
        self.validar_dados()  # Chama a validação no momento da inicialização

    def validar_dados(self):
        if not self.crm:
            raise ValueError("CRM INVÁLIDO: O campo precisa ser preenchido.")
        if len(self.crm) != 8:
            raise ValueError("CRM inválido: Deve conter 8 caracteres.")
        if not self.crm.isdigit():
            raise ValueError("CRM inválido: Deve conter apenas números.")
