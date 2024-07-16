import base64
import pytest
from fe.access import ocr
from fe import conf
from be.utils.api import handle_image
import os
import logging

# def getBody(filepath):
#     with open(filepath, 'rb') as f:
#         imgfile = f.read()
#     data = str(base64.b64encode(imgfile), 'utf-8')
#     return data

class TestOcr:
    @pytest.fixture(autouse=True)
    def pre_run_initialization(self):
        self.ocr = ocr.Ocr(conf.URL)
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        
        self.picFilePath1 = os.path.join(cur_dir, "test_pic/1.png")        
        self.picFilePath2 = os.path.join(cur_dir, "test_pic/2.jpg")
        self.picFilePath3 = os.path.join(cur_dir, "test_pic/3.wav")

        yield

    def test_ok_png(self):
        code, result = self.ocr.do_ocr(self.picFilePath1)
        assert code == 200
        
    def test_ok_jpg(self):
        code, result = self.ocr.do_ocr(self.picFilePath2)
        assert code == 200        
    
    def test_fail_wav(self):
        code, result = self.ocr.do_ocr(self.picFilePath3)
        assert code != 200