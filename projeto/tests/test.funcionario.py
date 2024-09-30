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
