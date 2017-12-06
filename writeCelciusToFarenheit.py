temperatures=[10,-20,-289,100]
def cels_to_farh(celsius):
    farenheit = celsius * 9/5 + 32
    return farenheit

file = open("data/temperatures.txt", "w")
for i in temperatures:
    if i > -273.15:
        file.write(str(cels_to_farh(i)) + "\n")
file.close()
