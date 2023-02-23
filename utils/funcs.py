import json


def load_json(path: str) -> list[dict]:
    """
    Открывает json файл с данными об операциях, возвращает
    список с данными о пяти выполненных операциях
    :param path: путь к файлу с данными об операциях
    :return: список с данными о последних пяти выполненных операциях
    """
    with open(path, 'r', encoding='UTF-8') as json_file:
        data = json.load(json_file)  # список с данными из .json файла
        filtered_data = []  # отфильтрованные данные
        counter = -1  # индекс последней в списке операции

        while len(filtered_data) != 5:
            if data['counter'].get('state') == 'EXECUTED':
                filtered_data.append(data['counter'])  # добавление операции в список
            counter -= 1  # уменьшение индекса на 1

    return filtered_data






def format_requisites(requisites):
    pass


def format_datetime(date_operation):
    pass


def format_operation(operation_data):
    pass
