from typing import Any, List, Mapping, Type, TypeVar, TypedDict


class Supplie(TypedDict):
    address: str
    cups: str
    postalCode: str
    province: str
    municipality: str
    distributor: str
    validDateFrom: str
    validDateTo: str
    pointType: int
    distributorCode: str


class ContractDetail(TypedDict):
    cups: str
    distributor: str
    marketer: str
    tension: str
    accesFare: str
    province: str
    municipality: str
    postalCode: str
    contractedPowerkW: List[int]
    timeDiscrimination: str
    modePowerControl: str
    startDate: str
    endDate: str


class ConsumptionData(TypedDict):
    cups: str
    date: str
    time: str
    consumptionKWh: float
    obtainMethod: str


class MaxPower(TypedDict):
    cups: str
    date: str
    time: str
    maxPower: float


T = TypeVar('T', Supplie, ConsumptionData, ContractDetail, MaxPower)


def dict_to_typed(data: Mapping[str, Any], typed: Type[T]) -> T:
    result: T = typed.__call__()
    for key, _ in typed.__annotations__.items():
        if key not in data:
            raise ValueError(f"Key: {key} is not available in data.")
        result[key] = data[key]
    return result
