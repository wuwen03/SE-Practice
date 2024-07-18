import logging
import os
from flask import Blueprint,request,jsonify
from be.model.handle_file import handle_file
from be.model.ocr import Ocr
    
bp_ocr = Blueprint("ocr",__name__,url_prefix="/ocr")

@bp_ocr.route("/upload",methods=['POST'])
def ocr():
    hf = handle_file()
    filepath, code = hf.getfile()
    if code == 520:
        return jsonify({"message":"no file part","result":""}), 520
    elif code == 521:
        return jsonify({"message":"no selected file","result":""}), 521
    ocr = Ocr(filepath)
    code,message,content = ocr.do_ocr()
    os.remove(filepath)
    return jsonify({"message":message,"result":content}),code

