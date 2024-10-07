import pytest
from models.endereco import Endereco  # Supondo que a classe Endereco esteja em um arquivo chamado endereco.py

def test_endereco_inicializacao_valida():  #Teste de validade do endereco
    endereco = Endereco("Rua das Flores", "123", "Apto 45", "12345-678", "Cidade Exemplo")
    assert endereco.logradouro == "Rua das Flores"
    assert endereco.numero == "123"
    assert endereco.complemento == "Apto 45"
    assert endereco.cep == "12345-678"
    assert endereco.cidade == "Cidade Exemplo"

def test_endereco_inicializacao_logradouro_invalido(): #Teste relacionado ao erro do logradouro
    with pytest.raises(ValueError) as excinfo:
        Endereco("R" * 101, "123", "Apto 45", "12345-678", "Cidade Exemplo")
    assert str(excinfo.value) == "O logradouro não pode ter mais de 100 caracteres."

def test_endereco_inicializacao_numero_invalido(): #Teste relacionado ao erro do numero da residência
    with pytest.raises(ValueError) as excinfo:
        Endereco("Rua das Flores", "ABC", "Apto 45", "12345-678", "Cidade Exemplo")
    assert str(excinfo.value) == "O número deve ser um valor numérico."

def test_endereco_inicializacao_cidade_invalida(): #Teste relacionado ao erro da cidade
    with pytest.raises(ValueError) as excinfo:
        Endereco("Rua das Flores", "123", "Apto 45", "12345-678", "C" * 51)
    assert str(excinfo.value) == "A cidade não pode ter mais de 50 caracteres."

def test_validar_cep_valido(): # CEP valido para a realização de testes
    assert Endereco.validar_cep("12345-678") == True

def test_validar_cep_invalido_formato(): #Teste relacionado ao erro do formato do CEP
    assert Endereco.validar_cep("1234-5678") == False
    assert Endereco.validar_cep("12345678") == False
    assert Endereco.validar_cep("12345-67") == False

def test_validar_cep_invalido_numerico(): #Teste relacionado ao erro da digitação de LETRAS no CEP
    assert Endereco.validar_cep("ABCDE-FGH") == False

# TESTE FUNCIONANDO CORRETAMENTE