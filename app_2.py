from flask import Flask

app = Flask(__name__)

@app.route('/')
def name():
    name = input("What is your name? ")
    return print(name)
