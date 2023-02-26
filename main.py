from utils import funcs

OPERATIONS_PATH = 'operations.json'  # Адрес файла с банковскими операциями
COUNT_OPERATIONS = 5  # количество операций


def main():
    data = funcs.load_json(OPERATIONS_PATH)
    if isinstance(data, str):
        print(data)
        exit()

    filtered_data = funcs.filter_operations(data)
    if isinstance(filtered_data, str):
        print(data)
        exit()

    sorted_data = funcs.sort_operations(filtered_data, COUNT_OPERATIONS)
    if isinstance(sorted_data, str):
        print(sorted_data)
        exit()

    for operation in sorted_data:
        print(funcs.format_operation(operation))
        print()


if __name__ == '__main__':
    main()
