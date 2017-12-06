file = open("data/fruits.txt", "r")

fruits=file.readlines()
fruits=[i.rstrip("\n") for i in fruits]
file.close

for i in fruits:
    print(len(i))
