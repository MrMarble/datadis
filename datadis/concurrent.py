from datadis.types import (
    ConsumptionData, ContractDetail, MaxPower, Supplie, dict_to_typed)
from typing import List, Literal
import httpx
from datadis import _ENDPOINTS


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
    credentials = {'username': username, 'password': password}
    async with httpx.AsyncClient() as client:
        r = await client.post(_ENDPOINTS['get_token'], data=credentials)
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
    headers = {'Authorization': f'Bearer {token}'}
    async with httpx.AsyncClient() as client:
        r = await client.get(_ENDPOINTS['get_supplies'], headers=headers)
        if r.status_code == 200:
            result = []
            for supply in r.json():
                result.append(dict_to_typed(supply, Supplie))
            return result
        else:
            raise ConnectionError(f'Error: {r.json()["message"]}')


async def get_contract_detail(token: str, cups: str,
                              distrubutor_code: int) -> List[ContractDetail]:
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
    headers = {'Authorization': f'Bearer {token}'}
    async with httpx.AsyncClient() as client:
        r = await client.get(
            _ENDPOINTS['get_contract_detail']
            + f'?cups={cups}&distributorCode={distrubutor_code}',
            headers=headers)

        if r.status_code == 200:
            result = []
            for contract in r.json():
                result.append(dict_to_typed(contract, ContractDetail))
            return result
        else:
            raise ConnectionError(f'Error: {r.json()["message"]}')


async def get_consumption_data(token: str, cups: str, distrubutor_code: int,
                               start_date: str, end_date: str,
                               measurement_type: Literal[0, 1], point_type: int
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
    headers = {'Authorization': f'Bearer {token}'}
    async with httpx.AsyncClient() as client:
        r = await client.get(
            _ENDPOINTS['get_consumption_data']
            + f'?cups={cups}&distributorCode={distrubutor_code}'
            + f'&start_date={start_date}&end_date={end_date}'
            + f'&measurement_type={measurement_type}'
            + f'&point_type={point_type}',
            headers=headers)

        if r.status_code == 200:
            result = []
            for contract in r.json():
                result.append(dict_to_typed(contract, ConsumptionData))
            return result
        else:
            raise ConnectionError(f'Error: {r.json()["message"]}')


async def get_max_power(token: str, cups: str, distrubutor_code: int,
                        start_date: str, end_date: str) -> List[MaxPower]:
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
    headers = {'Authorization': f'Bearer {token}'}
    async with httpx.AsyncClient() as client:
        r = await client.get(
            _ENDPOINTS['get_max_power']
            + f'?cups={cups}&distributorCode={distrubutor_code}'
            + f'&start_date={start_date}&end_date={end_date}',
            headers=headers)

        if r.status_code == 200:
            result = []
            for contract in r.json():
                result.append(dict_to_typed(contract, MaxPower))
            return result
        else:
            raise ConnectionError(f'Error: {r.json()["message"]}')
