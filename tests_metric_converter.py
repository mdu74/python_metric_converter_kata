import unittest
from metric_converter import MetricConverter

class TestMetricConverter(unittest.TestCase):
    def test_KilometersToMiles_GivenKilometers_ShouldReturnMiles(self):
        distance = {1:0.621371, 2:1.242742, 5:3.106855, 12:7.456452, 20:12.42742}
        for km, miles in distance.items():
            # Arrange
            kilometers = km
            # Act
            result = MetricConverter.KilometersToMiles(kilometers)
            # Assert
            self.assertEqual(result, miles)

    def test_CelsiusToFahrenheit_GivenCelsius_ShouldReturnFahrenheit(self):
        temperature = { 1:33.8, 4:39.2, 10:50, 16:60.8, 22:71.6, 30:86 }
        for c, fahrenheit in temperature.items():
            # Arrange
            celsius = c
            # Act
            result = MetricConverter.CelsiusToFahrenheit(celsius)
            # Assert
            self.assertEqual(result, fahrenheit)