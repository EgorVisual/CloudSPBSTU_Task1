from crypt import methods
from flask import Flask
from flask import request

app = Flask(__name__)

list = {'Egor':186,'Artem':175,'Arseniy':179}

@app.route("/helloserverget", methods=['GET'])
def hello_world():
    return "Lenght of the list: {len(list.keys())}\n {list} \n"

@app.route("/helloservergetlist/<string:name>", methods=['GET'])
def hello_world_num(name):
    if name in list.keys():
        return f"Your choise:\n {name} : {list[name]}\n"
    return "Person not found."

@app.route("/helloserverput", methods=['PUT'])
def hello_world_put():
    name = str(request.form['name'])
    height = int(request.form['height'])
    if name in lit.keys():
        list[name] = height
        return f"Person's height was changed: {name} : {list[name]}\n"
    else:
        return "Person not found!"
    return f"We get ahother request ({request.method})\n"

@app.route("/helloserverpost", methods=['GET','POST'])
def hello_world_post():
    name = str(request.form['name'])
    height = int(request.form['height'])
    if name in lit.keys():
        return "This person already in the list!\n"
    else:
        list[name] = height
        return "Person: {name} with height: {list[name]} was created!\n"
    return f"We get {request.method} request.\n"

app.run(host='0.0.0.0', port=5000)