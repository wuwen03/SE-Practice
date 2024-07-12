from flask import Flask,jsonify,request
import json
import requests
import logging
from utils.logger import logger

from view.correct import bp_correct
from view.summary import bp_summary
from view.translate import bp_translate
from view.user import bp_user
from view.ocr import bp_ocr

app = Flask(__name__)

@app.route("/login",methods=['GET'])
def login():
    return 0

if __name__ == "__main__":
    app.register_blueprint(bp_correct)
    app.register_blueprint(bp_summary)
    app.register_blueprint(bp_translate)
    app.register_blueprint(bp_user)
    app.register_blueprint(bp_ocr)

    app.run(host="0.0.0.0")