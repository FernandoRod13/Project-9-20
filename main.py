from flask import Flask, jsonify
from handler.resources import ResourcesHandler

app = Flask(__name__)

@app.route('/')
def local():
    return 'Welcome to Project 9-20!'

@app.route('/resources')
def getAllresources():
    handler = ResourcesHandler()
    return handler.getAllresources()

@app.route('/resources/requested')
def getAllResourcesRequested():
    handler = ResourcesHandler()
    return handler.getAllresources_requested()

@app.route('/resources/avaliable')
def getAllResourcesAvailable():
    handler = ResourcesHandler()
    return handler.getAllresources_avaliable()


if __name__ == '__main__':
    app.run()
