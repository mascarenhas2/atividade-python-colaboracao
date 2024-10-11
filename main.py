import os
os.system("cls || clear")

from projeto.models.endereco import Endereco
from projeto.models.engenheiro import Engenheiro
from projeto.models.medico import Medico

# Função para criar um endereço
def criar_endereco_engenheiro():
    return Endereco("Rua Paracaina", "250", "|casa 145", "54321-678", "Salvador")

def criar_endereco_medico():
    return Endereco("Liberdade", "78", "|Apartamento 5B", "12345-678", "Salvador")

# Função para criar um engenheiro
def criar_engenheiro(endereco):
    return Engenheiro(
        nome="Andrei Luiz de Jesus Souza Almeida",
        telefone="988112455",
        email="andrei@2232.com",
        crea="45488778",
        endereco=endereco,
        salario=6815.10
    )

# Função para criar um médico
def criar_medico(endereco):
    return Medico(
        nome="Dra. Clara",
        telefone="987654321",
        email="clara@medica.com",
        crm="98765432",
        endereco=endereco,
        salario=8512.20
    )

# Criar o endereço para o engenheiro
endereco_engenheiro = criar_endereco_engenheiro()
# Criar o engenheiro
engenheiro = criar_engenheiro(endereco_engenheiro)

# Validar e imprimir informações do engenheiro
engenheiro.validar_dados()
print(engenheiro)

# Criar o endereço para o médico
endereco_medico = criar_endereco_medico()
# Criar o médico
medico = criar_medico(endereco_medico)

# Validar e imprimir informações do médico
medico.validar_dados()
print(medico)
