import pytest
from src.conversor import celsius_a_fahrenheit, fahrenheit_a_celsius, celsius_a_kelvin, metros_a_kilometros, libras_a_kilogramos, kilometros_a_metros, kilogramos_a_libras, galones_a_litros, litros_a_galones, millas_a_kilometros


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

