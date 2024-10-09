
class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
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
    def validar_cep(cep: str) -> bool:
        partes = cep.split('-')
        if len(partes) != 2:
            return False
        primeira_parte = partes[0]
        segunda_parte = partes[1]
        if len(primeira_parte) != 5 or len(segunda_parte) != 3:
            return False
        if not primeira_parte.isdigit() or not segunda_parte.isdigit():
            return False
        return True

    def __str__(self) -> str:
        complemento_str = f", {self.complemento}" if self.complemento else ""
        return (
            f"\nLogradouro: {self.logradouro}"
            f"\nNúmero: {self.numero}"
            f"\nCidade: {self.cidade}"
            f"\nCEP: {self.cep}{complemento_str}"
        )
