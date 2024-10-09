import pytest
from models.endereco import Endereco  # Substitua pelo caminho correto
from models.funcionario import Funcionario  # Substitua pelo caminho correto

# Classe Funcionario é abstrata, então vamos criar uma classe concreta para testar
class FuncionarioTeste(Funcionario):
    def calcular_salario(self):
        return self.salario

@pytest.fixture
def endereco_valido(): #Definindo o endereco correto
    return Endereco("Rua das Flores", "123", "Apto 45", "12345-678", "Cidade Exemplo")

def test_funcionario_inicializacao_valida(endereco_valido): #Teste de validade do endereco
    funcionario = FuncionarioTeste("João Silva", "999999999", "joao@example.com", endereco_valido, 5000.0)
    assert funcionario.nome == "João Silva"
    assert funcionario.telefone == "999999999"
    assert funcionario.email == "joao@example.com"
    assert funcionario.endereco == endereco_valido
    assert funcionario.salario == 5000.0

def test_funcionario_inicializacao_nome_invalido(endereco_valido): #Teste relacionado ao erro do nome
    with pytest.raises(ValueError):
        FuncionarioTeste("J" * 51, "999999999", "joao@example.com", endereco_valido, 5000.0)

def test_funcionario_inicializacao_telefone_invalido(endereco_valido): #Teste relacionado ao erro do telefone
    with pytest.raises(ValueError):
        FuncionarioTeste("João Silva", "12345678", "joao@example.com", endereco_valido, 5000.0)

def test_funcionario_inicializacao_email_invalido(endereco_valido): # Teste relacionado ao erro do email
    with pytest.raises(ValueError):
        FuncionarioTeste("João Silva", "999999999", "joaoexample.com", endereco_valido, 5000.0)

def test_funcionario_inicializacao_salario_negativo(endereco_valido): # Teste relacionado ao erro do salário negativo
    with pytest.raises(ValueError):
        FuncionarioTeste("João Silva", "999999999", "joao@example.com", endereco_valido, -1000.0)

def test_str_metodo(endereco_valido): #Teste relacionado ao metodo do ato de puxar os dados
    funcionario = FuncionarioTeste("João Silva", "999999999", "joao@example.com", endereco_valido, 5000.0)
    assert str(funcionario) == (
        "Funcionário: João Silva\n"
        "Telefone: 999999999\n"
        "Email: joao@example.com\n"
        "Endereço: Logradouro: Rua das Flores\n"
        "Número: 123\n"
        "Cidade: Cidade Exemplo\n"
        "CEP: 12345-678, Apto 45\n"
        "Salário: 5000.00"
    )

# Se precisar, adicione mais testes conforme necessário.
# TESTE FUNCIONANDO CORRETAMENTE