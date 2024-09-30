import pytest
from models.medico import Medico
from models.endereco import Endereco

def test_medico_valido():
    endereco = Endereco("Rua A","123","Apto 1","12345-678","Cidade B")
    medico = Medico("Carlos", "4002-8922","carlos@gmail.com",endereco, "654321"
