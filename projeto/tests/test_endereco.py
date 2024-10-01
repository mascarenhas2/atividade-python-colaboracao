# projeto/tests/test_endereco.py
import pytest
from projeto.models.endereco import Endereco

def test_endereco_cep_invalido():
        Endereco(
            logradouro="Rua D",
            numero="789",
            complemento="Apto 2",
            cep="12345678",  # CEP sem o hífen
            cidade="Cidade D"
        )

def test_endereco_cep_valido():
    endereco = Endereco(
        logradouro="Rua D",
        numero="789",
        complemento="Apto 2",
        cep="12345-678",  # CEP válido
        cidade="Cidade D"
    )
    assert endereco.cep == "12345-678"
