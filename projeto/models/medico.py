from projeto.models.funcionario import Funcionario
from projeto.models.endereco import Endereco

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crm: str, salario: float) -> None:
        super().__init__(nome, telefone, email, endereco, salario)
        self.crm = crm
        self.validar_dados()

    def validar_dados(self):
        """Valida os dados do médico."""
        super().validar_dados()  # Chama a validação da classe base
        if len(self.crm) != 8:
            raise ValueError("CRM inválido: Deve conter 8 caracteres.")
        if not self.crm.isdigit():
            raise ValueError("CRM inválido: Deve conter apenas números.")

    def calcular_salario(self):
        """Implementação do método abstrato calcular_salario"""
        return self.salario

    def __str__(self):
        return (f"\nMédico: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nCRM: {self.crm}"
                f"\nEmail: {self.email}"
                f"\n=== Endereço === {self.endereco}"
                f"\nSalário: R${self.salario:.2f}")
