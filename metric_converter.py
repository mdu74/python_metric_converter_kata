from metric_calculator import MetricCalculator

class MetricConverter(object):
    def KilometersToMiles(kilometers):
        if kilometers == None or isinstance(kilometers, str):
            return 0

        miles = MetricCalculator.CalculateMilesFrom(kilometers)          
        return miles
    
    def CelsiusToFahrenheit(celsius): 
        if celsius == None or isinstance(celsius, str):
            return 0

        fahrenheit = MetricCalculator.CalculateFahrenheitFrom(celsius)
        return fahrenheit
    
    def KilogramToPound(kilogram): 
        if kilogram == None or isinstance(kilogram, str):
            return 0

        pounds = MetricCalculator.CalculatePoundsFrom(kilogram)
        return pounds
    
    def LitersToGallons(liters, targetUnit):
        if liters == None or isinstance(liters, str):
            return 0

        if targetUnit == "US":
            calculateGallons = MetricCalculator.CalculateUSGallonsFrom(liters)
        if targetUnit == "UK":
            calculateGallons = MetricCalculator.CalculateUKGallonsFrom(liters)
        
        gallons = round(calculateGallons)
        return gallons