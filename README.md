# freelanceTask3v2

[RU] Скрипт поиска в базе данных. ЗАДАЧА: сделать скрипт python поиска в базе данных числовых значений. Скрипт берет числовое значение с текстового файла или же с базы 1 и ищет совпадение в базе 2. При совпадении сохраняет обе строки в текстовом файле.

## Требования:
* pip inslall -r requirements.txt
* создать файл config.py для хранения данных, необходимых для соединения с сервером

## Примеры использования
##### Установка соединения с сервером:
try:
    connection = pymysql.connect(
        host=host,
# идет после 127.0.0.1: в сервере
        port=3306,  
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor

# данные для соединения заносятся в файл config.py
# если база данных находится на локальной машине, то: "local_host" либо "127.0.0.1" иначе: ip-адрес хостинга
# заменить на нужное значение (127.0.0.1) 
host = "127.0.0.1"  
# логин пользователя (root)
user = "root"  
# пароль(root)
password = "root"  
# имя базы даных
db_name = "first"  

##### Создание базы данных:
# Необходима для импорта данных из текстового файла secondText.txt. После первого использования - "закоментить", иначе будет писать, что таблица уже существует
def createTable():
    with connection.cursor() as cursor:
# Пишем название таблицы, в скобках перечисляем названия полей и тип переменных
        create_table3 = "CREATE TABLE thirdtable(id int, i1 int, numeric_value1 float, i2 int, numeric_value2 float);"
        cursor.execute(create_table3)
        print("Таблица3 создана успешно...")

##### взять значения из текстового файла firstText.txt
def open_text1():
# Если файл находится не в проекте, то писать полный путь: "C:/Users/Александр/OneDrive/Рабочий стол/python/FreelanceTask2/freelanceTask3/firstText.txt" (использ.:'/'!)
    file1 = open("firstText.txt", encoding='utf-8')
    file1_read = list(file1.read().split()) 
# Данные в файле должны быть записаны в ожидаемом формате: '5' и '5.0' это разные строки
    print("Взяты значения из текстового файла")
    file1.close()
    return file1_read

##### Взять ВСЕ данные из базы1 (таблицы firsttable) и занести в список со словарями date_from_table1
def open_base1():
    with connection.cursor() as cursor:
# firsttable - название первой таблицы без 'кавычек'
        select_all_rows1 = "SELECT * FROM firsttable"  
        cursor.execute(select_all_rows1)
        rows1 = cursor.fetchall()
        date_from_table1 = rows1
# При необходимости вызова значения из списка словарей имя ключа писать 'в кавычках'
        # print(date_from_table1[0]['id'])  
        print("Взяты значения из базы 1")
        return date_from_table1
