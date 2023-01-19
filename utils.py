import json




def load_data():
    '''
    эта функция загружает данные из
    файла json, и возвращает данные,
    а именно список.
    '''
    with open('data.json', 'r', encoding='UTF-8') as data:
        return json.load(data)
    
    
def day_week_data(day_week):
    '''
    эта функция берет нынешнее число,
    но во вьюшке берет на день больше,
    потому что нам нужно вывести расписание
    на завтра. и форматирует число в строку
    с днем недели (str), что бы потом проверить
    все дни с этим днем недели, и в итоге 
    возвратить список со всеми данными по
    этому дню.
    
    '''
    if day_week == 1:
        day_week = "вт"
    if day_week == 2:
        day_week = "ср"
    if day_week == 3:
        day_week = "чт"
    if day_week == 4:
        day_week = "пт"
    if day_week == 5:
        day_week = "сб"
    if day_week == 6:
        day_week = "вс"
    if day_week == 7:
        day_week = "пн"
    result = []
    for part in load_data():
        if part['day_week'] == day_week:
            result.append(part)
    return result


def search_for_lesson(query):
    '''
    эта функция ищет из data.json те уроки
    которые запросил в строке поиска, и эта
    функция возвращает список со всеми данными
    этого урока
    '''
    result = []
    for lesson in load_data():
        if query in lesson["discipline"]:
            result.append(lesson)
    return result




# сделал ненужные функции, потому что не понял условие
# delit code:

# def time_data(time):
#     result = []
#     for part in load_data():
#         if part['time'] == time:
#             result.append(part)
#     return result

# def discipline_data(discipline):
#     result = []
#     for part in load_data():
#         if part['discipline'] == discipline:
#             result.append(part)
#     return result

# def type_data(type_):
#     result = []
#     for part in load_data():
#         if part['type'] == type_:
#             result.append(part)
#     return result

# def classroom_data(classroom):
#     result = []
#     for part in load_data():
#         if part['classroom'] == classroom:
#             result.append(part)
#     return result

# def building_data(building):
#     result = []
#     for part in load_data():
#         if part['building'] == building:
#             result.append(part)
#     return result

# def position_data(position):
#     result = []
#     for part in load_data():
#         if part['position'] == position:
#             result.append(part)
#     return result

# def teacher_data(teacher):
#     result = []
#     for part in load_data():
#         if part['teacher'] == teacher:
#             result.append(part)
#     return result

# def department_data(department):
#     result = []
#     for part in load_data():
#         if part['department'] == department:
#             result.append(part)
#     return result