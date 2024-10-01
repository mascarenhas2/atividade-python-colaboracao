import pytest
from projeto.models.endereco import Endereco
from projeto.models.medico import Medico

@pytest.fixture
def test_medico_creation_basico(endereco_exemplo):
    medico = Medico("Dra. Maria", "987654321", "maria@exemplo.com", endereco_exemplo, "12345678")
    
    assert medico.nome == "Dra. Maria"
    assert medico.crm == "12345678"
