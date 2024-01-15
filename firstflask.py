from flask import Flask, request, render_template, make_response

import json

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello, World!"

@app.route("/name")
def helloworld():
    return "Hello, Tung!"

if __name__ == "__main__":
    app.run(host='0.0.0.0' ,debug=True,port=5001) #0.0.0.0 คือเข้าได้ในอินเตอร์เน็ท