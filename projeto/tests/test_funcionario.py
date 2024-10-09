import pytest
from projeto.models.endereco import Endereco  # Certifique-se de que este caminho esteja correto
from projeto.models.funcionario import Funcionario  # Certifique-se de que este caminho esteja correto

# Classe Funcionario é abstrata, então vamos criar uma classe concreta para testar
class FuncionarioTeste(Funcionario):
    def calcular_salario(self):
        return self.salario

@pytest.fixture
def endereco_valido():  # Definindo o endereco correto
    return Endereco("Rua das Flores", "123", "Apto 45", "12345-678", "Cidade Exemplo")

def test_funcionario_inicializacao_valida(endereco_valido):  # Teste de validade do endereco
    funcionario = FuncionarioTeste("João Silva", "999999999", "joao@example.com", endereco_valido, 5000.0)
    assert funcionario.nome == "João Silva"
    assert funcionario.telefone == "999999999"
    assert funcionario.email == "joao@example.com"
    assert funcionario.endereco == endereco_valido
    assert funcionario.salario == 5000.0

def test_funcionario_inicializacao_nome_invalido(endereco_valido):  # Teste relacionado ao erro do nome
    with pytest.raises(ValueError):
        FuncionarioTeste("J" * 51, "999999999", "joao@example.com", endereco_valido, 5000.0)

def test_funcionario_inicializacao_telefone_invalido(endereco_valido):  # Teste relacionado ao erro do telefone
    with pytest.raises(ValueError):
        FuncionarioTeste("João Silva", "12345678", "joao@example.com", endereco_valido, 5000.0)

def test_funcionario_inicializacao_email_invalido(endereco_valido):  # Teste relacionado ao erro do email
    with pytest.raises(ValueError):
        FuncionarioTeste("João Silva", "999999999", "joaoexample.com", endereco_valido, 5000.0)

def test_funcionario_inicializacao_salario_negativo(endereco_valido):  # Teste relacionado ao erro do salário negativo
    with pytest.raises(ValueError):
        FuncionarioTeste("João Silva", "999999999", "joao@example.com", endereco_valido, -1000.0)

