from tests import (
    CONSUMPTION_RESPONSE,
    CONTRACT_RESPONSE,
    POWER_RESPONSE,
    SUPPLIES_RESPONSE,
    TOKEN,
)
from datadis import (
    get_consumption_data,
    get_max_power,
    get_token,
    get_supplies,
    get_contract_detail,
    _ENDPOINTS,
)
from unittest import mock
import pytest


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
    if args[0].startswith(_ENDPOINTS["get_supplies"]):
        return MockResponse(
            SUPPLIES_RESPONSE,
            status_code=200,
        )
    elif args[0].startswith(_ENDPOINTS["get_contract_detail"]):
        return MockResponse(
            CONTRACT_RESPONSE,
            status_code=200,
        )
    elif args[0].startswith(_ENDPOINTS["get_consumption_data"]):
        return MockResponse(CONSUMPTION_RESPONSE)
    elif args[0].startswith(_ENDPOINTS["get_max_power"]):
        return MockResponse(POWER_RESPONSE)
    else:
        return MockResponse([{}], TOKEN, 200)


@pytest.mark.asyncio
@mock.patch("httpx.AsyncClient.post", side_effect=mock_requests)
async def test_get_token(mock_post: mock.MagicMock):
    token = await get_token("username", "password")

    mock_post.assert_called_once()
    assert token == TOKEN
    assert "params" not in mock_post.call_args[1]


@pytest.mark.asyncio
@mock.patch("httpx.AsyncClient.get", side_effect=mock_requests)
async def test_get_supplies(mock_get: mock.MagicMock):
    supplies = await get_supplies("token")

    mock_get.assert_called_once()
    assert len(supplies) == 1
    assert supplies[0]["address"] == SUPPLIES_RESPONSE[0]["address"]


@pytest.mark.asyncio
@mock.patch("httpx.AsyncClient.get", side_effect=mock_requests)
async def test_get_supplies_authorized(mock_get: mock.MagicMock):
    supplies = await get_supplies("token", "123456789A")

    mock_get.assert_called_once()
    assert len(supplies) == 1
    assert supplies[0]["address"] == SUPPLIES_RESPONSE[0]["address"]
    assert mock_get.call_args[1]["params"]["authorizedNif"] == "123456789A"


@pytest.mark.asyncio
@mock.patch("httpx.AsyncClient.get", side_effect=mock_requests)
async def test_get_contract_detail(mock_get: mock.MagicMock):
    contract_detail = await get_contract_detail("token", "cupaso", 2)

    mock_get.assert_called_once()
    assert contract_detail is not None
    assert "authorizedNif" not in mock_get.call_args[1]["params"]


@pytest.mark.asyncio
@mock.patch("httpx.AsyncClient.get", side_effect=mock_requests)
async def test_get_consumption_data(mock_get: mock.MagicMock):
    contract_detail = await get_consumption_data(
        "token", "cupaso", 2, "2021/08/01", "2021/08/31", 0, 5
    )

    mock_get.assert_called_once()
    assert contract_detail is not None
    assert "authorizedNif" not in mock_get.call_args[1]["params"]


@pytest.mark.asyncio
@mock.patch("httpx.AsyncClient.get", side_effect=mock_requests)
async def test_get_max_power(mock_get: mock.MagicMock):
    contract_detail = await get_max_power(
        "token", "cupaso", 2, "2021/08/01", "2021/08/31"
    )

    mock_get.assert_called_once()
    assert contract_detail is not None
    assert "authorizedNif" not in mock_get.call_args[1]["params"]
