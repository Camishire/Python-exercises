import tkinter
from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain

        self.window = tkinter.Tk()
        self.window.title("Quiz")
        self.window.geometry("400x600")
        self.window.minsize(600, 800)
        self.window.config(background=THEME_COLOR, padx=100, pady=100)

        self.question_window = Canvas(self.window, width=300, height=250, background="white", highlightthickness=0)
        self.question_text = self.question_window.create_text(
            150, 125, text="Some Question Text", width=250, font=("Arial", 20, "italic")
        )
        self.question_window.grid(row=0, column=0, columnspan=2, pady=50)

        self.right_answer_image = PhotoImage(file="images/true.png")
        right_answer_button = Button(image=self.right_answer_image, highlightthickness=0, command=self.true_pressed)
        right_answer_button.grid(row=1, column=1)

        self.wrong_answer_image = PhotoImage(file="images/false.png")
        wrong_answer_button = Button(image=self.wrong_answer_image, highlightthickness=0, command=self.false_pressed)
        wrong_answer_button.grid(row=1, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.question_window.itemconfig(self.question_text, text=question_text)
        else:
            self.question_window.itemconfig(self.question_text, text="You've completed the quiz!")

    def true_pressed(self):
        self.check_answer("True")

    def false_pressed(self):
        self.check_answer("False")

    def check_answer(self, user_answer):
        self.quiz.check_answer(user_answer)
        self.get_next_question()