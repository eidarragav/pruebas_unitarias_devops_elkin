import pytest
from src.conversor import celsius_a_fahrenheit, fahrenheit_a_celsius, celsius_a_kelvin, metros_a_kilometros, libras_a_kilogramos


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

