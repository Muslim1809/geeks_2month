import sqlite3


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)  # Corrected connection method
    except sqlite3.Error as e:
        print(f'{e} in CREATE_CONNECTION')
    return connection


def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(f'{e} in CREATE_TABLE function')


def insert_products(connection, product):
    try:
        sql = '''INSERT INTO products 
                 (product_title, price, quantity)
                 VALUES (?, ?, ?)'''  # Corrected typo in column name
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(f'{e} in INSERT_PRODUCTS function')


def update_quantity(connection, product):
    try:
        sql = '''UPDATE products SET quantity=? WHERE id=?'''  # Corrected SQL query
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(f'{e} in UPDATE_QUANTITY function')


def update_price(connection, product):
    try:
        sql = '''UPDATE products SET price=? WHERE id=?'''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(f'{e} in UPDATE_PRICE function')


def delete_by_id(connection, id):
    try:
        sql = '''DELETE FROM products WHERE id=?'''
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as e:
        print(f'{e} in DELETE_BY_ID function')


def select_all(connection):
    try:
        sql = '''SELECT * FROM products'''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f'{e} in SELECT_ALL function')


def select_by_price_and_quantity(connection, price_limit, quantity_limit):
    try:
        sql = '''SELECT * FROM products
                 WHERE price <= ? AND quantity >= ?'''
        cursor = connection.cursor()
        cursor.execute(sql, (price_limit, quantity_limit))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f'{e} in SELECT_BY_PRICE_AND_QUANTITY function')


def select_by_name(connection, name):
    try:
        sql = '''SELECT * FROM products
                 WHERE product_title LIKE ?'''
        cursor = connection.cursor()
        cursor.execute(sql, (f"%{name}%",))  # Added parameterized query
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f'{e} in SELECT_BY_NAME function')


sql_to_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price REAL NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''


my_connection = create_connection('hw.db')

if my_connection:
    print('Connected successfully!')

    # create_table(my_connection, sql_to_create_products_table)
    # insert_products(my_connection, ('Шоколад', 120.50, 7))
    # insert_products(my_connection, ('Мандарин', 129.99, 3))
    # insert_products(my_connection, ('Виноград', 99.99, 10))
    # insert_products(my_connection, ('Печенья', 150.40, 8))
    # insert_products(my_connection, ('Курут', 145.50, 5))
    # insert_products(my_connection, ('Кымыз', 89.90, 12))
    # insert_products(my_connection, ('Бозо', 100.00, 10))
    # insert_products(my_connection, ('Чалап', 100.00, 7))
    # insert_products(my_connection, ('Кофе', 30.30, 15))
    # insert_products(my_connection, ('Молоко', 35.50, 4))
    # insert_products(my_connection, ('Чай ', 45.80, 9))
    # insert_products(my_connection, ('Сахар', 43.30, 3))
    # insert_products(my_connection, ('Соль', 150.70, 4))
    # insert_products(my_connection, ('Чипсы', 145.99, 7))
    # insert_products(my_connection, ('Яблоко', 120.00, 2))
    #
    # update_price(my_connection, ( 120.50, 7))
    # update_quantity(my_connection, ( 10, 11))
    # delete_by_id(my_connection, 3)
    select_all(my_connection)
    select_by_price_and_quantity(my_connection, 100, 5)