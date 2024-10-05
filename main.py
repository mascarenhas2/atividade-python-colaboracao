import os
os.system("cls || clear")

from projeto.models.endereco import Endereco
from projeto.models.engenheiro import Engenheiro

# Função para criar um endereço
def criar_endereco():
    return Endereco("Rua das Flores", "123", "Apto 101", "12345-678", "Salvador")

# Função para criar um engenheiro
def criar_engenheiro(endereco):
    return Engenheiro(
        nome="Andrei Luiz",
        telefone="988112455",
        email="andrei@2232.com",
        crea="12345678",  # Adicionando um CREA válido
        endereco=endereco,
        salario=3000.00
    )

# Função para validar as instâncias
def validar_instancias(instancias):
    for instancia in instancias:
        instancia.validar_dados()

# Criar o endereço
endereco = criar_endereco()

# Criar a instância do engenheiro
instancias = [
    criar_engenheiro(endereco)
]

# Validar as instâncias
validar_instancias(instancias)

# Imprimir as informações do engenheiro
for instancia in instancias:
    print(instancia)
