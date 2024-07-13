from googletrans import Translator
from be.utils.api import call_with_messages

class Translate:
    def __init__(self,src_language,dst_language,content) -> None:
        self.src_lang = src_language
        self.dst_lang = dst_language
        self.content = content

    def do_translate(self) -> tuple[int,str,str]:
        translater = Translator()
        try:
            # result = translater.translate(self.content, self.dst_lang, self.src_lang)
            result = call_with_messages("将下面一段话翻译成中文:{}".format(self.content))
        except ValueError as e:
            return 501, "{}".format(str(e)), ""
        except BaseException as e:
            return 530, "{}".format(str(e)), ""
        
        return 200, "ok", result   
        # return 200, "ok", result.text        
        # 这个包不太稳定（可能530）只是暂时用一下跑通测试