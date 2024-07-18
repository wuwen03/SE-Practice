#1、根据输入的中文文本进行改写，指出语法错误

import os
from flask import Blueprint,request,jsonify
from be.model.correct import Correct
from be.model.handle_file import handle_file

bp_correct = Blueprint("correct",__name__,url_prefix="/correct")

@bp_correct.route("/",methods=['POST'])
def correct():
    text = request.json.get("content")
    correct = Correct(text)
    code,message,res = correct.do_correct()
    return jsonify({"message":message,"result":res}),code

@bp_correct.route("/upload",methods=['POST'])
def correct_file():
    hf = handle_file()
    filepath, code = hf.getfile()
    if code == 520:
        return jsonify({"message":"no file part","result":""}), 520
    elif code == 521:
        return jsonify({"message":"no selected file","result":""}), 521
    text = hf.readfile(filepath)
    correct = Correct(text)
    code,message,res = correct.do_correct()
    os.remove(filepath)
    return jsonify({"message":message,"result":res}),code