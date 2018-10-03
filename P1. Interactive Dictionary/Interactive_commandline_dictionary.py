import json
# to compensate typing error by user.
from difflib import get_close_matches
# importing the dictonary data.
data = json.load(open("data.json"))

def translate(w):

    # an attempt to make the program user friendly
    w = w.lower()
    if w in data:
        return data[w]

    # if there are similar matches in the dictionary
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " %get_close_matches(w, data.keys())[0])
        if yn == "Y":
            # return the first match key value
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
output = translate(word)

# making multiline outputs more presentable
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
