from flask import Flask
my_app = Flask(__name__)

@my_app.route('/')
def hello_world():
    return 'Hello, world!'


@my_app.route('/')
def hello_world2():
    return 'Hello, world!!!!'


my_app.run()
