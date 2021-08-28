import requests

_HOST = 'https://datadis.es'
_ENDPOINTS = {
    'get_token': f'{_HOST}/nikola-auth/tokens/login',
    'get_supplies': f'{_HOST}/api-private/api/get-supplies',
    'get_contract_detail': f'{_HOST}/api-private/api/get-contract-detail',
}


def get_token(username: str, password: str) -> str:
    credentials = {'username': username, 'password': password}
    r = requests.post(_ENDPOINTS['get_token'], data=credentials)
    if r.status_code == 200:
        return r.text
    else:
        raise Exception(f'Error: {r.json()["message"]}')


def get_supplies(token: str) -> dict:
    headers = {'Authorization': f'Bearer {token}'}
    r = requests.get(_ENDPOINTS['get_supplies'], headers=headers)
    if r.status_code == 200:
        return r.json()
    else:
        raise Exception(f'Error: {r.json()["message"]}')


def get_contract_detail(token: str, cups: str, distributorCode: int) -> dict:
    headers = {'Authorization': f'Bearer {token}'}

    r = requests.get(_ENDPOINTS['get_contract_detail']
                     + f'?cups={cups}&distributorCode={distributorCode}',
                     headers=headers)

    if r.status_code == 200:
        return r.json()
    else:
        raise Exception(f'Error: {r.json()["message"]}')
