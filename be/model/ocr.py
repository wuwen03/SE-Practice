import logging
from be.utils.api import call_with_image
from be.utils.api import handle_image
class Ocr:
    def __init__(self,picpath) -> None:
        self.pic_path = picpath

    def do_ocr(self) -> tuple[int,str,str]:
        try:
            message, pic_str = handle_image(self.pic_path)
            if message == "ok":
                res = call_with_image(pic_str, "提取图中文字")
            else:
                return 522, message, ""
        except BaseException as e:
            return 530, "{}".format(str(e)), ""
        return 200, "ok", res