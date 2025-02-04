import pytest
from calculadora import Calculadora

@pytest.fixture
def calc():
    return Calculadora()

def test_suma(calc):
    assert calc.suma(3, 2) == 5
    assert calc.suma(-1, 1) == 0
    assert calc.suma(0, 0) == 0

def test_resta(calc):
    assert calc.resta(3, 2) == 1
    assert calc.resta(2, 3) == -1
    assert calc.resta(0, 0) == 0

def test_multiplicacion(calc):
    assert calc.multiplicacion(3, 2) == 6
    assert calc.multiplicacion(-1, 1) == -1
    assert calc.multiplicacion(0, 100) == 0

def test_division(calc):
    assert calc.division(6, 2) == 3
    assert calc.division(5, 2) == 2.5
    assert calc.division(0, 1) == 0
    assert calc.division(1, 0) == "Error: División por cero"


