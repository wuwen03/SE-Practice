#1、根据输入的中文文本进行改写，指出语法错误

from flask import Blueprint,request,jsonify
from model.correct import Correct

bp_correct = Blueprint("correct",__name__,url_prefix="/correct")

@bp_correct.route("/",methods=['POST'])
def correct():
    text = request.json.get("content")
    correct = Correct(text)
    code,message,res = correct.do_correct(text)
    return jsonify({"message":message,"result":res}),code