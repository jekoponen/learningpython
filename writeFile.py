file = open("data/numbers.txt","w")
numbers = [1, 2, 3]

for index in numbers:
    if index == len(numbers):
        file.write(str(index))
    else:
        file.write(str(index) + "\n")

file.close()
