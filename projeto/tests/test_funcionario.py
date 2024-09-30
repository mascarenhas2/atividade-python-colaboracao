# projeto/tests/test_funcionario.py
import pytest
from projeto.models.endereco import Endereco
from projeto.models.funcionario import Funcionario

@pytest.fixture
def endereco_exemplo():
    return Endereco("Rua das Flores", "123", "Apto 101", "12345-678", "Salvador")

def test_funcionario_creation(endereco_exemplo):
    funcionario = Funcionario("Andrei Luiz", "988112455", "andrei@2232.com", endereco_exemplo, 3000.00)

    assert funcionario.nome == "Andrei Luiz"
    assert funcionario.telefone == "988112455"
    assert funcionario.email == "andrei@2232.com"
    assert funcionario.endereco.logradouro == "Rua das Flores"
    assert funcionario.salario == 3000.00

def test_funcionario_nome_excedido(endereco_exemplo):
    with pytest.raises(ValueError, match="O nome não pode ter mais de 50 caracteres."):
        Funcionario(
            nome="A" * 51,
            telefone="123456789",
            email="joao@exemplo.com",
            endereco=endereco_exemplo,
            salario=5000.0
        )

def test_funcionario_telefone_invalido(endereco_exemplo):
    with pytest.raises(ValueError, match="O telefone deve ter exatamente 9 dígitos."):
        Funcionario(
            nome="João Silva",
            telefone="12345678",  # Telefone com menos dígitos
            email="joao@exemplo.com",
            endereco=endereco_exemplo,
            salario=5000.0
        )

def test_funcionario_email_invalido(endereco_exemplo):
    with pytest.raises(ValueError, match="O email deve ser válido."):
        Funcionario(
            nome="João Silva",
            telefone="123456789",
            email="joaoexemplo.com",  # Email sem '@'
            endereco=endereco_exemplo,
            salario=5000.0
        )

def test_funcionario_salario_negativo(endereco_exemplo):
    with pytest.raises(ValueError, match="O salário não pode ser negativo."):
        Funcionario(
            nome="João Silva",
            telefone="123456789",
            email="joao@exemplo.com",
            endereco=endereco_exemplo,
            salario=-1000.0  # Salário negativo
        )
