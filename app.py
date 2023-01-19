import logging
from flask import Flask, render_template, request
from utils import *
from datetime import datetime
# загрузил все нужные библеотеки ↑

# поставил статус логирования
logging.basicConfig(filename="log.logs", level=logging.INFO)

# с помощью библиотеки datetime, добавил переменную с нынешним временем
now = datetime.now()      

# с помощью библиотеки datetime, добавил переменную с нынешним днем недели, используя прошлую переменную
week = datetime.weekday(now)

# создаю приложение, так же обозначаю где находятся файлы html
app = Flask(__name__, template_folder='templates')

# создаю главную вьюшку
@app.route("/")
def general_page():
    '''
    тут мы берем функцию из utilits.py 
    со всеми завтрашними уроками, 
    завтрашними потому что мы добавляем +1 
    ко дню в входе функции, и возвращаем
    html страницу со всеми данными
    '''
    table = day_week_data(week+1)
    logging.info("Главная страница: принята")
    return render_template("index.html", table=table)
# эта вьюшка обозначает ошибку
@app.errorhandler(500)
def not_found(error):
    logging.error("Главная страница: не принята")
    return "Ошибка: 500, проблема с импортом данных", 500


# создаю вьюшку поиска
@app.route("/search/")
def search_page():
    '''
    тут мы берем функцию из utilits.py 
    со всеми уроками указанные в поисковике
    сайта, и возвращаем в другой файл html
    все уроки с значением в поисковой строке,
    или с "s" можно сказать
    '''
    query = request.args.get('s') 
    posts = search_for_lesson(query)
    logging.info("Поисковая страница: принята")
    return render_template("search_page.html", posts=posts, query=query)
# эта вьюшка обозначает ошибку
@app.errorhandler(500)
def not_found(error):
    logging.error("Поисковая страница: не принята")
    return "Ошибка: 500, проблема с импортом данных", 500

app.run()