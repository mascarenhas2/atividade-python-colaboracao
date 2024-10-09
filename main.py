import os
os.system("cls || clear")

from projeto.models.endereco import Endereco
from projeto.models.engenheiro import Engenheiro
from projeto.models.medico import Medico

# Função para criar um endereço
def criar_endereco():
    return Endereco("Rua das Flores", "123", "Apto 101", "12345-678", "Salvador")

# Função para criar um engenheiro
def criar_engenheiro(endereco):
    return Engenheiro(
        nome="Andrei Luiz",
        telefone="988112455",
        email="andrei@2232.com",
        crea="12345678",
        endereco=endereco,
        salario=3000.00
    )

# Função para criar um médico
def criar_medico(endereco):
    return Medico(
        nome="Dra. Clara",
        telefone="987654321",
        email="clara@medica.com",
        crm="98765432",
        endereco=endereco,
        salario=5000.00  # Definindo um salário para o médico
    )

# Criar o endereço
endereco = criar_endereco()

# Criar o engenheiro
engenheiro = criar_engenheiro(endereco)

# Validar e imprimir informações do engenheiro
engenheiro.validar_dados()
print(engenheiro)

# Criar o médico
medico = criar_medico(endereco)

# Validar e imprimir informações do médico
medico.validar_dados()
print(medico)
