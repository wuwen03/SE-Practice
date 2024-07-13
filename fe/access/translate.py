import requests
from urllib.parse import urljoin


class Translate:
    def __init__(self, url_prefix):
        self.url_prefix = url_prefix

    def do_translate(self, src_language: str, dst_language: str, content: str) -> tuple[(int, str)]:
        json = {"src_language": src_language, "dst_language": dst_language, "content": content}
        url = urljoin(self.url_prefix, "translate")
        r = requests.post(url, json=json)
        return r.status_code, r.json().get("result")