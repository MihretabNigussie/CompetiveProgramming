class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        
        def kelvin(celsius):
            return celsius + 273.15
        
        def fahranheit(celsius):
            return celsius * 1.8 + 32
        
        res  = [kelvin(celsius), fahranheit(celsius)]
        
        return res