
import pytest
from models.endereco import Endereco  # Importando a classe Endereco
from models.funcionario import Funcionario
from models.medico import Medico  # Certifique-se de que o caminho está correto

@pytest.fixture
def endereco_exemplo():
    return Endereco(rua="Rua A", numero="123", complemento="Apto 1", cep="12345-678", cidade="Cidade B")

def test_medico_inicializacao(endereco_exemplo):
    medico = Medico(
        nome="Dr. João",
        telefone="123456789",
        email="dr.joao@exemplo.com",
        endereco=endereco_exemplo,
        crm="12345678"
    )
    
    assert medico.nome == "Dr. João"
    assert medico.telefone == "123456789"
    assert medico.email == "dr.joao@exemplo.com"
    assert medico.endereco.rua == "Rua A"
    assert medico.crm == "12345678"

def test_medico_crm_vazio(endereco_exemplo):
    with pytest.raises(ValueError, match="CRM INVÁLIDO: O campo precisa ser preenchido."):
        Medico(
            nome="Dr. João",
            telefone="123456789",
            email="dr.joao@exemplo.com",
            endereco=endereco_exemplo,
            crm=""
        )

def test_medico_crm_tamanho_incorreto(endereco_exemplo):
    with pytest.raises(ValueError, match="CRM inválido: Deve conter 8 caracteres."):
        Medico(
            nome="Dr. João",
            telefone="123456789",
            email="dr.joao@exemplo.com",
            endereco=endereco_exemplo,
            crm="1234567"  # Apenas 7 caracteres
        )

def test_medico_crm_nao_numerico(endereco_exemplo):
    with pytest.raises(ValueError, match="CRM inválido: Deve conter apenas números."):
        Medico(
            nome="Dr. João",
            telefone="123456789",
            email="dr.joao@exemplo.com",
            endereco=endereco_exemplo,
            crm="1234567A"  # Contém uma letra
        )
