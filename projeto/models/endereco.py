class Endereco:
    def __init__(self, logradouro, numero, complemento, cep, cidade):
        if len(logradouro) > 100:
            raise ValueError("O logradouro não pode ter mais de 100 caracteres.")
        if not numero.isdigit():
            raise ValueError("O número deve ser um valor numérico.")
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

    def __str__(self):
        complemento_str = f", {self.complemento}" if self.complemento else ""
        return (
            f"Logradouro: {self.logradouro}\n"
            f"Número: {self.numero}{complemento_str}\n"
            f"Cidade: {self.cidade}\n"
            f"CEP: {self.cep}"
        )

# Exemplo de uso
endereco = Endereco("Rua das Flores", "123", "Apto 101", "12345-678", "Salvador")
print(endereco)
