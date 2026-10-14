import pytest
import pytest
from src.conversor import (
    celsius_a_fahrenheit,
    fahrenheit_a_celsius,
    celsius_a_kelvin,
    kelvin_a_celsius,
    metros_a_kilometros,
    kilometros_a_metros,
    libras_a_kilogramos,
    kilogramos_a_libras,
    galones_a_litros,
    litros_a_galones,
    millas_a_kilometros,
    kilometros_a_millas,
    pies_a_metros,
    metros_a_pies,
    onzas_a_gramos,
    gramos_a_onzas,
)


def test_kelvin_negativo_debe_lanzar_error():
    kelvin = -10

    with pytest.raises(ValueError):
        kelvin_a_celsius(kelvin)


def test_celsius_a_fahrenheit():
    # Arrange
    celsius = 0

    # Act
    resultado = celsius_a_fahrenheit(celsius)

    # Assert
    assert resultado == 32


def test_fahrenheit_a_celsius():
    # Arrange
    fahrenheit = 212

    # Act
    resultado = fahrenheit_a_celsius(fahrenheit)

    # Assert
    assert resultado == 100


def test_celsius_a_kelvin():
    # Arrange
    celsius = 0

    # Act
    resultado = celsius_a_kelvin(celsius)

    # Assert
    assert resultado == 273.15


def test_metros_a_kilometros():
    # Arrange
    metros = 2000

    # Act
    resultado = metros_a_kilometros(metros)

    # Assert
    assert resultado == 2


def test_libras_a_kilogramos():
    # Arrange
    libras = 10

    # Act
    resultado = libras_a_kilogramos(libras)

    # Assert
    assert resultado == pytest.approx(4.53592)


def test_kilometros_a_metros():
    # Arrange
    kilometros = 3

    # Act
    resultado = kilometros_a_metros(kilometros)

    # Assert
    assert resultado == 3000


def test_kilogramos_a_libras():
    # Arrange
    kilogramos = 5

    # Act
    resultado = kilogramos_a_libras(kilogramos)

    # Assert
    assert resultado == pytest.approx(11.0231, abs=0.001)





def test_galones_a_litros():
    # Arrange
    galones = 2

    # Act
    resultado = galones_a_litros(galones)

    # Assert
    assert resultado == pytest.approx(7.57082)


def test_litros_a_galones():
    # Arrange
    litros = 7

    # Act
    resultado = litros_a_galones(litros)

    # Assert
    assert resultado == pytest.approx(7 / 3.78541)


def test_millas_a_kilometros():
    # Arrange
    millas = 10

    # Act
    resultado = millas_a_kilometros(millas)

    # Assert
    assert resultado == pytest.approx(16.0934)


def test_kelvin_a_celsius():
    kelvin = 273.15

    resultado = kelvin_a_celsius(kelvin)

    assert resultado == pytest.approx(0)


def test_metros_a_kilometros_negativo():
    metros = -100

    with pytest.raises(ValueError):
        metros_a_kilometros(metros)


def test_kilometros_a_metros_negativo():
    kilometros = -2

    with pytest.raises(ValueError):
        kilometros_a_metros(kilometros)


def test_libras_a_kilogramos_negativo():
    libras = -5

    with pytest.raises(ValueError):
        libras_a_kilogramos(libras)


def test_kilogramos_a_libras_negativo():
    kilogramos = -3

    with pytest.raises(ValueError):
        kilogramos_a_libras(kilogramos)


def test_galones_a_litros_negativo():
    galones = -2

    with pytest.raises(ValueError):
        galones_a_litros(galones)


def test_litros_a_galones_negativo():
    litros = -5

    with pytest.raises(ValueError):
        litros_a_galones(litros)


def test_millas_a_kilometros_negativo():
    millas = -10

    with pytest.raises(ValueError):
        millas_a_kilometros(millas)


def test_kilometros_a_millas():
    kilometros = 0

    resultado = kilometros_a_millas(kilometros)

    assert resultado == 0


def test_kilometros_a_millas_negativo():
    kilometros = -5

    with pytest.raises(ValueError):
        kilometros_a_millas(kilometros)


def test_pies_a_metros():
    pies = 10

    resultado = pies_a_metros(pies)

    assert resultado == pytest.approx(3.048)


def test_pies_a_metros_negativo():
    pies = -10

    with pytest.raises(ValueError):
        pies_a_metros(pies)


def test_metros_a_pies():
    metros = 3.048

    resultado = metros_a_pies(metros)

    assert resultado == pytest.approx(10)


def test_metros_a_pies_negativo():
    metros = -3

    with pytest.raises(ValueError):
        metros_a_pies(metros)


def test_onzas_a_gramos():
    onzas = 10

    resultado = onzas_a_gramos(onzas)

    assert resultado == pytest.approx(283.495)


def test_onzas_a_gramos_negativo():
    onzas = -2

    with pytest.raises(ValueError):
        onzas_a_gramos(onzas)


