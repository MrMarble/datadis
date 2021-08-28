from datadis import get_token
from unittest import mock


def mock_requests(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, text_data, status_code):
            self.json_data = json_data
            self.status_code = status_code
            self.text_data = text_data

        def json(self):
            return self.json_data

        @property
        def text(self):
            return self.text_data

    return MockResponse([{"cups": "of rice"}], 'token_ok', 200)


@mock.patch('requests.post', side_effect=mock_requests)
def test_get_token(mock_post: mock.MagicMock):
    token = get_token("username", "password")
    assert token is not None
    assert token == 'token_ok'
