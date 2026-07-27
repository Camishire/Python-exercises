from tkinter import *

window = Tk()
window.title("My GUI program")
window.minsize(500, 300)

# Label
my_label = Label( text="Hello World", font=("Arial", 25, "bold") )
my_label.pack()

def button_clicked():
    if my_label["text"] == "Hello World":
        my_label.configure(text="Button Clicked")
    elif my_label["text"] == "Button Clicked":
        my_label.configure(text="Hello World")


def button_clicked1():
    print("Button Clicked")
    new_text = input.get()
    my_label.configure(text=new_text)

input = Entry(width=40)
#button = Button(text="Click me", command=button_clicked)
button = Button(text="Click me", command=button_clicked1)
button.pack()
input.pack()

window.mainloop()