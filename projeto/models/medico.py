from models.funcionario import Funcionario
from models.endereco import Endereco

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crm: str, salario: float) -> None:
        super().__init__(nome, telefone, email, endereco, salario)
        self.crm = crm
        self.validar_dados()

    def validar_dados(self):
        if len(self.crm) != 8:
            raise ValueError("CRM inválido: Deve conter 8 caracteres.")
        if not self.crm.isdigit():
            raise ValueError("CRM inválido: Deve conter apenas números.")

    def calcular_salario(self):
        """Implementação do método abstrato calcular_salario"""
        # Exemplo simples de cálculo de salário (pode ser ajustado conforme a lógica do projeto)
        return self.salario

    def __str__(self):
        return (f"Médico: {self.nome}\n"
                f"Telefone: {self.telefone}\n"
                f"CRM: {self.crm}\n"
                f"Email: {self.email}\n"
                f"Endereço: {self.endereco}\n"
                f"Salário: {self.salario:.2f}")
