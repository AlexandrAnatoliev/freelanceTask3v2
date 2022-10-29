# freelanceTask3v2

# https://freelance.ru/projects/skript-poiska-v-baze-dannih-1444163.html
# Murathan Kapurov Москва Дата регистрации: 04.06.2014
# Дата публикации:	2022-09-30 16:35

# Скрипт поиска в базе данных
#
# Задача
# Нужно делать скрипт python поиска в базе данных числовых значений.
# Скрипт берет числовое значение с текстового файла или же с базы 1 и ищет совпадение в базе 2.
# При совпадении сохраняет обе строки в текстовом файле.

# Сделал до-сюда.
# Необходимо сделать: чистовой вариант, документацию и гитхаб
# изменение1

# Создать скрипт импорта в базу данных из текстового файла. !!! не смог!!! версия mariaBD не подддерживает эту функцию
# Создать базу данных в формате mysql или др.

import pymysql
from config import host, user, password, db_name

# создание базы данных thirdTable для импорта данных из текстового файла secondText.txt
# после первого использования - "закоментить", иначе будет писать, что таблица уже существует
def createTable():
    with connection.cursor() as cursor:
        create_table3 = "CREATE TABLE thirdtable(id int, i1 int, numeric_value1 float, i2 int, numeric_value2 float);"
        cursor.execute(create_table3)
        print("Таблица3 создана успешно...")

# взять значения из текстового файла firstText.txt
def open_text1():
    file1 = open("firstText.txt", encoding='utf-8')  # если файл находится не в проекте, то писать полный путь:
    # "C:/Users/Александр/OneDrive/Рабочий стол/python/FreelanceTask2/freelanceTask3/firstText.txt" (использ.:'/'!)
    file1_read = list(file1.read().split())  # сохраняет данные из файла в список в str формате
    # данные должны быть записаны в ожидаемом формате: '5' и '5.0' это разные строки
    print("Взяты значения из текстового файла")
    file1.close()  # закрывает файл
    return file1_read
# удалить позже

# взять ВСЕ данные из базы1 (таблицы firsttable) и занести в список со словарями date_from_table1
def open_base1():
    with connection.cursor() as cursor:
        select_all_rows1 = "SELECT * FROM firsttable"  # firsttable - название первой таблицы без 'кавычек'
        cursor.execute(select_all_rows1)
        rows1 = cursor.fetchall()
        date_from_table1 = rows1  # список словарей
        # print(date_from_table1[0]['id'])  # вызов значения из списка словарей !имя ключа - 'в кавычках'
        print("Взяты значения из базы 1")
        return date_from_table1

# взять ВСЕ данные из базы2 (таблицы secondtable) и занести в список со словарями date_from_table2
def open_base2():
    with connection.cursor() as cursor:
        select_all_rows2 = "SELECT * FROM secondtable"  # secondtable - название второй таблицы без 'кавычек'
        cursor.execute(select_all_rows2)
        rows2 = cursor.fetchall()
        date_from_table2 = rows2  # список словарей
        # print(date_from_table2)  # вызов значения из списка словарей !имя ключа - 'в кавычках'
        print("Взяты значения из базы2")
        return date_from_table2

 # значение из текстого файла сравниваем со значениями из базы 2 (таблицы secondtable)
def text1_base2_compare():
    print("Совпадения текста 1 и базы данных 2:")
    file2.write("\nСовпадения текста 1 и базы данных 2:\n\n")
    print("id    numeric_value1  i2  numeric_value2")
    file2.write("id  numeric_value1  i2  numeric_value2\n")
    id1 = 0  # порядковый номер в таблице
    for i in range(len(file1_read)):
        for j in range(len(date_from_table2)):
            if file1_read[i] == str(date_from_table2[j]['numeric_value']):
                id1 += 1
                print(f"{id1} {file1_read[i]} {date_from_table2[j]['id']} {date_from_table2[j]['numeric_value']}")
                file2.write(f"{id1} {id1} {file1_read[i]} {date_from_table2[j]['id']} "
                            f"{date_from_table2[j]['numeric_value']}\n")

# значение из базы 1 сравниваем со значением в базе 2
def base1_base2_compare():
    print("Совпадения базы данных 1 и базы данных 2:")
    file2.write("\nСовпадения базы данных 1 и базы данных 2:\n\n")
    id1 = 0
    for i in range(len(date_from_table1)):
        for j in range(len(date_from_table2)):
            if str(date_from_table1[i]['numeric_value']) == str(date_from_table2[j]['numeric_value']):
                id1 += 1
                print("Совпадение: " + str(date_from_table1[i]) + " => " + str(date_from_table2[j]))
                file2.write(f"{id1} {date_from_table1[i]['id']} {date_from_table1[i]['numeric_value']} "
                            f"{date_from_table2[j]['id']} {date_from_table2[j]['numeric_value']}\n")

# установка соединения с сервером
try:
    connection = pymysql.connect(
        host=host,
        port=3306,  # идет после 127.0.0.1: в сервере
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Соединение успешно...")
    print("#" * 50)  # границы просто для красоты

    # здесь рабочая часть
    try:
        print("Работа программы начата")
        # createTable() создание новой таблицы для внесения данных - пока не используется
        file2 = open("secondText.txt", 'w', encoding='utf-8')  # создается файл, 'w' - запись файла
        # если файл находится не в проекте, то писать полный путь к файлу:
        # "C:/Users/Александр/OneDrive/Рабочий стол/python/FreelanceTask2/freelanceTask3/secondText.txt" (использ.:'/'!)
        file1_read = open_text1()  # берем значения из текста 1
        date_from_table1 = open_base1()  # берем значения из базы 1
        date_from_table2 = open_base2()  # берем значения из базы 2
        text1_base2_compare()  # сравниваем значения из текста 1 и базы 1 и записываем в текст 2
        base1_base2_compare()  # сравниваем значения из базы 1 и базы 2 и записываем в текст 2
        file2.close()  # закрывает файл
    finally:
        connection.close()

except Exception as ex:
    print("Нет соединения...")
    print(ex)

