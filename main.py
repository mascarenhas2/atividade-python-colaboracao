# main.py
from projeto.models.endereco import Endereco
from projeto.models.funcionario import Funcionario

def main():
    funcionario = Funcionario(
        nome="Andrei Luiz",
        telefone="988112455",
        email="andrei@2232.com",
        endereco=Endereco("Rua das Flores", "123", "Apto 101", "12345-678", "Salvador"),
        salario= 3000.00
    )
    
    # Exibindo as informações do funcionário
    print(funcionario)


main()
