from abc import ABC, abstractmethod
from projeto.models.endereco import Endereco  # Corrigido para projeto.models

class Funcionario(ABC):
    def __init__(self, nome, telefone, email, endereco: Endereco, salario):
        if len(nome) > 50:
            raise ValueError("O nome não pode ter mais de 50 caracteres.")
        if not telefone.isdigit() or len(telefone) != 9:
            raise ValueError("O telefone deve ter exatamente 9 dígitos.")
        if '@' not in email:
            raise ValueError("O email deve ser válido.")
        if salario < 0:
            raise ValueError("O salário não pode ser negativo.")
        
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.salario = salario

    @abstractmethod
    def calcular_salario(self):
        pass

    def __str__(self):
        return (f"Funcionário: {self.nome}\n"
                f"Telefone: {self.telefone}\n"
                f"Email: {self.email}\n"
                f"Endereço: {self.endereco}\n"
                f"Salário: {self.salario:.2f}")
