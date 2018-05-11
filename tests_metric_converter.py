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

    def test_KilogramToPound_GivenKilogram_ShouldReturnPound(self):
        weight = { 1:2.205, 5:11.023, 10:22.046, 13:28.66, 19:41.888, 30:66.139, 35:77.162 }
        for kg, pounds in weight.items():
            # Arrange
            kilogram = kg
            # Act
            result = MetricConverter.KilogramToPound(kilogram)
            # Assert
            self.assertEqual(result, pounds)

    def test_LitersToGallons_GivenLiters_ShouldReturnUSGallons(self):
        volume = { 3.785411784:1, 7.57082:2, 45.4249:12, 75.7082:20, 124.919:33, 223.339:59 }
        for l, gallons in volume.items():
            # Arrange
            liters = l
            targetUnit = "US"
            # Act
            result = MetricConverter.LitersToGallons(liters, targetUnit)
            # Assert
            self.assertEqual(result, gallons)

    def test_LitersToGallons_GivenLiters_ShouldReturnUKGallons(self):
        volume = { 4.54609:1, 9.09218:2, 13.63827:3, 45.4609:10 }
        for l, gallons in volume.items():
            # Arrange
            liters = l
            targetUnit = "UK"
            # Act
            result = MetricConverter.LitersToGallons(liters, targetUnit)
            # Assert
            self.assertEqual(result, gallons)