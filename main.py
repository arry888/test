from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def hello():
    return "helloworld"


@app.route("/add")
def add():
    a = request.args.get("a")
    b = request.args.get("b")
    return a + b


# http://127.0.0.1:5000/add?a=1&b=2

if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=5000)
