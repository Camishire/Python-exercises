from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.configure(padx=20, pady=20)

def miles_to_km():
    miles=float(miles_input.get())
    km = miles * 1.609
    kilometer_results_label.config(text=f"{km}")

miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)

miles_label = Label(window, text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = Label(window, text="is equal to: ")
miles_label.grid(row=1, column=0)

kilometer_label = Label(window, text="Km: ")
kilometer_label.grid(row=1, column=2)

kilometer_results_label = Label(window, text="0")
kilometer_results_label.grid(row=1, column=1)

calculate_button = Button(window, text="Calculate", command=miles_to_km)
calculate_button.grid(row=2, column=1)



window.mainloop()