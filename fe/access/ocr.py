import requests
from urllib.parse import urljoin


class Ocr:
    def __init__(self, url_prefix):
        self.url_prefix = url_prefix

    def do_ocr(self, picture: str) -> tuple[(int, str)]:
        json = {"picture": picture}
        url = urljoin(self.url_prefix, "ocr")
        r = requests.post(url, json=json)
        return r.status_code, r.json().get("result")