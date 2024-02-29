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


sql_create_table = '''
CREATE TABLE country(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT(200) NOT NULL
)
'''

sql_create_table_cities = '''
CREATE TABLE cities(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT(200) NOT NULL,
    area FLOAT DEFAULT NULL,
    country_id INTEGER NOT NULL,
    FOREIGN KEY (country_id) REFERENCES country(id)
)
'''
sql_create_table_students = '''
CREATE TABLE students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT(200) NOT NULL,
    last_name TEXT(200) NOT NULL,
    city_id INTEGER NOT NULL,
    FOREIGN KEY (city_id) REFERENCES cities(id)
)
'''


def display_cities():
    conn = sqlite3.connect('hw_8.db')
    cursor = conn.cursor()
    cursor.execute('SELECT title FROM cities')
    cities = cursor.fetchall()
    print("Список городов:")
    for city in cities:
        print(city[0])
    conn.close()

def display_students_by_city(city_id):
    conn = sqlite3.connect('hw_8.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT students.first_name, students.last_name, country.title, cities.title, cities.area
        FROM students
        JOIN cities ON students.city_id = cities.id
        JOIN country ON cities.country_id = country.id
        WHERE students.city_id = ?''', (city_id,))
    students = cursor.fetchall()
    print(f"Ученики проживающие в выбранном городе:")
    for student in students:
        print(f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]}, Город: {student[3]}, Площадь города: {student[4]}")
    conn.close()

if __name__ == "__main__":
    while True:
        print("\nВы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
        display_cities()
        city_id = input("Введите id города: ")
        if city_id == '0':
            print("Программа завершена.")
            break
        else:
            try:
                city_id = int(city_id)
                display_students_by_city(city_id)
            except ValueError:
                print("Введите корректный id города.")


my_connection = create_connection("hw_8.db")
if my_connection:
    print("Successfully connected!")
    cursor = my_connection.cursor()
    # create_table(my_connection, sql_create_table)
    # create_table(my_connection, sql_create_table_cities)
    # create_table(my_connection, sql_create_table_students)


my_connection.close()