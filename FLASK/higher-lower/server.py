from flask import Flask
app = Flask(__name__)
import random

random_number = random.randint(0, 9)

@app.route('/')
def home():
    return ('<h1>Guess a number between 0 and 9 </h1>'
            '<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>')

@app.route('/<int:number>')
def guess_number(number):
    if number < random_number:
        return '<h1>Number is too low!</h1>'
    elif number > random_number:
        return '<h1>Number is too high!</h1>'
    else:
        return '<h1>Number is correct!</h1>'


if __name__ == '__main__':
    app.run()