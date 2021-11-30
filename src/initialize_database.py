from database_connection import get_db_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists Users;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE Users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT);
    ''')

    cursor.execute('''
        CREATE TABLE Recipes (
            id INTEGER PRIMARY KEY,
            name TEXT
            user_id INTEGER);
    ''')

    cursor.execute('''
        CREATE TABLE Ingredients (
            name TEXT,
            amount TEXT,
            recipe_id INTEGER);
    ''')

    connection.commit()


def initialize_database():
    connection = get_db_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
