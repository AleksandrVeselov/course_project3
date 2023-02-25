from utils import funcs

OPERATIONS = 'operations.json'  # Адрес файла с банковскими операциями


def main():
    last_operations = funcs.load_json(OPERATIONS)  # получение списка с данными о пяти последних проведенных операциях

    for operation in last_operations:
        print(funcs.format_operation(operation))  # вывод форматированных данных об операции
        print()  # пропуск строки


if __name__ == '__main__':
    main()
