file = open("data/fruits.txt", "r")

fruits=file.readlines()
file.close

print(fruits)
