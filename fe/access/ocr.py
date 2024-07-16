import requests
from urllib.parse import urljoin


class Ocr:
    def __init__(self, url_prefix):
        self.url_prefix = url_prefix

    def do_ocr(self, pic_path: str) -> tuple[(int, str)]:
        with open(pic_path, 'rb') as f:
            files = {'file': f}
            url = urljoin(self.url_prefix, "ocr/upload")
            r = requests.post(url, files=files)
            return r.status_code, r.json().get("result")