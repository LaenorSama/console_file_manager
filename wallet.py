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


# 1. пополнение счета
def donate_func(user_wallet):
    gold = int(input('Введите сумму на сколько пополнить счет:'))
    # небольшая защита от дурака
    if gold >= 0:
        user_wallet += gold
        print('Пополнение успешно.')
        print('Возврат в основное меню.')
        return user_wallet, ['пополнение', gold, 'остаток на счете', user_wallet]
    else:
        print('Ошибка!!! Нельзя пополнить на неположительное число!!!')
        print('Возврат в основное меню.')
        return user_wallet, ['ОШИБКА ПОПОЛНЕНИЯ', gold, 'остаток на счете', user_wallet]


# 2. покупка
def purchase_func(user_wallet):
    item_name = input('Введите наименование покупки:')
    item_cost = int(input('Введите стоимость покупки:'))
    if user_wallet >= item_cost:
        user_wallet -= item_cost
        print('Покупка успешна!')
        print('Возврат в основное меню.')
        return user_wallet, ['покупка', item_name, item_cost, 'остаток на счете', user_wallet]
    else:
        print('Нужно больше золота!')
        print('Возврат в основное меню.')
        return user_wallet, ['ОТКАЗ В ПОКУПКЕ', item_name, item_cost, 'остаток на счете', user_wallet]


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

def init_wallet_menu(user_wallet, action_list):
    while True:
        print()
        print(f'У вас на счете {user_wallet} золота.')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история операций')
        print('4. выход')

        choice = input('Выберите пункт меню:')
        if choice == '1':
            user_wallet, action = donate_func(user_wallet)
            action_list.append(action)
            # print(action_list)
            pass
        elif choice == '2':
            user_wallet, action = purchase_func(user_wallet)
            action_list.append(action)
            # print(action_list)
            pass
        elif choice == '3':
            print_actions(action_list)
            pass
        elif choice == '4':
            return user_wallet, action_list
            # break
        else:
            print('Неверный пункт меню')
