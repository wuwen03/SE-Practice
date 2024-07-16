import logging
from be.utils.api import call_with_image
class Ocr:
    def __init__(self,picture) -> None:
        self.pic_str = picture

    def do_ocr(self) -> tuple[int,str,str]:
        try:
            res = call_with_image(self.pic_str, "提取图中文字")
        except BaseException as e:
            return 530, "{}".format(str(e)), ""
        return 200, "ok", res