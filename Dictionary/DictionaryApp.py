import json
import sys
from difflib import get_close_matches

data = json.load(open(sys.path[0] + "\data.json"))

def wordDefinition(word):
    word = word.lower()
    if word in data:        #seek in lowcase, most of the words
        return data[word]
    elif word.upper() in data:  #seek in uppercas, some appreveviation like USA,NATO
        return data[word.upper()]
    elif word.title() in data:      #seek as Title, names, cities, countries etc.
        return data[word.title()]
    elif len(get_close_matches(word,data.keys(), cutoff = 0.75)) > 0:    #search close values for input
        match = get_close_matches(word,data.keys())[0]     #select the closet one
        print("Did you mean %s instead?" % match)
        stay = "TRUE"
        print("Do you want to continue with %s" % match)
        while stay == "TRUE":                  #ask while user gives accepted answer     
            answer = input("Give Y to continue, N to exit : ")
            if answer == "Y":
                stay = "FALSE"
                return data[match]
            elif answer == "N":
                stay = "FALSE"
                return "Given word %s is not in dictionary" % inputString
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
