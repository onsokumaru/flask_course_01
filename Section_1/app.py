from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/hithere')
def hi_there_everyone():
    return "I just hit /hithere"

@app.route('/add_two_nums', methods=["POST"])
def add_two_nums():
    #get x,y from posted data
    dataDict = request.get_json()
    x = dataDict["x"]
    y = dataDict["y"]
    #add z=x+y
    z = x + y

    #prepare a json, "z":z
    retJson = {
        "z":z
    }

    #return jsonify(map_prepared)
    return jsonify(retJson), 200

@app.route('/bye')
def bye():
    #prepare response for request that came to bye
    age = 42
    #c = 1/0
    retJson = {
        'Name':'Mike',
        'Age': age,
        "phones":[
            {
                "phoneName":"Iphone5",
                "phoneNumber":1111111
            },
            {
                "phoneName":"Samsung Galaxy Note",
                "phoneNumber":2222222
            }
        ]
    }
    return jsonify(retJson)

if __name__ == "__main__":
    app.run(debug=True)
