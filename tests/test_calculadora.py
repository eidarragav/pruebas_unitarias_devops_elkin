from src.calculadora import (
    sumar, restar, multiplicar, dividir, potencia,
    raiz_cuadrada, maximo, minimo, promedio,
    calcular_area_rectangulo, calcular_perimetro_rectangulo
)
import pytest

def test_sumar_positivos():
	# Arrange
	a, b = 7, 5
	# Act
	resultado = sumar(a, b)
	# Assert
	assert resultado == 12

def test_dividir_por_cero_lanza_error():
	with pytest.raises(ValueError):
		dividir(10, 0)

def test_potencia():
	#Arrange
	c, d = 3, 2
	#Act
	potencia_resultado = potencia(3,2)
	#Assert
	assert potencia_resultado == 9



def test_probar_maximo():
	#Arrange
	lista =  [3,4,5,7,9,10,20]
	#Act
	resultado = maximo(lista)
	#Assert
	assert resultado == 20

def test_promedio():
	#Arrange
	lista = [1,8,4,5,8,10]
	#Act
	resultado = promedio(lista)
	#Assert
	assert resultado == 6

def test_sumar_negativos():
    # Arrange
    a, b = -4, -6

    # Act
    resultado = sumar(a, b)

    # Assert
    assert resultado == -10


def test_restar():
    # Arrange
    a, b = 10, 4

    # Act
    resultado = restar(a, b)

    # Assert
    assert resultado == 6


def test_multiplicar():
    # Arrange
    a, b = 5, 4

    # Act
    resultado = multiplicar(a, b)

    # Assert
    assert resultado == 20


def test_dividir_correctamente():
    # Arrange
    a, b = 15, 3

    # Act
    resultado = dividir(a, b)

    # Assert
    assert resultado == 5


def test_potencia_exponente_cero():
    # Arrange
    base, exponente = 8, 0

    # Act
    resultado = potencia(base, exponente)

    # Assert
    assert resultado == 1


def test_raiz_cuadrada():
    # Arrange
    numero = 25

    # Act
    resultado = raiz_cuadrada(numero)

    # Assert
    assert resultado == 5


def test_promedio_lista_vacia():
    # Arrange
    lista = []

    # Act y Assert
    with pytest.raises(ValueError):
        promedio(lista)


def test_maximo_lista_negativa():
    # Arrange
    lista = [-8, -3, -10]

    # Act
    resultado = maximo(lista)

    # Assert
    assert resultado == -3


def test_minimo_lista():
    # Arrange
    lista = [-5, -2, -9]

    # Act
    resultado = minimo(lista)

    # Assert
    assert resultado == -9


def test_minimo_lista_positiva():
    # Arrange
    lista = [3, 7, 2, 9]

    # Act
    resultado = minimo(lista)

    # Assert
    assert resultado == 2


def test_area_rectangulo():
    # Arrange
    base, altura = 5, 4

    # Act
    resultado = calcular_area_rectangulo(base, altura)

    # Assert
    assert resultado == 20


def test_area_rectangulo_base_negativa():
    # Arrange
    base, altura = -5, 4

    # Act y Assert
    with pytest.raises(ValueError):
        calcular_area_rectangulo(base, altura)


def test_perimetro_rectangulo():
    # Arrange
    base, altura = 5, 4

    # Act
    resultado = calcular_perimetro_rectangulo(base, altura)

    # Assert
    assert resultado == 18


def test_perimetro_rectangulo_altura_negativa():
    # Arrange
    base, altura = 5, -4

    # Act y Assert
    with pytest.raises(ValueError):
        calcular_perimetro_rectangulo(base, altura)



