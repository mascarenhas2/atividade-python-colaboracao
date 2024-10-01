from models.funcionario import Funcionario
from models.endereco import Endereco  # Corrigi para 'Endereco' com E maiúsculo

class Medico:
    def __init__(self, nome, telefone, email, endereco, crm):
        if len(nome) > 50:
            raise ValueError("O nome não pode ter mais de 50 caracteres.")
        
        if len(telefone) != 9:
            raise ValueError("O telefone deve ter exatamente 9 dígitos.")
        
        if '@' not in email:
            raise ValueError("O email deve ser válido.")
        
        if len(crm) != 8:
            raise ValueError("CRM inválido: Deve conter 8 caracteres.")

        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.crm = crm
