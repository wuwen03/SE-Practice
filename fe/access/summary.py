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
    
    def do_summary_file(self, file_path: str) -> tuple[(int, str)]:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            url = urljoin(self.url_prefix, "summary/upload")
            r = requests.post(url, files=files)
            return r.status_code, r.json().get("result")