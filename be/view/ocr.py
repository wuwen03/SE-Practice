import logging
import os
import uuid
from flask import Blueprint,request,jsonify
from be.model.translate import Translate
from be.model.ocr import Ocr

cur_dir = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(cur_dir, 'uploads_tmp/')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
    
bp_ocr = Blueprint("ocr",__name__,url_prefix="/ocr")

@bp_ocr.route("/upload",methods=['POST'])
def ocr():
    # picture = request.json.get("picture")
    if 'file' not in request.files:
        return jsonify({"message":"no file part","result":""}), 520
    file = request.files['file']
    if file.filename == '':
        return jsonify({"message":"no selected file","result":""}), 521
    if file:
        # 使用 uuid4 生成唯一的文件名
        unique_filename = str(uuid.uuid4()) + "_" + file.filename
        filepath = os.path.join(UPLOAD_FOLDER, unique_filename)
        file.save(filepath)
        ocr = Ocr(filepath)
        code,message,content = ocr.do_ocr()
        os.remove(filepath)

    return jsonify({"message":message,"result":content}),code

