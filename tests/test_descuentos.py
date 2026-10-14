from src.descuentos import (
    aplicar_descuento,
    calcular_descuento,
    calcular_precio_final,
    descuento_apilado,
    descuento_por_volumen,
    descuento_cumulativo,
)
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

def test_aplicar_descuento_porcentaje_negativo():
    porcentaje = -10
    precio = 100

    with pytest.raises(ValueError):
        aplicar_descuento(precio, porcentaje)


def test_aplicar_descuento_porcentaje_mayor_a_cien():
    precio = 100
    porcentaje = 110

    with pytest.raises(ValueError):
        aplicar_descuento(precio, porcentaje)


def test_aplicar_descuento_cien_por_ciento():
    precio = 150
    porcentaje = 100

    resultado = aplicar_descuento(precio, porcentaje)

    assert resultado == 0


def test_calcular_descuento_precio_negativo():
    precio = -20
    porcentaje = 10

    with pytest.raises(ValueError):
        calcular_descuento(precio, porcentaje)


def test_calcular_descuento_porcentaje_invalido():
    precio = 100
    porcentaje = 110

    with pytest.raises(ValueError):
        calcular_descuento(precio, porcentaje)


def test_precio_final_precio_negativo():
    precio = -100
    impuesto = 10
    descuento = 20

    with pytest.raises(ValueError):
        calcular_precio_final(precio, impuesto, descuento)


def test_precio_final_impuesto_negativo():
    precio = 100
    impuesto = -5
    descuento = 20

    with pytest.raises(ValueError):
        calcular_precio_final(precio, impuesto, descuento)


def test_precio_final_descuento_invalido():
    precio = 100
    impuesto = 10
    descuento = 110

    with pytest.raises(ValueError):
        calcular_precio_final(precio, impuesto, descuento)


def test_descuento_volumen_sin_descuento():
    cantidad = 5
    precio_unitario = 100

    resultado = descuento_por_volumen(cantidad, precio_unitario)

    assert resultado == 500


def test_descuento_volumen_cinco_por_ciento():
    cantidad = 10
    precio_unitario = 100

    resultado = descuento_por_volumen(cantidad, precio_unitario)

    assert resultado == 950


def test_descuento_cumulativo_una_aplicacion():
    precio = 500
    descuentos = [15]

    resultado = descuento_cumulativo(precio, descuentos)

    assert resultado == 425


def test_descuento_cumulativo_tres_aplicaciones():
    precio = 1000
    descuentos = [10, 10, 10]

    resultado = descuento_cumulativo(precio, descuentos)

    assert resultado == pytest.approx(729)


def test_descuento_cumulativo_lista_vacia():
    precio = 350
    descuentos = []

    resultado = descuento_cumulativo(precio, descuentos)

    assert resultado == 350


def test_descuento_cumulativo_descuento_negativo():
    precio = 200
    descuentos = [10, -5]

    with pytest.raises(ValueError):
        descuento_cumulativo(precio, descuentos)


def test_descuento_cumulativo_descuento_superior_al_limite():
    precio = 200
    descuentos = [10, 101]

    with pytest.raises(ValueError):
        descuento_cumulativo(precio, descuentos)


def test_descuento_apilado_lista_vacia():
    precio = 400
    descuentos = []

    resultado = descuento_apilado(precio, descuentos)

    assert resultado == 400


def test_descuento_apilado_un_descuento():
    precio = 300
    descuentos = [20]

    resultado = descuento_apilado(precio, descuentos)

    assert resultado == 240

