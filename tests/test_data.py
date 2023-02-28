import pytest
from datetime import datetime


@pytest.fixture()
def test_list_1():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2016-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2019-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        },
        {},
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        },
        {
            "id": 608117766,
            "state": "CANCELED",
            "date": "2018-10-08T09:05:05.282282",
            "operationAmount": {
                "amount": "77302.31",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Visa Gold 6527183396477720",
            "to": "Счет 38573816654581789611"
        },
        {
            "id": 108066781,
            "state": "EXECUTED",
            "operationAmount": {
                "amount": "25762.92",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 90817634362091276762"
        }]


@pytest.fixture()
def test_list_2():
    return [{
        "id": 464419177,
        "state": "CANCELED",
        "date": "2018-07-15T18:44:13.346362",
        "operationAmount": {
            "amount": "71024.64",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на счет",
        "from": "Visa Gold 9657499677062945",
        "to": "Счет 19213886662094884261"
    },
        {
            "id": 560813069,
            "date": "2019-12-03T04:27:03.427014",
            "operationAmount": {
                "amount": "17628.50",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "MasterCard 1796816785869527",
            "to": "Visa Classic 7699855375169288"
        }]


@pytest.fixture()
def test_list_3():
    return [{
        "id": 441945886,
        "state": "EXECUTED",
        "date": datetime.strptime("2019-08-26T10:50:58.294041", '%Y-%m-%dT%H:%M:%S.%f'),
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"}, {
            "id": 587085106,
            "state": "EXECUTED",
            "date": datetime.strptime("2019-03-23T10:45:06.972075", '%Y-%m-%dT%H:%M:%S.%f'),
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        }, {
            "id": 587085106,
            "state": "EXECUTED",
            "date": datetime.strptime("2019-03-23T10:45:06.972075", '%Y-%m-%dT%H:%M:%S.%f'),
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
        }, {
            "id": 587085106,
            "state": "EXECUTED",
            "date": datetime.strptime("2019-03-23T10:45:06.972075", '%Y-%m-%dT%H:%M:%S.%f'),
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219H82431"
        },  {
            "id": 587085106,
            "state": "EXECUTED",
            "date": datetime.strptime("2019-03-23T10:45:06.972075", '%Y-%m-%dT%H:%M:%S.%f'),
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 4142156539521928243199"
        }]

