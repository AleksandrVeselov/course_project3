import json
from datetime import datetime

import pytest
from tests.test_data import test_list_1, test_list_2, test_list_3
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


def test_format_operations(test_list_3):
    formatted_data = funcs.format_operation(test_list_3[0])
    assert formatted_data == '26.08.2019 Перевод организации\n' \
                             'Maestro 1596 83** **** 5199 -> Счет **9589\n' \
                             '31957.58 руб.'

    formatted_data = funcs.format_operation(test_list_3[1])
    assert formatted_data == '23.03.2019 Открытие вклада\n' \
                             'Счет **2431\n' \
                             '48223.05 руб.'

    formatted_data = funcs.format_operation(test_list_3[2])
    assert formatted_data == 'Отсутствуют реквизиты'

    formatted_data = funcs.format_operation(test_list_3[3])
    assert formatted_data == '23.03.2019 Открытие вклада\n' \
                             'Некорректный номер карты/счета\n' \
                             '48223.05 руб.'

    formatted_data = funcs.format_operation(test_list_3[4])
    assert formatted_data == '23.03.2019 Открытие вклада\n' \
                             'Некорректный номер карты/счета\n' \
                             '48223.05 руб.'



