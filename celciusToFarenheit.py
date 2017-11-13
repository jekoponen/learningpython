def convertCelsius(Celsius):
    if Celsius < -273.15:
        return "Given temperature below absolute zero"
    else:
        Farenheith = Celsius * 9/5 + 32
        return Farenheith

print("Give temperature ")
C = float(input())
print(convertCelsius(C))
