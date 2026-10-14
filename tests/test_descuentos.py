from src.descuentos import aplicar_descuento, calcular_descuento, calcular_precio_final, descuento_apilado
import pytest

def test_aplicar_descuento():
    # Arrange
    precio = 100
    porcentaje = 20

    # Act
    resultado = aplicar_descuento(precio, porcentaje)

    # Assert
    assert resultado == 80




def test_calcular_descuento():
    # Arrange
    precio = 200
    porcentaje = 10

    # Act
    resultado = calcular_descuento(precio, porcentaje)

    # Assert
    assert resultado == 20

def test_precio_negativo():
    # Arrange
    precio = -50
    porcentaje = 10

    # Act y Assert
    with pytest.raises(ValueError):
        aplicar_descuento(precio, porcentaje)

def test_calcular_precio_final_con_impuesto():
    # Arrange
    precio = 100
    impuesto = 10
    descuento = 20

    # Act
    resultado = calcular_precio_final(precio, impuesto, descuento)

    # Assert
    assert resultado == 88

def test_descuento_apilado_mayor_al_100():
    # Arrange
    precio = 100
    descuentos = [60, 50]

    # Act y Assert
    with pytest.raises(ValueError):
        descuento_apilado(precio, descuentos)

