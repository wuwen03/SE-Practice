import os
import pytest
from fe.access import summary
from fe import conf
from test_text import text

class TestSummary:
    @pytest.fixture(autouse=True)
    def pre_run_initialization(self):
        self.summary = summary.Summary(conf.URL)
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        self.filepath1 = os.path.join(cur_dir, "test_text/test.pdf")        
        self.filepath2 = os.path.join(cur_dir, "test_text/test.txt")
        self.filepath3 = os.path.join(cur_dir, "test_text/test.docx")
        yield

    def test_ok(self):
        code, result = self.summary.do_summary(text.normal_text)
        assert code == 200

    def test_abnormal_text(self):
        code, result = self.summary.do_summary(text.abnormal_text) 
        assert code == 200
        
    def test_pdf(self):
        code, result = self.summary.do_summary_file(self.filepath1)
        assert code == 200
        
    def test_txt(self):
        code, result = self.summary.do_summary_file(self.filepath2)
        assert code == 200
        
    def test_docx(self):
        code, result = self.summary.do_summary_file(self.filepath3)
        assert code == 200
    