import pytest
from abc import ABC, abstractmethod
from projeto.models import endereco

class Funcionario(ABC):
    def __init__(self, nome : str, telefone: str, email:str, endereco: endereco, salario:float) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.salario = salario