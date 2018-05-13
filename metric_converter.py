from metric_calculator import MetricCalculator

class MetricConverter(object):
    def KilometersToMiles(kilometers):
        miles = MetricCalculator.CalculateMilesFrom(kilometers)          
        return miles
    
    def CelsiusToFahrenheit(celsius): 
        fahrenheit = MetricCalculator.CalculateFahrenheitFrom(celsius)
        return fahrenheit
    
    def KilogramToPound(kilogram): 
        pounds = MetricCalculator.CalculatePoundsFrom(kilogram)
        return pounds
    
    def LitersToGallons(liters, targetUnit):
        if targetUnit == "US":
            calculateGallons = MetricCalculator.CalculateUSGallonsFrom(liters)
        if targetUnit == "UK":
            calculateGallons = MetricCalculator.CalculateUKGallonsFrom(liters)
        
        gallons = round(calculateGallons)
        return gallons