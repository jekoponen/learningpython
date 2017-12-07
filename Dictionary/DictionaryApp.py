import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def wordDefinition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys(), cutoff = 0.75)) > 0:
        match = get_close_matches(word,data.keys())[0]
        print("Did you mean %s instead?" % match)
        stay = "TRUE"
        print("Do you want to continue with %s" % match)
        while stay == "TRUE":
            answer = input("Give Y to continue, N to exit : ")
            if answer == "Y":
                stay = "FALSE"
                return data[match]
            elif answer == "N":
                stay = "FALSE"
                return "Too bad :("
            else:
                print("Unknown input")
    else:
        return "Given word %s is not in dictionary" % inputString


inputString = input("Please enter a word: ")
definitions = wordDefinition(inputString)

if type(definitions) == list:
    for index in definitions:
        print(index)
else:
    print(definitions)
