def stringLenght(string):
    if type(string) == str:
        lenght = len(string)
        return lenght
    else:
        return "Input wasn't string"

#print("Give any string ")
#inputString = input()
inputString = "8720437502983745"

print(stringLenght(inputString))
