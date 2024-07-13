#翻译

from flask import Blueprint,request,jsonify
from be.model.translate import Translate
from be.utils.logger import logger

bp_translate = Blueprint("translate",__name__,url_prefix="/translate")

@bp_translate.route("/",methods=['POST'])
def translate():
    src_language = request.json.get("src_language")
    dst_language = request.json.get("dst_language")
    content = request.json.get("content")

    logger.info("{},{},{}".format(src_language,dst_language,content))

    tran = Translate(src_language,dst_language,content)
    code,message,ans = tran.do_translate()
    # code,message,ans = 200,"","我爱你"
    return jsonify({"message":message,"result":ans}),code