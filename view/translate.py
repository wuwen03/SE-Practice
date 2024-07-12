#翻译

from flask import Blueprint,request,jsonify
from model.translate import Translate

bp_translate = Blueprint("translate",__name__,url_prefix="/translate")

@bp_translate.route("/",methods=['POST'])
def translate():
    src_language = request.json.get("src_language")
    dst_language = request.json.get("dst_language")
    content = request.json.get("content")
    tran = Translate(src_language,dst_language,content)
    code,message,ans = tran.do_translate()
    return jsonify({"message":message,"result":ans}),code