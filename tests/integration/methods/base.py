from urllib.parse import urljoin

import requests

from tests.config import LOCAL_HOST


class BaseMethod:
    response = None
    url = LOCAL_HOST

    def __init__(self, base=LOCAL_HOST, method=''):
        self.method = method
        self.base = base

    def url_join(self):
        self.url = urljoin(self.base, self.method)
        return self.url

    def send_post_request(self, body):
        self.response = requests.post(self.url, body)
        return self.response

    def should_be_status_code_200(self):
        assert self.response.status_code == 200, \
            f'Status code of response is not 200. Returned {self.response.status_code}'

    def should_be_status_code_302(self):
        assert self.response.status_code == 302, \
            f'Status code of response is not 302. Returned {self.response.status_code}'

    def should_be_status_code_405(self):
        assert self.response.status_code == 405, \
            f'Status code of response is not 405. Returned {self.response.status_code}'
