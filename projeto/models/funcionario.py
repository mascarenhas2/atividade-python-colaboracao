from abc import ABC, abstractmethod
from projeto.models.endereco import Endereco

class Funcionario(ABC):
    def __init__(self, nome, telefone, email, endereco: Endereco, salario):
        # Validações do nome
        if len(nome) > 50:
            raise ValueError("O nome não pode ter mais de 50 caracteres.")
        # Validações do telefone
        if not telefone.isdigit() or len(telefone) != 9:
            raise ValueError("O telefone deve ter exatamente 9 dígitos.")
        # Validações do email
        if '@' not in email:
            raise ValueError("O email deve conter o @ para ser válido.")
        # Validações do salário
        if salario < 0:
            raise ValueError("O salário não pode ser negativo.")

        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.salario = salario

    def validar_dados(self):
        """Valida os dados do funcionário."""
        if self.salario < 0:
            raise ValueError("O salário não pode ser negativo.")

    @abstractmethod
    def calcular_salario(self):
        """Método abstrato para cálculo de salário, deve ser implementado nas classes filhas."""
        pass

    def __str__(self):
        return (f"\nFuncionário: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail: {self.email}"
                f"\n=== Endereço === {self.endereco}"
                f"\nSalário: R${self.salario:.2f}")
