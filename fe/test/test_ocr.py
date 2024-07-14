import base64
import pytest
from fe.access import ocr
from fe import conf
import os

def getBody(filepath):
    with open(filepath, 'rb') as f:
        imgfile = f.read()
    data = str(base64.b64encode(imgfile), 'utf-8')
    return data

class TestOcr:
    @pytest.fixture(autouse=True)
    def pre_run_initialization(self):
        self.ocr = ocr.Ocr(conf.URL)
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        picFilePath = os.path.join(cur_dir, "test_pic/ocr.jpg")
        self.b64pic = getBody(picFilePath)
        yield

    def test_ok(self):
        code, result = self.ocr.do_ocr(self.b64pic)
        assert code == 200
    
    def test_invalid_b64encode(self):
        code, result = self.ocr.do_ocr("abc")
        assert code != 200