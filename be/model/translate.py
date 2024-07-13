from googletrans import Translator
class Translate:
    def __init__(self,src_language,dst_language,content) -> None:
        self.src_lang = src_language
        self.dst_lang = dst_language
        self.content = content

    def do_translate(self) -> tuple[int,str,str]:
        translater = Translator()
        try:
            result = translater.translate(self.content, self.dst_lang, self.src_lang)

        except ValueError as e:
            return 501, "{}".format(str(e)), ""
        except BaseException as e:
            return 530, "{}".format(str(e)), ""
        
        return 200, "ok", result.text        
        # 这个包不太稳定（可能530）只是暂时用一下跑通测试