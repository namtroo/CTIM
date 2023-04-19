import requests

class Init:

    def __init__(self, url: str):
        self.url = url

    def start(self, target: str) -> str:
        headers = {
            "Content-Type": "application/json",
        }
        r = requests.get(
            url = self.url + "/" + target, 
            headers = headers,
        )
        return r.text