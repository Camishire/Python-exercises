from question_model import Question
from quiz_brain import QuizBrain
import requests
from ui import QuizInterface

url = "https://opentdb.com/api.php?amount=10&category=15&difficulty=easy&type=boolean"
data = requests.get(url)
data = data.json()["results"]

question_bank = []
for question in data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")