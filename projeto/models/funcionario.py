# projeto/models/funcionario.py

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

    def __str__(self):
        return (f"Funcionário: {self.nome}\n"
                f"Telefone: {self.telefone}\n"
                f"Email: {self.email}\n"
                f"Endereço: {self.endereco}\n"
                f"Salário: {self.salario:.2f}")
