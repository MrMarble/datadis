from datadis import get_token, get_supplies, get_contract_detail
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


@mock.patch('requests.get', side_effect=mock_requests)
def test_get_supplies(mock_get: mock.MagicMock):
    supplies = get_supplies("token")
    assert supplies is not None
    assert supplies == [{"cups": "of rice"}]


@mock.patch('requests.get', side_effect=mock_requests)
def test_get_contract_detail(mock_get: mock.MagicMock):
    contract_detail = get_contract_detail("token", "cupaso", 2)

    assert contract_detail is not None
    assert contract_detail == [{"cups": "of rice"}]
    assert "cupaso" in mock_get.call_args.args[0]
