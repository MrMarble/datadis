import requests

_HOST = 'https://datadis.es'
_ENDPOINTS = {
    'get_token': f'{_HOST}/nikola-auth/tokens/login',
    'get_supplies': f'{_HOST}/api-private/api/get-supplies',
    'get_contract_detail': f'{_HOST}/api-private/api/get-contract-detail',
}


def get_token(username: str, password: str) -> str:
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
    r = requests.post(_ENDPOINTS['get_token'], data=credentials)
    if r.status_code == 200:
        return r.text
    else:
        raise Exception(f'Error: {r.json()["message"]}')


def get_supplies(token: str) -> dict:
    """Search all the supplies

    Args:
        token (str): Bearer token

    Raises:
        Exception: If the authentication fails

    Returns:
        dict: A dictionary with the supplies
    """
    headers = {'Authorization': f'Bearer {token}'}
    r = requests.get(_ENDPOINTS['get_supplies'], headers=headers)
    if r.status_code == 200:
        return r.json()
    else:
        raise Exception(f'Error: {r.json()["message"]}')


def get_contract_detail(token: str, cups: str, distributorCode: int) -> dict:
    """Search the contract detail

    Args:
        token (str): Bearer token
        cups (str): Cups code. Get it from get_supplies
        distributorCode (int): Distributor code. Get it from get_supplies

    Raises:
        Exception: [description]

    Returns:
        dict: [description]
    """
    headers = {'Authorization': f'Bearer {token}'}

    r = requests.get(_ENDPOINTS['get_contract_detail']
                     + f'?cups={cups}&distributorCode={distributorCode}',
                     headers=headers)

    if r.status_code == 200:
        return r.json()
    else:
        raise Exception(f'Error: {r.json()["message"]}')
