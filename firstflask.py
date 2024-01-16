from crypt import methods
from flask import Flask, request, render_template, make_response
import sys
import json

app = Flask(__name__)
##api
@app.route('request', methods={'POST'})
def web_service_API():

    payload = request.data.decode("utf-8")
    immessage = json.loads(payload)

    print(immessage)
    json_data = json.dumps({'y': 'received!'})
    return json_data

@app.route("/") # ถ้าจะใช้คำสั่งนี้ไม่ต้องมี / ก็ได้
def helloworld():
    return "Hello, World!"

@app.route("/name") # ถ้าจะใช้คำสั่งนี้ต้องมี /name
def hellotung(): 
    return "Hello, Tung!"

@app.route("/home", methods=['POST','GET'])
def homefn():
    if request.method == "GET":
       print('we are in home(GET)', file=sys.stdout)
       name = request.args.get('fname')
       print(name, file=sys.stdout)
       return render_template("home.html",name=name)
    
    elif request.method == "POST":
       print('we are in home(POST)', file=sys.stdout)
       namein = request.form.get('fname')
       lastnamein = request.form.get('lname')
       print(namein, file=sys.stdout)
       print(lastnamein, file=sys.stdout)
       return render_template("home.html",name=namein)
    
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file.save('filename')
        return render_template("home.html",name='uplond completed')
        
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == "__main__": # ต้อง IP VM เราแล้วตามด้วย :5001
    app.run(host='0.0.0.0' ,debug=True,port=5001) #0.0.0.0 คือเข้าได้ในอินเตอร์เน็ท