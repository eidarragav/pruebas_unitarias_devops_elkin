from src.calculadora import sumar, dividir, potencia, maximo, promedio
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





