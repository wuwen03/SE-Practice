import pytest
from fe.access import translate
from fe import conf

class TestTranslate:
    @pytest.fixture(autouse=True)
    def pre_run_initialization(self):
        self.translate = translate.Translate(conf.URL)
        yield

    def test_ok(self):
        code, result = self.translate.do_translate("にほんご", "english", "にほんご") #japanese
        assert code == 200
    
    def test_error_dst_language(self):
        code, result = self.translate.do_translate("英语", "", "i love you")
        assert code == 200
        
    def test_error_scr_language(self):
        code, result = self.translate.do_translate("abc", "にほんご", "i love you")
        assert code == 200        