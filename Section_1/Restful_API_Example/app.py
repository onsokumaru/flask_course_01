from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def checkPosteddata(postedData, functionName):
    if(functionName == "add"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200


class Add(Resource):
    def post(self):
        #if I'm here then the resoruce was requested using the method POST

        #step 1: get POSTed data
        postedData = request.get_json()

        #step 1b: verify validity of posted data
        status_code = checkPosteddata(postedData, "add")
        if(status_code != 200):
            retJson = {
                "Message" : "An Error happened",
                "Status Code" : status_code
            }
            return jsonify(retJson)
        #if i'm here the status code was 200

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)

        # step 2: add poseted date
        sumToReturn = x + y
        retMap = {
            'Message' : sumToReturn,
            'Status Code' : 200
        }
        return jsonify(retMap)

class Subtract(Resource):
    pass

class Multiply(Resource):
    pass

class Divide(Resource):
    pass

api.add_resource(Add, "/add")

@app.route('/')
def hello_world():
    return "Hello World!"


if __name__=="_main":
    app.run(debug=True)
