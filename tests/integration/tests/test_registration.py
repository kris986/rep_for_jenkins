import pytest

from tests.integration.methods.registration import Registration


class TestRegistration:
    registration = Registration()

    @pytest.mark.parametrize('body', [{'username': 'user_u1',
                                       'email': 'ubuntu1@ubuntu.com',
                                       'password': '12345',
                                       'country': 'ubuntu',
                                       'city': '19'}])
    def test_post_valid_data(self, body):
        self.registration.send_post_request(body)
        self.registration.should_be_status_code_200()

    @pytest.mark.parametrize('body', [{'username': 'user_u1',
                                       'email': 'ubuntu1@ubuntu.com',
                                       'password': '12345',
                                       'country': 'ubuntu',
                                       'city': '19'}])
    def test_post_invalid_data(self, body):
        self.registration.send_post_request(body)
        self.registration.should_be_status_code_405()
