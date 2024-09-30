import pytest 
from models.endereco import Endereco 
from models.funcionario import Funcionario
from models.engenheiro import Engenheiro

@pytest.fixture
def endereco_exemplo():
    return Endereco(rua="Rua B",numero="321",complemento ="Apto 2",cep = "87654-321", cidade="Cidade A",)

def test_engenheiro_inicializacao(endereco_exemplo):
    engenheiro = Engenheiro(
        nome = "Carlos",
        telefone = "987654321",
        email = "carlos@gmail.com",
        endereco = endereco_exemplo,
        crea = "12345678"
    )

    assert engenheiro.nome == "Carlos"
    assert engenheiro.telefone == "987654321"
    assert engenheiro.email == "carlos@gmail.com"
    assert engenheiro.endereco.rua == "Rua B"
    assert engenheiro.crea == "12345678"

def test_engenheiro_crea_vazio(endereco_exemplo):
    with pytest.raises(ValueError, match="CRM INVÁLIDO: O campo precisa ser preenchido."):
        Engenheiro(
            nome = "Carlos",
            telefone = "987654321",
            email = "carlos@gmail.com",
            endereco = endereco_exemplo,
            crea = ""
        )

def test_engenheiro_crea_tam_incorreto(endereco_exemplo):
    with pytest.raises(ValueError, match="CREA inválido: Deve conter 8 caracteres."):
        Engenheiro(
            nome = "Carlos",
            telefone = "987654321",
            email = "carlos@gmail.com",
            endereco = endereco_exemplo,
            crea = "1234567" #Apenas 7 caracteres
        )

def test_engenheiro_crea_nao_numerico(endereco_exemplo):
    with pytest.raises(ValueError, match="CREA inválido: Deve conter apenas números."):
        Engenheiro(
            nome = "Carlos",
            telefone = "987654321",
            email = "carlos@gmail.com",
            endereco = endereco_exemplo,
            crea = "1234567B" #CONTEM LETRAS 
        )        