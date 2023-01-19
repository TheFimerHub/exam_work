import pytest
from utils import *


def test_load_data():
    test = load_data()
    assert type(test) == list, "Ошибка, функция не возвращает list"
    assert type(test[0]) == dict, "Ошибка, функция не возвращает dict"

def test_day_week_data():
    day_week = 6
    test = day_week_data(day_week)
    assert type(test) == list, "Ошибка, функция не возвращает list"

def test_search_for_lesson():
    query = "Теория тепловых процессов"
    test = search_for_lesson(query)
    assert type(test) == list, "Ошибка, функция не возвращает list"
    assert type(test[0]) == dict, "Ошибка, функция не возвращает dict"