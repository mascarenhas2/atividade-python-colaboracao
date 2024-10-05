import pytest
from models.endereco import Endereco  # Substitua pelo caminho correto
from models.funcionario import Funcionario  # Substitua pelo caminho correto
from models.medico import Medico  # Substitua pelo caminho correto

# Classe Medico é concreta, então vamos testar diretamente.
@pytest.fixture
def endereco_valido():
    return Endereco("Rua das Flores", "123", "Apto 45", "12345-678", "Cidade Exemplo")

def test_medico_inicializacao_valida(endereco_valido):
    medico = Medico("Dr. João Silva", "999999999", "joao@example.com", endereco_valido, "12345678", 10000.0)
    assert medico.nome == "Dr. João Silva"
    assert medico.telefone == "999999999"
    assert medico.email == "joao@example.com"
    assert medico.endereco == endereco_valido
    assert medico.crm == "12345678"
    assert medico.salario == 10000.0

def test_medico_inicializacao_crm_invalido_tamanho(endereco_valido):
    with pytest.raises(ValueError):
        Medico("Dr. João Silva", "999999999", "joao@example.com", endereco_valido, "1234567", 10000.0)

def test_medico_inicializacao_crm_invalido_numeros(endereco_valido):
    with pytest.raises(ValueError):
        Medico("Dr. João Silva", "999999999", "joao@example.com", endereco_valido, "1234567A", 10000.0)

def test_calcular_salario(endereco_valido):
    medico = Medico("Dr. João Silva", "999999999", "joao@example.com", endereco_valido, "12345678", 10000.0)
    assert medico.calcular_salario() == 10000.0

def test_str_metodo(endereco_valido):
    medico = Medico("Dr. João Silva", "999999999", "joao@example.com", endereco_valido, "12345678", 10000.0)
    assert str(medico) == (
        "Médico: Dr. João Silva\n"
        "Telefone: 999999999\n"
        "CRM: 12345678\n"
        "Email: joao@example.com\n"
        "Endereço: Logradouro: Rua das Flores\n"
        "Número: 123\n"
        "Cidade: Cidade Exemplo\n"
        "CEP: 12345-678, Apto 45\n"
        "Salário: 10000.00"
    )

# Se precisar, adicione mais testes conforme necessário.
