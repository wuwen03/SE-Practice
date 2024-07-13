import pytest
from fe.access import translate
from fe import conf

class TestTranslate:
    @pytest.fixture(autouse=True)
    def pre_run_initialization(self):
        self.translate = translate.Translate(conf.URL)
        yield

    def test_ok(self):
        code, result = self.translate.do_translate("auto", "zh-cn", "i love you") #语言代码可能要改
        assert code == 200
    
    def test_no_language(self):
        code, result = self.translate.do_translate("abc", "", "i  love you")
        assert code != 200