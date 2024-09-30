from projeto.models import funcionario

# models.py

class Endereco:
    def __init__(self, logradouro, numero, complemento, cep, cidade):
        if len(logradouro) > 100:
            raise ValueError("O logradouro não pode ter mais de 100 caracteres.")
        if not numero.isdigit():
            raise ValueError("O número deve ser um valor numérico.")
        if not self.validar_cep(cep):
            raise ValueError("O CEP deve estar no formato 'XXXXX-XXX'.")
        if len(cidade) > 50:
            raise ValueError("A cidade não pode ter mais de 50 caracteres.")
        
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    @staticmethod
    def validar_cep(cep):
        return len(cep) == 10 and cep[5] == '-'
