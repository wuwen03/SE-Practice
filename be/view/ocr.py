#翻译

from flask import Blueprint,request,jsonify
from be.model.translate import Translate
from be.model.ocr import Ocr

bp_ocr = Blueprint("ocr",__name__,url_prefix="/ocr")

@bp_ocr.route("/",methods=['POST'])
def ocr():
    # dst_language = request.json.get("dst_language")
    picture = request.json.get("picture")

    ocr = Ocr(picture)
    code,message,content = ocr.do_ocr()

    return jsonify({"message":message,"result":content}),code