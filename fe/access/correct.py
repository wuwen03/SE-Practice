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
    
    def do_correct_file(self, file_path: str) -> tuple[(int, str)]:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            url = urljoin(self.url_prefix, "correct/upload")
            r = requests.post(url, files=files)
            return r.status_code, r.json().get("result")