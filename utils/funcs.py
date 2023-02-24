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


def format_datetime(date_operation):
    pass


def format_operation(operation_data):
    pass
