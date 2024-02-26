import sqlite3


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection


def create_table(connection, create_table_sql):
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def insert_product(connection, product):
    sql = '''INSERT INTO products
    (product_title, price, quantity)
    VALUES (?, ?, ?)'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)
#
def update_product(connection, product):
    sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def update_price(connection, product):
    sql = '''UPDATE products SET price = ? WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)
#
def delete_product(connection, id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def select_all_products(connection):
    sql = '''SELECT * FROM products'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_products(connection, limit_1, limit_2):
    sql = '''SELECT * FROM products WHERE price < ? and quantity > ?'''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, (limit_1, limit_2))
        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)


def search_products_by_title(connection, keyword):
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM products WHERE product_title LIKE ?', (f'%{keyword}%',))
        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)

sql_create_table = '''
CREATE TABLE products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title TEXT(200) NOT NULL,
    price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''


my_connection = create_connection("hw7.db")
if my_connection:
    print("Successfully connected!")
    # create_table(my_connection, sql_create_table)
    # insert_product(my_connection, ('Туалетная бумага ZEWA', 200.0, 500))
    # insert_product(my_connection, ('Чипсы Lays', 80.0, 15))
    # insert_product(my_connection, ('Вода Legenda', 25.0, 300))
    # insert_product(my_connection, ('Чипсы Pringles', 180.0, 20))
    # insert_product(my_connection, ('Вода Asu', 21.2, 200))
    # insert_product(my_connection, ('Чипсы Пир', 75.82, 120))
    # insert_product(my_connection, ('Молоко', 80.0, 100))
    # insert_product(my_connection, ('Сливки', 200.0, 50))
    # insert_product(my_connection, ('Черный хлеб', 40.09, 30))
    # insert_product(my_connection, ('Белый хлеб', 32.0, 50))
    # insert_product(my_connection, ('Pepsi', 40.55, 500))
    # insert_product(my_connection, ('Coca-Cola', 40.4, 500))
    # insert_product(my_connection, ('Fanata', 40.9, 230))
    # insert_product(my_connection, ('Sprite', 40.4, 300))
    # insert_product(my_connection, ('7-UP', 40.6, 300))
    # insert_product(my_connection, ('Mirinda', 40.12, 100))
    # update_product(my_connection, (120, 7))
    # update_price(my_connection, (90.5, 2))
    # delete_product(my_connection, 5)
    # select_all_products(my_connection)
    # select_products(my_connection, 100, 5)
    search_products_by_title(my_connection, 'Чипсы')
    my_connection.close()