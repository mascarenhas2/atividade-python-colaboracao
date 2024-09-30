# projeto/test_funcionario.py

import pytest
from projeto.models import Endereco
from models import Funcionario 

@pytest.fixture
def endereco_exemplo():
    return Endereco(rua="Rua A", numero="123", cidade="Cidade B")

def test_funcionario_inicializacao(endereco_exemplo):
    funcionario = Funcionario(
        nome="João Silva",
        telefone="123456789",
        email="joao@exemplo.com",
        endereco=endereco_exemplo,
        salario=5000.0
    )
    
    assert funcionario.nome == "João Silva"
    assert funcionario.telefone == "123456789"
    assert funcionario.email == "joao@exemplo.com"
    assert funcionario.endereco.rua == "Rua A"
    assert funcionario.endereco.numero == "123"
    assert funcionario.endereco.cidade == "Cidade B"
    assert funcionario.salario == 5000.0

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
