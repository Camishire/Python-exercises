#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

import os
os.makedirs("ReadyToSend", exist_ok=True)

names = []
with open("Input/Names/invited_names.txt") as f:
    for line in f:
        names.append(line.strip())

with open("Input/Letters/starting_letter.txt") as f:
    letter_template = f.read()

for name in names:
    new_letter = letter_template.replace("[name]", name)
    with open(f"ReadyToSend/letter_for_{name}.txt", "w") as f:
        f.write(new_letter)