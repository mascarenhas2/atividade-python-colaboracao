# projeto/test_endereco.py

import pytest
from projeto.models import Endereco

def test_endereco_inicializacao():
    endereco = Endereco(
        logradouro="Rua A",
        numero="123",
        complemento="Apto 1",
        cep="12345-678",
        cidade="Cidade B"
    )
    
    assert endereco.logradouro == "Rua A", "O logradouro deve ser 'Rua A'"
    assert endereco.numero == "123", "O número deve ser '123'"
    assert endereco.complemento == "Apto 1", "O complemento deve ser 'Apto 1'"
    assert endereco.cep == "12345-678", "O CEP deve ser '12345-678'"
    assert endereco.cidade == "Cidade B", "A cidade deve ser 'Cidade B'"

def test_endereco_complemento_vazio():
    endereco = Endereco(
        logradouro="Rua B",
        numero="456",
        complemento="",
        cep="98765-432",
        cidade="Cidade C"
    )
    
    assert endereco.logradouro == "Rua B", "O logradouro deve ser 'Rua B'"
    assert endereco.numero == "456", "O número deve ser '456'"
    assert endereco.complemento == "", "O complemento deve estar vazio"
    assert endereco.cep == "98765-432", "O CEP deve ser '98765-432'"
    assert endereco.cidade == "Cidade C", "A cidade deve ser 'Cidade C'"
