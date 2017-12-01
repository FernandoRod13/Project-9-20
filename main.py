from flask import Flask, jsonify, request
from handler.resources import ResourceHandler
#from handler. import SupplierHandler

app = Flask(__name__)

@app.route('/')
def local():
    return 'Welcome to Project 9-20!'

@app.route('/resources/requested')
def getAllResourceRequested(self):
    return ResourceHandler.getAllresources_requested()

@app.route('/resources/avalible')
def getAllResourceAvalible(self):
    return ResourceHandler.getAllresources_avaliable()

# @app.route('/Project9-20/parts')
# def getAllParts():
#     if not request.args:
#         return PartHandler().getAllParts()
#     else:
#         return PartHandler().searchParts(request.args)

# @app.route('/Project9-20/parts/<int:pid>')
# def getPartById(pid):
#     return PartHandler().getPartById(pid)

# @app.route('/Project9-20/parts/<int:pid>/suppliers')
# def getSuppliersByPartId(pid):
#     return PartHandler().getSuppliersByPartId(pid)

# @app.route('/Project9-20/suppliers')
# def getAllSuppliers():
#     if not request.args:
#         return SupplierHandler().getAllSuppliers()
#     else:
#         return SupplierHandler().searchSuppliers(request.args)

# @app.route('/Project9-20/suppliers/<int:sid>')
# def getSupplierById(sid):
#     return SupplierHandler().getSupplierById(sid)

# @app.route('/Project9-20/suppliers/<int:sid>/parts')
# def getPartsBySuplierId(sid):
#     return SupplierHandler().getPartsBySupplierId(sid)

if __name__ == '__main__':
    app.run()