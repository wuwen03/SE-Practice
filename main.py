from flask import Flask,jsonify,request
import json
import requests

app = Flask(__name__)

@app.route("/",mothods=['GET'])
def login():
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0")