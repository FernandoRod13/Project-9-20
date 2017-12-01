from flask import Flask, jsonify
from handler.resources import ResourcesHandler


app = Flask(__name__)

@app.route('/')
def local():
    return 'Welcome to Project 9-20!'

@app.route('/resources/requested')
def getAllResourcesRequested():
    return ResourcesHandler.getAllresources_requested()

@app.route('/resources/avalible')
def getAllResourcesRequested():
    return ResourcesHandler.getAllresources_avaible()

if __name__ == '__main__':
    app.run()
