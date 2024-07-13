import requests
from urllib.parse import urljoin


class Correct:
    def __init__(self, url_prefix):
        self.url_prefix = url_prefix

    def do_correct(self, content: str) -> tuple[(int, str)]:
        json = {"content": content}
        url = urljoin(self.url_prefix, "correct")
        r = requests.post(url, json=json)
        return r.status_code, r.json().get("result")