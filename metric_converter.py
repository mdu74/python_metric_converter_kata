from metric_calculation import MetricCalculator
from metric_validation import MetricInputValidator

class MetricConverter():
    def KilometersToMiles(kilometers):
        if MetricInputValidator.MetricIsNullOrStringFrom(kilometers):
            return 0

        miles = MetricCalculator.CalculateMilesFrom(kilometers)          
        return miles
    
    def CelsiusToFahrenheit(celsius): 
        if MetricInputValidator.MetricIsNullOrStringFrom(celsius):
            return 0

        fahrenheit = MetricCalculator.CalculateFahrenheitFrom(celsius)
        return fahrenheit
    
    def KilogramToPound(kilogram): 
        if MetricInputValidator.MetricIsNullOrStringFrom(kilogram):
            return 0

        pounds = MetricCalculator.CalculatePoundsFrom(kilogram)
        return pounds
    
    def LitersToGallons(liters, targetUnit):
        if MetricInputValidator.MetricIsNullOrStringFrom(liters):
            return 0

        if targetUnit == "US":
            calculateGallons = MetricCalculator.CalculateUSGallonsFrom(liters)
        if targetUnit == "UK":
            calculateGallons = MetricCalculator.CalculateUKGallonsFrom(liters)
        
        gallons = round(calculateGallons)
        return gallons