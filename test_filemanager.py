# тестируем свои функции
import os, sys, shutil
from operations_with_files import check_copy

def test_check_copy():
    dir_name = 'new folder' # берем имя папки
    copy_dir_name = check_copy(dir_name) # генерируем как будет называться копия
    assert not os.path.exists(copy_dir_name) # проверяем есть такое имя в директории
    assert copy_dir_name.find(dir_name) == 0 # проверяем начинается ли название копии с названия исходной папки

    file_name = 'new.txt.py' # берем файл с расширением
    copy_file_name = check_copy(file_name)  # генерируем как будет называться копия

    file_name_list = [i for i in file_name.split('.')]
    copy_file_name_list = [i for i in copy_file_name.split('.')]
    assert copy_file_name_list[-1] == file_name_list[-1] # сверяем расширение

    # проверяем начинается ли название копии с названия исходного файла
    file_name_only = ''
    for el in range(len(file_name_list) - 1):
        file_name_only += file_name_list[el]
        if el <= len(file_name_only) - 2:
            file_name_only += '.'
    assert copy_file_name.find(file_name_only) == 0