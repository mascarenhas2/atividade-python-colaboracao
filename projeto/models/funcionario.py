import pytest
from abc import ABC, abstractmethod
from projeto.models import endereco

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
        self.endereco = endereco
        self.salario = salario
