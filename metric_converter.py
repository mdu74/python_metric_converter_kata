class MetricConverter(object):
    def KilometersToMiles(kilometers):
        calculateMiles = kilometers * 0.621371  
        miles = round(calculateMiles,6)  
            
        return miles
    
    def CelsiusToFahrenheit(celsius): 
        fahrenheit = (celsius * 1.8) + 32
        return fahrenheit