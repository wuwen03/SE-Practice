from flask import Flask,jsonify,request
import json
from flask.blueprints import Blueprint
import requests
import logging
from be.utils.logger import logger

from be.view.correct import bp_correct
from be.view.summary import bp_summary
from be.view.translate import bp_translate
from be.view.user import bp_user
from be.view.ocr import bp_ocr
from be.model.store import init_completed_event

app = Flask(__name__)

bp_shutdown = Blueprint("shutdown", __name__)


def shutdown_server():
    func = request.environ.get("werkzeug.server.shutdown")
    if func is None:
        raise RuntimeError("Not running with the Werkzeug Server")
    func()


@bp_shutdown.route("/shutdown")
def be_shutdown():
    shutdown_server()
    return "Server shutting down..."

@app.route("/")
def index():
    return "hello"

def be_run():
    app.register_blueprint(bp_shutdown)
    app.register_blueprint(bp_correct)
    app.register_blueprint(bp_summary)
    app.register_blueprint(bp_translate)
    app.register_blueprint(bp_user)
    app.register_blueprint(bp_ocr)
    init_completed_event.set()
    # app.run(host="0.0.0.0")    
    app.run()

if __name__ == "__main__":
    be_run()