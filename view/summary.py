#概括
from flask import Blueprint,request,jsonify
from model.summary import Summary
from utils.logger import logger

bp_summary = Blueprint("summary",__name__,url_prefix="/summary")

@bp_summary.route("/",methods=['POST'])
def summary():
    content = request.json.get("content")   
    sum = Summary(content)
    code,message,ans = sum.do_summary()
    return jsonify({"message":message,"result":ans}),code