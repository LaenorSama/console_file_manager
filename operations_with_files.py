# в этом модуле функции на все элементы меню
# нам потребутются
import os, shutil, json


# функция проверяет есть ли копия, если есть то увеличит номер копии и так пока не найдет последнюю
def check_copy(element):
    i = 1
    if not os.path.isfile(element):
        while os.path.exists(f'{element} ({i})'):
            i += 1
        free_name = f'{element} ({i})'
    else:
        # разобьем по точкам
        el_list = [i for i in element.split('.')]
        el_name = ''
        for el in range(len(el_list) - 1):
            # print(el_list[el])
            el_name += el_list[el]
            if el <= len(el_list) - 2:
                el_name += '.'
        el_index = el_list[-1]
        # print(el_name)
        while os.path.exists(f'{el_name}({i}).{el_index}'):
            i += 1
        free_name = f'{el_name}({i}).{el_index}'
    return free_name  # возвращает имя копии которую можно создать


# 1 пункт меню - создать папку
def create_dir_func(dir_name):  # создаем папку
    # проверка ввел ли пользователь имя папки
    if dir_name == '':
        # если не ввел то будем создавать новую папку
        dir_name = 'new_folder'
    # проверка на существование
    if os.path.exists(dir_name):
        # если папка есть, то спросим создать копию или ничего не делать.
        choice = input('Такая папка уже существует, создать новую? (y/n)')
        # если пишет 'y' или пустое поле, то делаем новую со следующей цифрой
        if choice == 'y' or choice == '':
            free_name = check_copy(dir_name)
            # создаем копию папки
            os.mkdir(free_name)
    else:
        # создаем папку
        os.mkdir(f'{dir_name}')


def print_files():  # показываем только файлы
    for element in os.listdir():
        if os.path.isfile(element):
            print(element, end=', ')


def print_dir():  # показываем только папки
    for element in os.listdir():
        if not os.path.isfile(element):
            print(element, end=', ')


def del_element_func(element):  # удаляем элемент
    if not os.path.exists(element):
        print('Такого элемента не существует.')
        return
    if os.path.isfile(element):
        choice = input(f'Вы точно желаете удалить файл {element}? (y/n)')
        if choice == 'y':
            os.remove(element)
    else:
        choice = input(f'Вы точно желаете удалить папку {element}? (y/n)')
        if choice == 'y':
            shutil.rmtree(element)


def copy_element_func(element):  # копируем элемент
    if not os.path.exists(element):
        print('Такого элемента не существует.')
        return
    new_element = check_copy(element)
    print(new_element)
    if os.path.isfile(element):
        shutil.copy(element, new_element)
    else:
        shutil.copytree(element, new_element)

def save_file_names_to_list(FILE_DIST = 'database/listdir.json'): # сохраняем содержимое папки в файл
    files = []
    dirs = []
    for element in os.listdir():
        if os.path.isfile(element):
            files.append(element)
        else:
            dirs.append(element)
    items_list = {'files': files, 'dirs': dirs}

    with open('database/listdir.txt', 'w', encoding='utf-8') as f_list:
         f_list.write(f'files:{files}\n')
         f_list.write(f'dirs:{dirs}\n')

    with open(FILE_DIST, 'w') as f_list:
        json.dump(items_list, f_list)



# проверяю в самом модуле
if __name__ == '__main__':
    save_file_names_to_list()