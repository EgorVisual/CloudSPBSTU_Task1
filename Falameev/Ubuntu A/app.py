from crypt import methods
from flask import Flask

app = Flask(__name__)

@app.route("/helloserverget", methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/helloserverput", methods=['PUT'])
def hello_world_put():
    return "<p>Hello, World!</p>"

@app.route("/helloserverpost", methods=['POST'])
def hello_world_post():
    return "<p>Hello, World!</p>"

app.run(host='0.0.0.0', port=5000)