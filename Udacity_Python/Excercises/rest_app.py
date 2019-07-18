from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Index"

@app.route('/company')
def company():
    return "Company_name"

@app.route('/employees')
def employees():
    return "employees"

@app.route("/employees/<string:name>/")
def getEmployee(name):
    return "name</string:name>"

if __name__ == '__main__':
    app.run()

