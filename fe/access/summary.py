import requests
from urllib.parse import urljoin


class Summary:
    def __init__(self, url_prefix):
        self.url_prefix = url_prefix

    def do_summary(self, content: str) -> tuple[(int, str)]:
        json = {"content": content}
        url = urljoin(self.url_prefix, "summary")
        r = requests.post(url, json=json)
        return r.status_code, r.json().get("result")