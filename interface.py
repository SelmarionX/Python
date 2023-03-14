def main_menu(value):
    match value:
        case 'Begin':
            print('=' * 45)
            print('Телефонный справочник')
            print('=' * 45)
        case 'Main':
            print('Введите число - номер действия:')
            print('1. Создать новый файл')
            print('2. Добавить запись')
            print('3. Найти запись')
            print('4. Импорт/экспорт данных')
            print('0. Выход')
            print()
            print('Назад в основное меню', '- ввод любого другого символа'.upper())
            print('=' * 45)


def find_menu():
    print('=' * 45)
    print('Введите число - номер действия:')
    print()
    print('1. Поиск по фамилии')
    print('2. Поиск по номеру телефона')
    print()
    print('Назад в основное меню', '- ввод любого другого символа'.upper())
    print('=' * 45)


def imp_exp_menu():
    print('=' * 45)
    print('Введите число - номер действия:')
    print()
    print('1. Экспорт из csv в txt файл')
    print('2. Импорт из txt в csv файл')
    print()
    print('Назад в основное меню', '- ввод любого другого символа'.upper())
    print('=' * 45)


def file_menu():
    print('=' * 45)
    print('Выберите число - номер действия:')
    print()
    print('Введите 1 - Для подтверждения своего выбора')
    print()
    print('Назад в основное меню', '- ввод любого другого символа'.upper())
    print('=' * 45)
