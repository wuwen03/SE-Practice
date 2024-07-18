#概括
import os
from flask import Blueprint,request,jsonify
from be.model.summary import Summary
from be.utils.logger import logger
from be.model.handle_file import handle_file

bp_summary = Blueprint("summary",__name__,url_prefix="/summary")

@bp_summary.route("/",methods=['POST'])
def summary():
    content = request.json.get("content")   
    sum = Summary(content)
    code,message,ans = sum.do_summary()
    return jsonify({"message":message,"result":ans}),code

@bp_summary.route("/upload",methods=['POST'])
def summary_file():
    hf = handle_file()
    filepath, code = hf.getfile()
    if code == 520:
        return jsonify({"message":"no file part","result":""}), 520
    elif code == 521:
        return jsonify({"message":"no selected file","result":""}), 521
    text = hf.readfile(filepath)
    summary = Summary(text)
    code,message,res = summary.do_summary()
    os.remove(filepath)
    return jsonify({"message":message,"result":res}),code