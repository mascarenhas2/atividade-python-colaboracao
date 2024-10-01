import pytest
from projeto.models.endereco import Endereco
from projeto.models.engenheiro import Engenheiro

@pytest.fixture
def endereco_exemplo():
    return Endereco("Rua dos Engenheiros", "456", "Apto 303", "65432-987", "Vitória da Conquista")


def test_engenheiro_nome_excedido(endereco_exemplo):
    with pytest.raises(ValueError, match="O nome não pode ter mais de 50 caracteres."):
        Engenheiro(
            nome="P" * 51,
            telefone="987654321",
            email="pedro@exemplo.com",
            endereco=endereco_exemplo,
            crea="87654321"
        )

def test_engenheiro_telefone_invalido(endereco_exemplo):
    with pytest.raises(ValueError, match="O telefone deve ter exatamente 9 dígitos."):
        Engenheiro(
            nome="Eng. Pedro",
            telefone="98765432",  # Telefone com menos dígitos
            email="pedro@exemplo.com",
            endereco=endereco_exemplo,
            crea="87654321"
        )

def test_engenheiro_email_invalido(endereco_exemplo):
    with pytest.raises(ValueError, match="O email deve ser válido."):
        Engenheiro(
            nome="Eng. Pedro",
            telefone="987654321",
            email="pedroexemplo.com",  # Email sem '@'
            endereco=endereco_exemplo,
            crea="87654321"
        )

