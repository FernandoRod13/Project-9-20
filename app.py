from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def local():
    return 'Welcome to Project 9-20!'


if __name__ == '__main__':
    app.run()
