from crypt import methods
from flask import Flask, request, render_template, make_response

import json

app = Flask(__name__)

@app.route("/") # ถ้าจะใช้คำสั่งนี้ไม่ต้องมี / ก็ได้
def helloworld():
    return "Hello, World!"

@app.route("/name") # ถ้าจะใช้คำสั่งนี้ต้องมี /name
def hellotung(): 
    return "Hello, Tung!"

@app.route("/home", methods=['POST'])
def homefn():
    print('we are in home')

    namein = request.form.get('fname')
    lastname = request.form.get('lname')
    print(namein)
    print(lastnamein)
    return render_template("home.html",name='namein')

if __name__ == "__main__": # ต้อง IP VM เราแล้วตามด้วย :5001
    app.run(host='0.0.0.0' ,debug=True,port=5001) #0.0.0.0 คือเข้าได้ในอินเตอร์เน็ท