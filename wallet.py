"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
import os, sys, shutil

# 1. пополнение счета
def donate_func(user_wallet):
    gold = int(input('Введите сумму на сколько пополнить счет:'))
    # небольшая защита от дурака
    if gold >= 0:
        user_wallet += gold
        print('Пополнение успешно.')
        print('Возврат в основное меню.')
        return user_wallet, f'пополнение;NaN;{gold};остаток на счете;{user_wallet}'
    else:
        print('Ошибка!!! Нельзя пополнить на неположительное число!!!')
        print('Возврат в основное меню.')
        return user_wallet, f'ОШИБКА ПОПОЛНЕНИЯ;NaN;{gold};остаток на счете;{user_wallet}'

# 2. покупка
def purchase_func(user_wallet):
    item_name = input('Введите наименование покупки:')
    item_cost = int(input('Введите стоимость покупки:'))
    if user_wallet >= item_cost:
        user_wallet -= item_cost
        print('Покупка успешна!')
        print('Возврат в основное меню.')
        return user_wallet, f'покупка;{item_name};{item_cost};остаток на счете;{user_wallet}'
    else:
        print('Нужно больше золота!')
        print('Возврат в основное меню.')
        return user_wallet, f'ОТКАЗ В ПОКУПКЕ;{item_name};{item_cost};остаток на счете;{user_wallet}'


# 3. выводим историю операций
def print_actions(action_list):
    if len(action_list) == 0:
        print('Вы не произвели ниодной операции.')
        print('Возврат в основное меню.')
    else:
        print('Ваши операции:')
        for i in range(len(action_list)):
            print(action_list[i])
        print('Возврат в основное меню.')


# 4. выход из меню. тут обойдемся без функции


# делаем функцию чтобы вести лог
def action_log(action, FILE_ORDER):
    with open(FILE_ORDER, 'a', encoding='utf-8') as f: # обращаемся к файлу для дозаписи
        f.write(action) # дописываем в конец файла
        f.write('\n')

# функция для изменения значения кошелька
def change_wallet(user_wallet, FILE_WALLET):
    with open(FILE_WALLET, 'w', encoding='utf-8') as f_wallet:
        f_wallet.write(str(user_wallet))

def init_wallet_menu():
    # указываем пути к файлам
    FILE_WALLET = 'database/wallet'
    FILE_ORDER = 'database/orders_list.csv'

    # текущее значение кошелька
    if os.path.exists(FILE_WALLET): # если файл есть то считываем из него инфу
        f_wallet = open(FILE_WALLET, 'r', encoding='utf-8') # обращаемся к файлу для чтения
        user_wallet = int(f_wallet.read()) # забираем значение которое есть в файле
    else: # если файла нет, то создаем пустой файл
        with open(FILE_WALLET, 'w', encoding='utf-8') as f_wallet:
            pass
        # и записываем 0 в переменную
        user_wallet = 0

    while True:
        print()
        print(f'У вас на счете {user_wallet} золота.')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история операций')
        print('4. выход')

        choice = input('Выберите пункт меню:')
        if choice == '1': # пополнение счета
            user_wallet, action = donate_func(user_wallet)
            change_wallet(user_wallet, FILE_WALLET)
            action_log(action, FILE_ORDER)
            pass

        elif choice == '2': # покупка
            user_wallet, action = purchase_func(user_wallet)
            change_wallet(user_wallet, FILE_WALLET)
            action_log(action, FILE_ORDER)
            pass

        elif choice == '3': # вывод списка операций
            with open(FILE_ORDER, 'r', encoding='utf-8') as f_order:
                print(f_order.read())
            pass

        elif choice == '4': # выход из личного счета
            return

        else: # неверный пункт меню
            print('Неверный пункт меню')

# проверяю в самом модуле
if __name__ == '__main__':
    init_wallet_menu()