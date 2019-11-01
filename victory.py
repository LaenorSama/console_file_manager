import random

# для тестов фиксировали рэндом, чтобы выдавал одинаковые данные
# random.seed(42)

# создадим датасет с днями рождениями знаменитостей
# список словарей
people_dataset = [
    {'name': 'Эмма Уотсон', 'digit_date': '15.04.1990', 'alpha_date': '15 апреля 1990 г.'},
    {'name': 'Эмилия Кларк', 'digit_date': '23.10.1986', 'alpha_date': '23 октября 1986 г.'},
    {'name': 'Эллен Рипли', 'digit_date': '07.01.2092', 'alpha_date': '7 января 2092 г.'},
    {'name': 'Джон Коннор', 'digit_date': '28.02.1985', 'alpha_date': '28 февраля 1985 г.'},
    {'name': 'Милена Фермер', 'digit_date': '12.09.1961', 'alpha_date': '12 сентября 1961 г.'},
    {'name': 'Тарья Турунен', 'digit_date': '17.08.1977', 'alpha_date': '17 августа 1977 г.'},
    {'name': 'Уна Чаплин', 'digit_date': '04.06.1986', 'alpha_date': '4 июня 1986 г.'},
    {'name': 'Роуз Лесли', 'digit_date': '09.02.1987', 'alpha_date': '9 февраля 1987 г.'},
    {'name': 'Джейсон Мамоа', 'digit_date': '01.08.1979', 'alpha_date': '1 августа 1979 г.'},
    {'name': 'Натали Эммануэль', 'digit_date': '02.03.1989', 'alpha_date': '2 марта 1989 г.'}
]

def start_game():
    # выбираем 'случайно' несколько людей из списка
    people_count = 5
    people_for_test = random.sample(people_dataset, people_count)

    # для теста выводили что он нам выбрал
    # print(people_for_test)

    # обнуляем счетчики
    correct_answer = 0
    fail_answer = 0

    # начальное желаение играть
    wish_play = True
    # так же обнулим счетчик попыток
    try_counts = 0
    # цикл для постоянного запуска блока с вопросами
    while wish_play:
        # задаем вопросы в цикле
        for name in people_for_test:
            # для теста выводили тип элемента
            # print(type(name))
            user_answer = input(f'Введите дату рождения человека {name["name"]} , в формате "dd.mm.yyyy"')
            if user_answer == name["digit_date"]:
                print(random.sample(['Верно!', 'Отлично!', 'Великолепно!', 'Невероятно!'], 1)[0])
                correct_answer += 1
            else:
                print(random.sample(['Неверно :(', 'Почти получилось :(', 'Ошибка :(', 'Мимо :('], 1)[0])
                fail_answer += 1
                print(f'Правильный ответ: {name["alpha_date"]}')

        # выводим % правильных и неправильных
        print(
            f'Верно отвечено на {correct_answer / people_count * 100}% и неверно отвечено на {fail_answer / people_count * 100}% от заданных вопросов.')

        # увеличиваем счетчик попыток
        try_counts += 1

        # спрашиваем хочет ли пользователь повторить попытку
        wish_play = input('Чтобы попытаться еще раз введите "да", для выхода введите что-нибудь другое :D')
        # ой! мы поменяли тип переменной!! как же так!! вернем как нам надо
        if wish_play == 'да':
            wish_play = True
        else:
            wish_play = False

    # прощаемся с пользователем
    print(f'Вы пытались {try_counts} раз! Но теперь все позади!')
    print('Хорошего дня! Подписывайтесь, ставьте лайки!')
    pass