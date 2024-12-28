# Turdubaev Muslim test.
import sqlite3


def create_db():
    conn = sqlite3.connect("store.db")
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS categories (
            code TEXT PRIMARY KEY,
            title TEXT
        )
    """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS store (
            store_id INTEGER PRIMARY KEY,
            title TEXT
        )
    """
    )

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            title TEXT,
            category_code TEXT,
            unit_price REAL,
            stock_quantity INTEGER,
            store_id INTEGER,
            FOREIGN KEY (category_code) REFERENCES categories (code),
            FOREIGN KEY (store_id) REFERENCES store (store_id)
        )
    """
    )

    cur.execute(
        "INSERT OR IGNORE INTO categories (code, title) VALUES ('FD', 'Food products')"
    )
    cur.execute("INSERT OR IGNORE INTO store (store_id, title) VALUES (1, 'Asia')")
    cur.execute("INSERT OR IGNORE INTO store (store_id, title) VALUES (2, 'Globus')")
    cur.execute("INSERT OR IGNORE INTO store (store_id, title) VALUES (3, 'Spar')")

    cur.execute(
        """
        INSERT OR IGNORE INTO products (title, category_code, unit_price, stock_quantity, store_id)
        VALUES ('Chocolate', 'FD', 10.5, 129, 1)
    """
    )
    cur.execute(
        """
        INSERT OR IGNORE INTO products (title, category_code, unit_price, stock_quantity, store_id)
        VALUES ('Bread', 'FD', 2.5, 200, 2)
    """
    )
    cur.execute(
        """
        INSERT OR IGNORE INTO products (title, category_code, unit_price, stock_quantity, store_id)
        VALUES ('Milk', 'FD', 1.8, 150, 3)
    """
    )

    conn.commit()
    cur.close()
    conn.close()


def fetch_stores(cursor):
    cursor.execute("SELECT store_id, title FROM store")
    return cursor.fetchall()


def fetch_products(cursor, store_id):
    cursor.execute(
        """
        SELECT p.title, c.title, p.unit_price, p.stock_quantity 
        FROM products p
        JOIN categories c ON p.category_code = c.code
        WHERE p.store_id = ?
    """,
        (store_id,),
    )
    return cursor.fetchall()


create_db()

with sqlite3.connect("store.db") as conn:
    try:
        cur = conn.cursor()
        while True:
            print(
                "Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:"
            )

            stores = fetch_stores(cur)

            if not stores:
                print("В базе данных нет магазинов.")
                break

            for i, store in enumerate(stores, 1):
                print(f"{i}. {store[1]}")

            choice = input("Введите id магазина: ")

            if choice == "0":
                print("Выход...")
                break

            try:
                store_id = int(choice)
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите цифру.")
                continue

            if store_id < 1 or store_id > len(stores):
                print(f"Такого магазина нет. Введите число от 1 до {len(stores)}.")
                continue

            selected_store_id = stores[store_id - 1][0]
            products = fetch_products(cur, selected_store_id)

            if products:
                for product in products:
                    print(f"Название продукта: {product[0]}")
                    print(f"Категория: {product[1]}")
                    print(f"Цена: {product[2]:.2f}")
                    print(f"Количество на складе: {product[3]}")
                    print("-" * 40)
            else:
                print("В этом магазине нет продуктов.")

        cur.close()

    except sqlite3.Error as e:
        print(f"Ошибка работы с базой данных: {e}")


