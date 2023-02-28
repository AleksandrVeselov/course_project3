import json
from datetime import datetime
import os


def load_json(path_to_file: str) -> list[dict] or str:
    """
    Открывает json файл, расположенный по переданному пути
    :param path_to_file: путь к файлу с данными об операциях
    :return: список с загруженными и преобразованными данными об операциях
    """
    if os.path.exists(path_to_file):
        with open(path_to_file, 'r', encoding='UTF-8') as json_file:
            operations = json.load(json_file)  # список с данными из .json файла
            return operations

    else:
        return f'Ошибка при обращении к файлу {path_to_file}. Проверьте правильность введенного имени'


def filter_operations(operations: list[dict]) -> list[dict] or str:
    """
    Отфильтровывает выполненные операции
    :param operations: список с операциями
    :return: список с выполненными (где есть ключ 'state' и его значение равно 'EXECUTED') операциями
    """
    filtered_operations = []  # отфильтрованные данные

    for operation in operations:
        if operation.get('state') == 'EXECUTED':  # отбор выполненных (EXECUTED) операций
            filtered_operations.append(operation)  # добавление операции в список
    if filtered_operations:
        return filtered_operations

    # Если в списке нет ни одного элемента
    else:
        return 'Внимание! В списке отсутствуют операции, отвечающие заданным критериям. ' \
               'Проверьте корректность переданного списка операций'


def sort_operations(operations: list[dict], end, start=0) -> list[dict] or str:
    """
    Сортирует список по дате и возвращает нужное количество операций
    :param operations: список с операциями
    :param start: номер первой операции
    :param end: номер последней операции
    :return: список с нужным количеством операций, отсортированных по дате
    """
    for operation in operations:
        if operation.get('date'):  # отбор операций у которых есть ключ date
            operation['date'] = convert_date(operation['date'])  # конвертация даты в формат datetime
        else:
            operation['date'] = datetime(1970, 1, 1)
    operations.sort(key=lambda x: x['date'], reverse=True)  # сортировка операций в списке по дате
    return operations[start:end]  # возвращение пяти последних операций


def convert_date(date: str) -> datetime:
    input_pattern = '%Y-%m-%dT%H:%M:%S.%f'  # шаблон для входной даты
    return datetime.strptime(date, input_pattern)


def format_requisites(requisites: str) -> str:
    """Маскирует номер карты или счета в формат XXXX XX** **** XXXX или **ХХХХ соответственно.
    (видны первые 6 цифр и последние 4, разбито по блокам по 4 цифры, разделенных пробелом).
    Если номер не корректный возвращает соответствующее сообщение
    :param requisites: реквизиты карты или счета
    :return: отформатированные реквизиты карты или счета
    """
    requisites = requisites.split()  # разделение реквизитов на название карты/счета и номер
    card_number = requisites[-1]  # Выделение номера из списка

    # если номер состоит не только из цифр, то он некорректен
    if not card_number.isdigit():
        return 'Некорректный номер карты/счета'

    # иначе если его длина 16 -> это номер карты, если 20 -> это номер счета. Во всех остальных случаях он некорректен
    elif len(card_number) == 16:
        hidden_card_number = f'{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}'
    elif len(card_number) == 20:
        hidden_card_number = '**' + card_number[-4:]
    else:
        return 'Некорректный номер карты/счета'
    requisites[-1] = hidden_card_number  # замена номера карты в списке requisites на отформатированный

    return ' '.join(requisites)


def format_datetime(date_operation: datetime) -> str:
    """
    Функция конвертирует дату операции в удобный для пользователя формат.
    :param date_operation: строка с датой из файла json
    :return: строка с датой в формате удобном для чтения пользователем
    """
    output_pattern = '%d.%m.%Y'  # шаблон даты на выходе
    output_date = date_operation.strftime(output_pattern)  # конвертация из формата datetime в строку нужного формата

    return output_date


def format_operation(operation: dict) -> str:
    """
    Функция форматирует данные об операции в удобный для пользователя формат.
    Если формат словаря не соответствует шаблону, возвращает строку "Некорректные данные об операции"
    :param operation: словарь с данными об операции
    :return: строка с данными об операции в нужном формате
    """
    # Если это перевод
    if operation.get('from') and operation.get('to'):
        output_format = f"{format_datetime(operation['date'])} {operation['description']}\n" \
                        f"{format_requisites(operation['from'])} -> {format_requisites(operation['to'])}\n" \
                        f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}"

    # Если это открытие вклада
    elif operation.get('to') and not operation.get('from'):
        output_format = f"{format_datetime(operation['date'])} {operation['description']}\n" \
                        f"{format_requisites(operation['to'])}\n" \
                        f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}"

    else:
        output_format = 'Отсутствуют реквизиты'

    return output_format


