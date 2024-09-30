import pytest
from abc import ABC, abstractmethod
from projeto.models import endereco # Corrigi a importação para refletir o nome da classe

class Funcionario:
    def __init__(self, nome, telefone, email, endereco, salario):
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
        self.endereco = endereco  # Supõe-se que 'endereco' seja um objeto da classe Endereco
        self.salario = salario

    def __str__(self):
        return (
            f"Nome: {self.nome}\n"
            f"Telefone: {self.telefone}\n"
            f"Email: {self.email}\n"
            f"Endereço: {self.endereco}\n" 
            f"Salário: R$ {self.salario:.2f}"  
        )

# Exemplo de uso
funcionario1 = Funcionario("João da Silva", "987654321", "joao@example.com", endereco, 3000.00)
endereco = Endereco("Rua das Flores", "123", "Apto 101", "12345-678", "Salvador")
print(funcionario1)
