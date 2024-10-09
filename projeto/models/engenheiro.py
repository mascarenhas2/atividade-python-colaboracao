from projeto.models.funcionario import Funcionario
from projeto.models.endereco import Endereco

class Engenheiro(Funcionario):
    def __init__(self, nome, telefone, email, crea, endereco: Endereco, salario):
        super().__init__(nome, telefone, email, endereco, salario)
        self.crea = crea
        self.validar_dados()  # Chama a validação dos dados do engenheiro

    def validar_dados(self):
        """Valida os dados do engenheiro."""
        super().validar_dados()  # Chama a validação da classe base
        if not self.crea:
            raise ValueError("CREA INVÁLIDO: O campo precisa ser preenchido.")
        if len(self.crea) != 8:
            raise ValueError("CREA inválido: Deve conter 8 caracteres.")
        if not self.crea.isdigit():
            raise ValueError("CREA inválido: Deve conter apenas números.")

    def calcular_salario(self):
        return self.salario

    def __str__(self):
        return (f"\nEngenheiro: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nCREA: {self.crea}"
                f"\nEmail: {self.email}"
                f"\n=== Endereço === {self.endereco}"
                f"\nSalário: R${self.salario:.2f}")
