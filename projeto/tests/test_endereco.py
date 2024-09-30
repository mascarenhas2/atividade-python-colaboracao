# projeto/test_endereco.py

import pytest
from models.endereco import Endereco


def test_endereco_inicializacao():
    endereco = Endereco(
        logradouro="Rua A",
        numero="123",
        complemento="Apto 1",
        cep="12345-678",
        cidade="Cidade B"
    )
    
    assert endereco.logradouro == "Rua A"
    assert endereco.numero == "123"
    assert endereco.complemento == "Apto 1"
    assert endereco.cep == "12345-678"
    assert endereco.cidade == "Cidade B"

def test_endereco_complemento_vazio():
    endereco = Endereco(
        logradouro="Rua B",
        numero="456",
        complemento="",
        cep="98765-432",
        cidade="Cidade C"
    )
    
    assert endereco.logradouro == "Rua B"
    assert endereco.numero == "456"
    assert endereco.complemento == ""
    assert endereco.cep == "98765-432"
    assert endereco.cidade == "Cidade C"

def test_endereco_logradouro_excedido():
    with pytest.raises(ValueError, match="O logradouro não pode ter mais de 100 caracteres."):
        Endereco(
            logradouro="A" * 101,
            numero="123",
            complemento="Apto 1",
            cep="12345-678",
            cidade="Cidade B"
        )

def test_endereco_numero_invalido():
    with pytest.raises(ValueError, match="O número deve ser um valor numérico."):
        Endereco(
            logradouro="Rua C",
            numero="ABC",  # Número não numérico
            complemento="Apto 1",
            cep="12345-678",
            cidade="Cidade B"
        )

def test_endereco_cep_invalido():
    with pytest.raises(ValueError, match="O CEP deve estar no formato 'XXXXX-XXX'."):
        Endereco(
            logradouro="Rua D",
            numero="789",
            complemento="Apto 2",
            cep="12345678",  # CEP sem o hífen
            cidade="Cidade D"
        )

def test_endereco_cidade_excedida():
    with pytest.raises(ValueError, match="A cidade não pode ter mais de 50 caracteres."):
        Endereco(
            logradouro="Rua E",
            numero="101",
            complemento="Apto 3",
            cep="12345-678",
            cidade="C" * 51  # Cidade excedendo o limite
        )
