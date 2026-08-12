from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

# @app.route('/username/<name>')
# def username(name):
#     return f'Hello, {name}!'

# @app.route('/<name>')
# def hello_name(name):
#     return f'Hello, {name}!'

# @app.route('/username/<path:name>') #http://127.0.0.1:5000/username/kamile/1
# def hello_name(name):
#     return f'Hello, {name}!' # Hello, kamile/1!

# @app.route('/username/<name>/<int:number>')
# def hello_name(name, number):
#     return f'Hello, {name}! You are {number} years old.'

@app.route('/bye')
@make_bold
@make_emphasis
def bye():
    return 'Bye!'


if __name__ == '__main__':
    app.run()
