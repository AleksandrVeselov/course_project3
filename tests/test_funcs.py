import json
from datetime import datetime

import pytest
from tests.test_data import test_list_1, test_list_2
from utils import funcs


def test_load_json():
    # Подача в функцию отсутствующего файла
    test_path = 'missing_file.json'
    data = funcs.load_json(test_path)
    assert data == f'Ошибка при обращении к файлу {test_path}. Проверьте правильность введенного имени'

    # Подача тестового файла
    test_path = './tests/test_operations.json'
    reference_data = {}  # Тестовые данные для сравнения
    data = funcs.load_json(test_path)
    assert data == reference_data


def test_filter_operations(test_list_1, test_list_2):

    filter_data = funcs.filter_operations(test_list_1)
    assert len(filter_data) == 4

    filter_data = funcs.filter_operations(test_list_2)
    assert filter_data == 'Внимание! В списке отсутствуют операции, отвечающие заданным критериям. ' \
                          'Проверьте корректность переданного списка операций'


def test_sort_operations(test_list_1):
    sorted_data = funcs.sort_operations(test_list_1, 7)
    assert sorted_data[0]['id'] == 441945886
    assert sorted_data[-1]['date'] == datetime(1970, 1, 1)


def test_format_requisites():
    pass


def test_format_datetime():
    pass


def test_format_operations():
    pass
