from be.utils.api import call_with_messages
class Correct:
    def __init__(self,text) -> None:
        self.text = text

    def do_correct(self)->tuple[int,str,str]:
        try:
            result = call_with_messages("帮我重写下面这段话，并用数字列出其中的语法错误:{}".
                                        format(self.text))
        except BaseException as e:
            return 530, "{}".format(str(e)), ""
        
        return 200, "ok", result 