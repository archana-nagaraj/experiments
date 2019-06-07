from flask import Flask , request
import requests 
import json
app = Flask(__name__)

@app.route('/')
def index():
  return 'Index Page'

@app.route('/hello', methods=['GET','POST'])
def hello():
  return 'Hello, greetings from different endpoint'

#adding variables
@app.route('/login', methods=['GET','POST'])
def login():
  if request.method == 'POST':
    #check user details from db
    return 'POST Method'
  elif request.method == 'GET':
    #serve login page
    return 'GET Method'

@app.route('/messages', methods = ['POST'])
def body():
    if request.headers['Content-Type'] == 'text/plain':
        return 'this is the body of the message'
    else:
        return 'not sure about the content type'

@app.route('/postmessage', methods = ['POST'])
def printeverything():
    r = requests.get('http://127.0.0.1:5000/postmessage')   
    print(r.headers['Content-Type']) 
    print(r.headers['Content-Length'])
    print(r.headers['Server'])
    print(r.headers['Date'])
    return "displaying the header attribute values"

@app.route('/mymessage', methods = ['POST'])
def readbody():
    message = request.get_json()
    print(str(message))
    return str(message)


@app.route('/post/<int:post_id>')
def show_post(post_id):
  #returns the post, the post_id should be an int
  return str(post_id)


