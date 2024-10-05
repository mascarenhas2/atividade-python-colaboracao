from projeto.models.funcionario import Funcionario
from projeto.models.endereco import Endereco  # Corrigido para projeto.models

class Engenheiro(Funcionario):
    def __init__(self, nome, telefone, email, crea, endereco: Endereco, salario):
        super().__init__(nome, telefone, email, endereco, salario)
        self.crea = crea
        self.validar_dados()
    
    def validar_dados(self):
        if not self.crea:
            raise ValueError("CREA INVÁLIDO: O campo precisa ser preenchido.")
        if len(self.crea) != 8:
            raise ValueError("CREA inválido: Deve conter 8 caracteres.")
        if not self.crea.isdigit():
            raise ValueError("CREA inválido: Deve conter apenas números.")

    def calcular_salario(self):
        return self.salario
    
    def __str__(self):
        return (f"Engenheiro: {self.nome}\n"
                f"Telefone: {self.telefone}\n"
                f"CREA: {self.crea}\n"
                f"Email: {self.email}\n"
                f"Endereço: {self.endereco}\n"
                f"Salário: {self.salario:.2f}")
