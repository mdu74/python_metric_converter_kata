import unittest
from metric_converter import MetricConverter

class TestMetricConverter(unittest.TestCase):
    def test_KilometersToMiles_GivenKilometer_ShouldReturnMiles(self):
        kilometers = {1:0.621371, 2:1.242742, 5:3.106855, 12:7.456452, 20:12.42742}
        for km, miles in kilometers.items():
            # Arrange
            kilometer = km
            # Act
            result = MetricConverter.KilometersToMiles(kilometer)
            # Assert
            self.assertEqual(result, miles)