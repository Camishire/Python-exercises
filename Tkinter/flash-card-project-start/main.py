from tkinter import *
import pandas as pd
import random
import json
import os

BACKGROUND_COLOR = "#B1DDC6"

LANGUAGE_FONT = ("Arial", 40, "italic")
LANGUAGE_FONT_POS = (400, 150)
MEANING_FONT = ("Arial", 60, "bold")
MEANING_FONT_POS = (400, 263)

window = Tk()
window.title("Flash cards")
window.configure(background=BACKGROUND_COLOR, padx=20, pady=20)
window.geometry("1050x726")
window.resizable(0, 0)

card_img_back = PhotoImage(file="images/card_back.png")
card_img_front = PhotoImage(file="images/card_front.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=card_img_front)

canvas_language_text = canvas.create_text(*LANGUAGE_FONT_POS, text="", font=LANGUAGE_FONT)
canvas_meaning_text = canvas.create_text(*MEANING_FONT_POS, text="", font=MEANING_FONT)

canvas.grid(row=0, column=1)


def read_data():
    df = pd.read_csv("data/french_words.csv", usecols=['French', 'English'])
    return df.to_dict(orient='records')

def load_words():
    if os.path.exists('data/words_to_learn.json'):
        with open('data/words_to_learn.json', 'r') as fp:
            return json.load(fp)
    else:
        return read_data()

def save_data(words):
    with open('data/words_to_learn.json', 'w') as fp:
        json.dump(words, fp, indent=4)


words = load_words()
current_card = {}
flip_timer = None


def next_card():
    global current_card, flip_timer
    if flip_timer is not None:
        window.after_cancel(flip_timer)

    current_card = random.choice(words)
    canvas.itemconfig(card_background, image=card_img_front)
    canvas.itemconfig(canvas_language_text,text="French")
    canvas.itemconfig(canvas_meaning_text, text=current_card["French"])

    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_background, image=card_img_back)
    canvas.itemconfig(canvas_language_text, text="English")
    canvas.itemconfig(canvas_meaning_text, text=current_card["English"])


def pressed_right():
    words.remove(current_card)
    if len(words) == 0:
        ending_screen()
    else:
        save_data(words)
        next_card()

def pressed_wrong():
    next_card()

def ending_screen():
    canvas.itemconfig(card_background, image=card_img_front)
    canvas.itemconfig(canvas_language_text, text="You did it! :)")
    canvas.itemconfig(canvas_meaning_text, text="Yay!")
    button_right_img["state"] = "disabled"
    button_wrong_img["state"] = "disabled"


button_right_img = PhotoImage(file="images/right.png")
button_right_btn = Button(image=button_right_img, highlightthickness=0, command=pressed_right)
button_right_btn.grid(row=1, column=2)

button_wrong_img = PhotoImage(file="images/wrong.png")
button_wrong_btn = Button(image=button_wrong_img, highlightthickness=0, command=pressed_wrong)
button_wrong_btn.grid(row=1, column=0)

next_card()

window.mainloop()