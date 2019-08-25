import json
from difflib import get_close_matches


data = json.load(open("data.json"))


def search(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:  # in case user enters words like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:

        yn = input("Did you mean %s instead? Enter Y for yes or N for no: " %
                   get_close_matches(word, data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == 'N':
            return "The word doesnt exist, double check it."
        else:
            return "We cannot process your request!"
    else:
        print("The word doesnt exist, double check it.")


word = input("Enter a word: ")

output = search(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
