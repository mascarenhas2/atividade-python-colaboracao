from projeto.models import funcionario

class Endereco():
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: float):
        # Inicializa os atributos do funcionário
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

