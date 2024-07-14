import pytest
from fe.access import summary
from fe import conf
from test_text import text

class TestSummary:
    @pytest.fixture(autouse=True)
    def pre_run_initialization(self):
        self.summary = summary.Summary(conf.URL)
        yield

    def test_ok(self):
        code, result = self.summary.do_summary(text.normal_text)
        assert code == 200

    def test_abnormal_text(self):
        code, result = self.summary.do_summary(text.abnormal_text) 
        assert code == 200
    