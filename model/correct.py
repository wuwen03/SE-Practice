class Correct:
    def __init__(self,text) -> None:
        self.template = "帮我重写以下这段文字，并指出其中的语法错误：{}"
        self.text = text

    def do_correct(self)->tuple[int,str,str]:
        '''连接通义千问api,获取改正后的答案'''
        ans = "answer"
        return 200,ans