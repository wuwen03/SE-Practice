from be.utils.api import call_with_messages
class Summary:
    def __init__(self,content) -> None:
        self.content = content

    def do_summary(self) -> tuple[int,str,str]:
        try:
            result = call_with_messages("将下面一段话做个摘要并用数字列出:{}".format(self.content))
        except BaseException as e:
            return 530, "{}".format(str(e)), ""
        
        return 200, "ok", result 