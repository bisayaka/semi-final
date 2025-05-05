from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "ARIEL MENSAVILLA BS-IT B SYSTEM INTEGRATED AND ARCHITECTURE"
