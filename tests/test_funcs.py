import json

import pytest
from utils import funcs


def test_load_json():
    test_path = 'missing_file.json'
    data = funcs.load_json(test_path)
    assert data == f'Ошибка при обращении к файлу {test_path}. Проверьте правильность введенного имени'

    test_path = 'tests/test_operations.json'
    with open(test_path, 'r', encoding='UTF-8') as test_json_file:
        test_data = json.load(test_json_file)
    data = funcs.load_json(test_path)
    assert data == test_data


def test_filter_operations():
    pass


def test_sort_operations():
    pass


def test_convert_date():
    pass


def test_format_requisites():
    pass


def test_format_datetime():
    pass


def test_format_operations():
    pass
