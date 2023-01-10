
# Datadis

Python client for https://datadis.es

![GitHub](https://img.shields.io/github/license/mrmarble/datadis)
[![Semantic Release](https://github.com/MrMarble/datadis/actions/workflows/release.yml/badge.svg)](https://github.com/MrMarble/datadis/actions/workflows/release.yml)
![PyPI - Downloads](https://img.shields.io/pypi/dm/datadis)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=MrMarble_datadis&metric=alert_status)](https://sonarcloud.io/dashboard?id=MrMarble_datadis)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/datadis)

## Installation

From [PyPi](https://pypi.org/project/datadis/)

```bash
pip install datadis
```
    
## Usage/Examples

```python
import asyncio
from datadis import get_token, get_supplies

token = asyncio.run(get_token('username', 'password'))

supplies = asyncio.run(get_supplies(token))

#[
#    {
#        "address": "home",
#        "cups": "1234ABC",
#        "postalCode": "1024",
#        "province": "madrid",
#        "municipality": "madrid",
#        "distributor": "Energy",
#        "validDateFrom": "2020/09",
#        "validDateTo": "2021/09",
#        "pointType": 0,
#        "distributorCode": "2"
#    }
#]
```

  