from flask import Flask

app = Flask(__name__)

@app.route("/") #default

def index():
    return "Hello ,World ! "

@app.route("/david") 

def index():
    return "Hello ,david ! "
