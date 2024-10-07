import pytest
from models.funcionario import Funcionario  # Substitua pelo caminho correto
from models.endereco import Endereco  # Substitua pelo caminho correto
from models.engenheiro import Engenheiro  # Supondo que a classe Engenheiro esteja em models.engenheiro.py

@pytest.fixture
def endereco_valido(): #Teste de validade do endereco
    return Endereco("Rua das Flores", "123", "Apto 45", "12345-678", "Cidade Exemplo")


def test_engenheiro_inicializacao_crea_vazio(endereco_valido): #Teste relacionado ao erro do CREA vazio
    with pytest.raises(ValueError):
        Engenheiro("João Silva", "9999-9999", "", "joao@example.com", endereco_valido, 5000.0)

def test_engenheiro_inicializacao_crea_incorreto_tamanho(endereco_valido): #Teste relacionado ao tamanho incorreto do CREA
    with pytest.raises(ValueError):
        Engenheiro("João Silva", "9999-9999", "123456", "joao@example.com", endereco_valido, 5000.0)

def test_engenheiro_inicializacao_crea_incorreto_numeros(endereco_valido): #Teste relacionado a compatibilidade dos numeros do CREA
    with pytest.raises(ValueError):
        Engenheiro("João Silva", "9999-9999", "1234567A", "joao@example.com", endereco_valido, 5000.0)


# TESTE FUNCIONANDO CORRETAMENTE