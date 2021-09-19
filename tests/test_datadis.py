from datadis import (get_consumption_data, get_max_power, get_token,
                     get_supplies, get_contract_detail, _ENDPOINTS)
from unittest import mock


def mock_requests(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, text_data="", status_code=200):
            self.json_data = json_data
            self.status_code = status_code
            self.text_data = text_data

        def json(self):
            return self.json_data

        @property
        def text(self):
            return self.text_data
    print(args[0])
    if args[0].startswith(_ENDPOINTS['get_supplies']):
        return MockResponse([{
            "address": "home",
            "cups": "1234ABC",
            "postalCode": "1024",
            "province": "madrid",
            "municipality": "madrid",
            "distributor": "Energy",
            "validDateFrom": "2020/09",
            "validDateTo": "2021/09",
            "pointType": 0,
            "distributorCode": "2"
        }], status_code=200)
    elif args[0].startswith(_ENDPOINTS['get_contract_detail']):
        return MockResponse([{
            "address": "home",
            "cups": "c",
            "postalCode": "1024",
            "province": "madrid",
            "municipality": "madrid",
            "distributor": "Energy",
            "validDateFrom": "2020/09",
            "validDateTo": "2021/09",
            "pointType": 0,
            "marketer": "idk",
            "tension": "10",
            "accesFare": "10",
            "contractedPowerkW": ["10"],
            "timeDiscrimination": "4",
            "modePowerControl": "1",
            "startDate": "2020/09",
            "endDate": "2020/09",
        }], status_code=200)
    elif args[0].startswith(_ENDPOINTS['get_consumption_data']):
        return MockResponse([{
            "cups": "1234ABC",
            "date": "2021/08/01",
            "time": "01:00",
            "consumptionKWh": 0.194,
            "obtainMethod": "Real"
        }])
    elif args[0].startswith(_ENDPOINTS['get_max_power']):
        return MockResponse([{
            "cups": "1234ABC",
            "date": "2021/08/21",
            "time": "13:30",
            "maxPower": 3.788
        }])
    else:
        return MockResponse([{"cups": "of rice"}], 'token_ok', 200)


@mock.patch('httpx.post', side_effect=mock_requests)
def test_get_token(mock_post: mock.MagicMock):
    token = get_token("username", "password")
    assert token is not None
    assert token == 'token_ok'


@mock.patch('httpx.get', side_effect=mock_requests)
def test_get_supplies(mock_get: mock.MagicMock):
    supplies = get_supplies("token")
    assert supplies is not None
    assert len(supplies) == 1
    assert supplies[0]['address'] == 'home'


@mock.patch('httpx.get', side_effect=mock_requests)
def test_get_contract_detail(mock_get: mock.MagicMock):
    contract_detail = get_contract_detail("token", "cupaso", 2)

    assert contract_detail is not None


@mock.patch('httpx.get', side_effect=mock_requests)
def test_get_consumption_data(mock_get: mock.MagicMock):
    contract_detail = get_consumption_data(
        "token", "cupaso", 2, '2021/08/01', '2021/08/31', 0, 5)

    assert contract_detail is not None


@mock.patch('httpx.get', side_effect=mock_requests)
def test_get_max_power(mock_get: mock.MagicMock):
    contract_detail = get_max_power(
        "token", "cupaso", 2, '2021/08/01', '2021/08/31')

    assert contract_detail is not None
