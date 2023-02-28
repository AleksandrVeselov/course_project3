from utils import funcs


def main():
    OPERATIONS_PATH = 'operations.json'  # Адрес файла с банковскими операциями
    COUNT_OPERATIONS = 5  # количество операций

    data = funcs.load_json(OPERATIONS_PATH)  # загрузка операций из файла
    if isinstance(data, str):
        print(data)
        exit()

    filtered_data = funcs.filter_operations(data)  # отбор выполненных (EXECUTED) операций
    if isinstance(filtered_data, str):
        print(data)
        exit()

    sorted_data = funcs.sort_operations(filtered_data, COUNT_OPERATIONS)  # сортировка операций по дате
    if isinstance(sorted_data, str):
        print(sorted_data)
        exit()

    # Форматирование и вывод на экран информации об операциях
    for operation in sorted_data:
        print(funcs.format_operation(operation))
        print()


if __name__ == '__main__':
    main()
