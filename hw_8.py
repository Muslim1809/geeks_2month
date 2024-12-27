import sqlite3
def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection
def create_table(connection,sql): #создание таблицы
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_country(connection,country):#добавление стран
    try:
        sql = '''INSERT INTO countries 
        (title) 
        VALUES (?)'''
        cursor = connection.cursor()
        cursor.execute(sql,country)
        connection.commit()

    except sqlite3.Error as e:
        print(e)

def insert_city(connection,city):#добавление городов
    try:
        sql = '''INSERT INTO cityes
        (title,area) 
        VALUES (?,?)'''
        cursor = connection.cursor()
        cursor.execute(sql,city)
        connection.commit()

    except sqlite3.Error as e:
        print(e)


def insert_student(connection, student):  # добавление студентов
    try:
        sql = '''INSERT INTO students
        (first_name,last_name) 
        VALUES (?,?)'''
        cursor = connection.cursor()
        cursor.execute(sql, student)
        connection.commit()

    except sqlite3.Error as e:
        print(e)


def stu_print(connection,city_id):  # общий вывод
    try:
        sql = (f'SELECT first_name,last_name,cityes.title, area, countries.title FROM (cityes JOIN students ON cityes.id = students.city_id) JOIN countries '
               f'ON countries.id = cityes.country_id WHERE city_id = {city_id}')
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print(e)

def city_print(connection): #вывод городов и их айди
    try:
        sql = '''SELECT id,title FROM cityes '''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


sql_to_create_countries_table = '''
    CREATE TABLE countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL
)
'''

sql_to_create_cityes_table = '''
    CREATE TABLE cityes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    area FLOAT(10,2) NOT NULL DEFAULT 0,
    country_id INT DEFAULT NULL
    REFERENCES countries (id)
)
'''

sql_to_create_students_table = '''
    CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    city_id INT DEFAULT NULL
    REFERENCES cityes (id)

)
'''


connect_to_db = create_connection('''hom.db''')
if connect_to_db is not None:
    # create_table(connect_to_db,sql_to_create_countries_table)
    # create_table(connect_to_db,sql_to_create_cityes_table)
    # create_table(connect_to_db,sql_to_create_students_table)
    # insert_country(connect_to_db,('Kyrgyzstan',))
    # insert_country(connect_to_db,('Uzbekistan',))
    # insert_country(connect_to_db,('Kazakhstan',))
    # insert_city(connect_to_db,('Dublin',40000.43))
    # insert_city(connect_to_db, ('Bishkek', 5300.7))
    # insert_city(connect_to_db, ('Moscow', 12050.67))
    # insert_city(connect_to_db, ('Batken', 80000.23))
    # insert_city(connect_to_db, ('New-York', 99000.12))
    # insert_city(connect_to_db, ('Abu-Dabi', 60400.98))
    # insert_city(connect_to_db, ('Paris', 12300.4))

    # insert_student(connect_to_db, ('Kadyr','Abdillaev'))
    # insert_student(connect_to_db, ('Azat', 'Victorev'))
    # insert_student(connect_to_db, ('Abdymurat', 'Gaziev'))
    # insert_student(connect_to_db, ('Aleksei', 'Bondarev'))
    # insert_student(connect_to_db, ('Nurlan', 'Toktobekov'))
    # insert_student(connect_to_db, ('Duisho', 'Kudayarov'))
    # insert_student(connect_to_db, ('Malika', 'Isakbaeva'))
    # insert_student(connect_to_db, ('Aliya', 'Saipidinova'))
    # insert_student(connect_to_db, ('Nikita', 'Ten'))
    # insert_student(connect_to_db, ('Stella', 'Thai'))
    # insert_student(connect_to_db, ('Victor', 'Tsoi'))
    # insert_student(connect_to_db, ('Billy', 'Jean'))
    # insert_student(connect_to_db, ('Michael', 'Jackson'))
    # insert_student(connect_to_db, ('Tom', 'Crusenko'))
    # insert_student(connect_to_db, ('Aleksei', 'Titov'))
    # insert_student(connect_to_db, ('Sergei', 'Bondarchuk'))

    connect_to_db.close()