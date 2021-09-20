"""Constants"""

TOKEN = "FAKE_TOKEN"

SUPPLIES_RESPONSE = [
    {
        "address": "ADDRESS",
        "cups": "CUPS",
        "postalCode": "POSTAL_CODE",
        "province": "PRONVICE",
        "municipality": "MUNICIPALITY",
        "distributor": "DISTRIBUTOR",
        "validDateFrom": "2020/10/06",
        "validDateTo": "",
        "pointType": 5,
        "distributorCode": "2",
    }
]

CONTRACT_RESPONSE = [
    {
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
    }
]

CONSUMPTION_RESPONSE = [
    {
        "cups": "1234ABC",
        "date": "2021/08/01",
        "time": "01:00",
        "consumptionKWh": 0.194,
        "obtainMethod": "Real",
    }
]


POWER_RESPONSE = [
    {
        "cups": "1234ABC",
        "date": "2021/08/21",
        "time": "13:30",
        "maxPower": 3.788,
    }
]
