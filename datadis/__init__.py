from typing import List, Literal, Mapping, Type, Union
from datadis.types import (
    T,
    ConsumptionData,
    ContractDetail,
    MaxPower,
    Supplie,
    dict_to_typed,
)
import httpx

_HOST = "https://datadis.es"
_ENDPOINTS = {
    "get_token": f"{_HOST}/nikola-auth/tokens/login",
    "get_supplies": f"{_HOST}/api-private/api/get-supplies",
    "get_contract_detail": f"{_HOST}/api-private/api/get-contract-detail",
    "get_consumption_data": f"{_HOST}/api-private/api/get-consumption-data",
    "get_max_power": f"{_HOST}/api-private/api/get-max-power",
}


async def get_token(username: str, password: str) -> str:
    """Get authentication token for private api

    Args:
        username (str): NIF/NIE associated with the account
        password (str): Password for the account

    Raises:
        Exception: If the authentication fails

    Returns:
        str: Bearer token
    """
    credentials = {"username": username, "password": password}
    async with httpx.AsyncClient(timeout=30.0) as client:
        r = await client.post(_ENDPOINTS["get_token"], data=credentials)
        if r.status_code == 200:
            return r.text
        else:
            raise ConnectionError(f'Error: {r.json()["message"]}')


async def get_supplies(token: str) -> List[Supplie]:
    """Search all the supplies

    Args:
        token (str): Bearer token

    Raises:
        Exception: If the authentication fails

    Returns:
        dict: A dictionary with the supplies
    """
    return await _request(_ENDPOINTS["get_supplies"], token, None, Supplie)


async def get_contract_detail(
    token: str, cups: str, distrubutor_code: int
) -> List[ContractDetail]:
    """Search the contract detail

    Args:
        token (str): Bearer token
        cups (str): Cups code. Get it from get_supplies
        distrubutor_code (int): Distributor code. Get it from get_supplies

    Raises:
        Exception: [description]

    Returns:
        dict: [description]
    """

    params = {"cups": cups, "distributorCode": distrubutor_code}

    return await _request(
        _ENDPOINTS["get_contract_detail"], token, params, ContractDetail
    )


async def get_consumption_data(
    token: str,
    cups: str,
    distrubutor_code: int,
    start_date: str,
    end_date: str,
    measurement_type: Literal[0, 1],
    point_type: int,
) -> List[ConsumptionData]:
    """Search the consumption data

    Args:
        token (str): Bearer token
        cups (str): Cups code. Get it from get_supplies
        start_date (str): start date beetween search data. Format: YYYY/MM/dd
        end_date (str): end date beetween search data. Format: YYYY/MM/dd
        measurement_type (str): 0 -> Hourly, 1 -> quarter hourly
        pointType (str): Point type code, get it from get-supplies
        distrubutor_code (int): Distributor code. Get it from get_supplies

    Raises:
        Exception: [description]

    Returns:
        dict: [description]
    """
    params = {
        "cups": cups,
        "distributorCode": distrubutor_code,
        "startDate": start_date,
        "endDate": end_date,
        "measurementType": measurement_type,
        "pointType": point_type,
    }

    return await _request(
        _ENDPOINTS["get_consumption_data"], token, params, ConsumptionData
    )


async def get_max_power(
    token: str,
    cups: str,
    distrubutor_code: int,
    start_date: str,
    end_date: str,
) -> List[MaxPower]:
    """Search the maximum power and the result will appear in kW

    Args:
        token (str): Bearer token
        cups (str): Cups code. Get it from get_supplies
        start_date (str): start date beetween search data. Format: YYYY/MM
        end_date (str): end date beetween search data. Format: YYYY/MM
        distrubutor_code (int): Distributor code. Get it from get_supplies

    Raises:
        Exception: [description]

    Returns:
        dict: [description]
    """
    params = {
        "cups": cups,
        "distributorCode": distrubutor_code,
        "startDate": start_date,
        "endDate": end_date,
    }

    return await _request(_ENDPOINTS["get_max_power"], token, params, MaxPower)


async def _request(
    endpoint: str,
    token: str,
    params: Union[Mapping[str, Union[str, int]], None],
    output_type: Type[T],
) -> List[T]:
    headers = {"Authorization": f"Bearer {token}"}
    async with httpx.AsyncClient(timeout=30.0) as client:
        r = await client.get(endpoint, params=params, headers=headers)
        if r.status_code == 200:
            result = []
            for contract in r.json():
                result.append(dict_to_typed(contract, output_type))
            return result
        else:
            raise ConnectionError(f'Error: {r.json()["message"]}')
