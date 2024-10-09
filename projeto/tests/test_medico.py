import pytest
from projeto.models.endereco import Endereco  # Certifique-se de que este caminho esteja correto
from projeto.models.medico import Medico  # Certifique-se de que este caminho esteja correto

@pytest.fixture
def endereco_valido():  # Definindo o endereco correto
    return Endereco("Rua das Flores", "123", "Apto 45", "12345-678", "Cidade Exemplo")

def test_medico_inicializacao_valida(endereco_valido):  # Teste de validade do endereco
    medico = Medico("Dr. João Silva", "999999999", "joao@example.com", endereco_valido, "12345678", 10000.0)
    assert medico.nome == "Dr. João Silva"
    assert medico.telefone == "999999999"
    assert medico.email == "joao@example.com"
    assert medico.endereco == endereco_valido
    assert medico.crm == "12345678"
    assert medico.salario == 10000.0

def test_medico_inicializacao_crm_invalido_tamanho(endereco_valido):  # Teste relacionado ao erro do tamanho do CRM inválido
    with pytest.raises(ValueError):
        Medico("Dr. João Silva", "999999999", "joao@example.com", endereco_valido, "1234567", 10000.0)

def test_medico_inicializacao_crm_invalido_numeros(endereco_valido):  # Teste relacionado ao erro da compatibilidade do CRM
    with pytest.raises(ValueError):
        Medico("Dr. João Silva", "999999999", "joao@example.com", endereco_valido, "1234567A", 10000.0)

def test_calcular_salario_medico(endereco_valido):  # Teste de cálculo de salário
    medico = Medico("Dr. João Silva", "999999999", "joao@example.com", endereco_valido, "12345678", 10000.0)
    assert medico.calcular_salario() == 10000.0

