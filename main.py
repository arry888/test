from flask import Flask
from flask import request
from flask import render_template

import users as db
# 123
app = Flask(__name__)

@app.route("/")
def hello():
    user_list = db.select_user()
    return render_template("index.html", user_list=user_list)
    #return render_template("index.html")

@app.route("/select")
def select():

   return str(db.select_user())

@app.route("/delete")
def deleteUser():
  name= request.args.get("name")
  db.delect_user(name)
  return '删除成功'
# @app.route("/add")
# def add():
#     a = request.args.get("a")
#     b = request.args.get("b")
#     return a + b

@app.route("/addUser")
def add():
    name = request.args.get("name")
    mail = request.args.get("mail")
    age = request.args.get("age")
    db.add_user(name, mail, age)
    return '添加成功'




# http://127.0.0.1:5000/add?a=1&b=2

if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=5000)
