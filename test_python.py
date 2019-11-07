# тесты для встроенных функций filter, map, sorted
# а также для функций из библиотеки math: pi, sqrt, pow, hypot
# Чем больше тестов на каждую функцию - тем лучше

import pytest # для добавления параметров надо импортировать модуль

import math


def test_pi():  # число Пи
    n_pi = math.pi
    assert float(f'{n_pi:.2f}') == 3.14
    assert float(f'{n_pi:.4f}') == 3.1416
    assert float(f'{n_pi:.8f}') == 3.14159265


def test_sqrt():  # квадратный корень неотрицательного числа
    source_list = [1, 4, 9, 16, 64, 1024]
    result_list = [1, 2, 3, 4, 8, 32]
    for i in range(len(source_list)):
        assert math.sqrt(source_list[i]) == result_list[i]
        assert math.sqrt(source_list[i]) ** 2 == source_list[i]
        assert math.sqrt(source_list[i]) * math.sqrt(source_list[i]) == source_list[i]

@pytest.mark.parametrize('x', [1, 10, 20, -5, 3])
@pytest.mark.parametrize('y', [0, -2, 5, 10, 2])
def test_pow(x, y):  # возведение в степень
    # x_list = [1, 10, 20, -5, 3]
    # y_list = [0, -2, 5, 10, 2]
    # for x in x_list:
    #     for y in y_list:
    #         assert math.pow(x, y) == x ** y
    assert math.pow(x, y) == x ** y

@pytest.mark.parametrize('x', [1, 2, 3])
@pytest.mark.parametrize('y', [3, 4, 5])
def test_hypot(x, y):  # гипотенуза угла с катетами x, y
    # x_list = [1, 2, 3]
    # y_list = [3, 4, 5]
    # for x in x_list:
    #     for y in y_list:
    #         assert math.hypot(x, y) == math.sqrt(x * x + y * y)
    assert math.hypot(x, y) == math.sqrt(x * x + y * y)

@pytest.fixture(scope="function", params=[([1, 10, 20, -5, 3], [10, 20])])
def param_test(request):
    return request.param
def test_filter(param_test):
    # x_list = [1, 10, 20, -5, 3]
    # result_list = [10, 20]
    (x_list, result_list) = param_test
    assert list(filter(lambda y: True if y % 10 == 0 else False, x_list)) == result_list


def test_map():
    friends = ['max', 'leo', 'mike', 'jane']
    result = ['MAX', 'LEO', 'MIKE', 'JANE']
    assert list(map(lambda y: y.upper(), friends)) == result


def test_sorted():
    x_list = [1, 10, 20, -5, 3]
    result = [-5, 1, 3, 10, 20]
    assert sorted(x_list) == result
