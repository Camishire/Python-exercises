import pandas

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet =pandas.DataFrame(data)
name_dictionary = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}
print(name_dictionary)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Please enter your name: ")
print ({letter.upper():name_dictionary[letter.upper()] for letter in name if letter.upper() in name_dictionary})

