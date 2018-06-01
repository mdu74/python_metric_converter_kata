class MetricCalculator:
    def CalculateFahrenheitFrom(celsius):
        return (celsius * 1.8) + 32

    def CalculateMilesFrom(kilometers):
        calculateMiles = kilometers * 0.621371  
        miles = round(calculateMiles,6)  
        return miles

    def CalculatePoundsFrom(kilogram):
        calculatePounds = kilogram / 0.45359237
        pounds = round(calculatePounds,3)
        return pounds
        
    def CalculateUSGallonsFrom(liters):
        return liters / 3.785411784

    def CalculateUKGallonsFrom(liters):
        return liters / 4.54609