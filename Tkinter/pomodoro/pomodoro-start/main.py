from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global completed_sesh_counter, timer
    if timer is not None:
        window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    completed_sessions.config(text="")
    completed_sesh_counter = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    timer_label.config(text="Work")
    count_down(WORK_MIN * 60)

def start_short_break():
    timer_label.config(text="Short Break")
    count_down(SHORT_BREAK_MIN * 60)

def start_long_break():
    timer_label.config(text="Long Break")
    count_down(LONG_BREAK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
timer = None
completed_sesh_counter = 0

def count_down(count):
    global timer, completed_sesh_counter
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds:02d}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        completed_sesh_counter += 1
        if completed_sesh_counter % 4 == 0:
            add_checkmark()
            start_long_break()
        else:
            add_checkmark()
            start_short_break()

def add_checkmark():
    compl = "✅" * (completed_sesh_counter % 4 or 4)
    completed_sessions.config(text=compl)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.configure(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer")
timer_label.config(fg=GREEN, background=YELLOW, font=(FONT_NAME, 25, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

completed_sessions = Label(bg=YELLOW, font=(FONT_NAME, 25, "bold"))
completed_sessions.grid(column=1, row=3)

window.mainloop()