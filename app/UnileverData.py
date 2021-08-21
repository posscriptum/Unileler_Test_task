import datetime, random, sqlite3

"""класс, формирующий элемент"""
class DataItem:

    def __init__(self, date, random_value):
        self.date = date
        self.randomValue = random_value

"""массив, в который все складываем"""
global arrayUnilever
arrayUnilever = []

"""Коннект к базе"""
conn = sqlite3.connect("database_unilever")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS store_unilever
                  (years integer, months integer, days integer,
                  hours integer, minutes integer, seconds integer,
                  random_number integer)
               """)

"""Заполнение элементами по 1000 штук в массив и в базу"""
def filling_1000_items(range_start_val):
    for fill_number in range(range_start_val, range_start_val + 1000):

        _date = datetime.datetime(2000, 1, 1, 0, 0, 0)
        if fill_number == 1:
            _date = datetime.datetime(2020, 1, 1, 0, 0, 0)
        else:
            _date = arrayUnilever[-1].date + datetime.timedelta(days=1)

        _random_number = random.randint(100, 200)
        _obj_item = DataItem(_date, _random_number)
        arrayUnilever.append(_obj_item)

        g = """INSERT INTO store_unilever (years, months, days, hours, minutes, seconds, random_number) VALUES (""" + str(_date.year) + ", " + str(_date.month) + ", " + str(_date.day) + ", " + str(_date.hour) + ", " + str(_date.minute) + ", " + str(_date.second) + ", " + str(_random_number) + ")"
        cursor.execute(g)
        conn.commit()

"""Начало бизнес логики"""
sql = "SELECT * FROM store_unilever"
cursor.execute(sql)
records = cursor.fetchall()

"""если программа запускается первый раз - заполняем базу, если нет, то на каждый существующий элемент создаем еще 1000"""
"""ОСТОРОРЖНО!!!! ОЧЕНЬ МНОГО ВЫЧИСЛЕНИЙ, НО ТАК ПО ЗАДАНИЮ"""
if (len(records) == 0):
    filling_1000_items(1)
else:
    for every_item in records:
        _date = datetime.datetime(every_item[0], every_item[1], every_item[2], every_item[3], every_item[4], every_item[5])
        _obj_item = DataItem(_date, every_item[6])
        arrayUnilever.append(_obj_item)
    for every_item in records:
        filling_1000_items(2)

cursor.close()