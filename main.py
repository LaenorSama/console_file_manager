# импортируем наши библиотеки
import wallet, victory, operations_with_files
import os, sys, shutil

# вот такие пункты меню у нас есть
menu_buttons = ['0 - просмотр пути до текущей директории (где сейчас находимся)',
                '1 - создать папку',
                '2 - удалить (файл/папку)',
                '3 - копировать (файл/папку)',
                '4 - просмотр содержимого рабочей директории',
                '5 - посмотреть только папки',
                '6 - посмотреть только файлы',
                '7 - просмотр информации об операционной системе',
                '8 - создатель программы',
                '9 - играть в викторину',
                '10 - мой банковский счет',
                '11 - смена рабочей директории',
                '12 - сохранить содержимое рабочей директории в файл',
                '13 - выход']


# # общий  счет клиента
# user_wallet = 0
# # наш список операций
# action_list = []

# собственно само меню, клиент вводит соответствующие цифры меню
while True:
    print()
    for menu_item in menu_buttons:
        print(menu_item)

    choice = input('Выберите пункт меню:')

    if choice == '0': # путь где находимся
        print(os.getcwd())

    elif choice == '1': # создать папку
        dir_name = input('Введите название папки:')
        operations_with_files.create_dir_func(dir_name)

    elif choice == '2': # удалить (файл/папку)
        element = input('Введите элемент для удаления:')
        operations_with_files.del_element_func(element)

    elif choice == '3': # копировать (файл/папку)
        element = input('Введите элемент для копирования:')
        operations_with_files.copy_element_func(element)

    elif choice == '4': # список файлов и папок
        # for element in os.listdir():
        #     print(element, end=', ')
        # использую генератор списков
        element_list = [element for element in os.listdir()]
        print(element_list)

    elif choice == '5': # просмотреть только папки
        operations_with_files.print_dir()

    elif choice == '6': # просмотреть только файлы
        operations_with_files.print_files()

    elif choice == '7': # информация о система
        print('Операционная система', sys.platform)

    elif choice == '8': # информация о создателе программы
        print('Программу создал LaenorSama.')

    elif choice == '9': # играть в викторину
        victory.start_game()

    elif choice == '10': # мой банковский счет
        wallet.init_wallet_menu()

    elif choice == '11': # переход в другую директорию
        path = input('Введите путь куда ходите перейти')
        if os.path.exists(path):
            os.chdir(path)
        else:
            print('Неправильный путь или указанной директории не существует!!!')

    elif choice == '12': # сохранить содержимое рабочей директории в файл
        FILE_DIST = 'database/listdir.txt'  # если файл, есть при запуске он перезапишется!!!
        operations_with_files.save_file_names_to_list(FILE_DIST)

    elif choice == '13':
        break

    else:
        print('Неверный пункт меню')