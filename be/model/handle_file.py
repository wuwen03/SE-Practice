# from be.utils.logger import logger
import os
import uuid
from flask import Blueprint,request,jsonify
import mimetypes
import PyPDF2
import docx

cur_dir = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(cur_dir, 'uploads_tmp/')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

class handle_file:
    def __init__(self) -> None:
        pass
    
    def getfile(self):
        if 'file' not in request.files:
            return "", 520
        file = request.files['file']
        if file.filename == '':
            return "", 521
        # 使用 uuid4 生成唯一的文件名
        unique_filename = str(uuid.uuid4()) + "_" + file.filename
        filepath = os.path.join(UPLOAD_FOLDER, unique_filename)
        file.save(filepath)
        return filepath, 200

    def extract_text_from_pdf(self, file_path):
        file = open(file_path, 'rb')
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        content = ""
        for i in range(num_pages):
            page = pdf_reader.pages[i]
            content += page.extract_text()
        file.close()
        return content
    
    def readfile(self, filepath):
        mimetype, _ = mimetypes.guess_type(filepath)
        if mimetype == 'application/pdf':
            content = self.extract_text_from_pdf(filepath)
            return content
        elif mimetype == 'text/plain':
            with open(filepath, encoding='utf-8') as f:
                content = f.read()
            return content
        elif mimetype == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':   
            file = docx.Document(filepath)
            content = ''
            for p in file.paragraphs:
                content += p.text
                content += '\n'
            print(content)
            return content
        # print(mimetype)
    
if __name__ == "__main__":
    hf = handle_file()
    hf.readfile(r"C:\Users\ld\Desktop\se\SE-Practice\fe\test\test_text\test.docx")