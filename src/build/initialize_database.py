from build.database_connection import DatabaseConnection


def drop_all_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""drop table if exists user;""")
    cursor.execute("""drop table if exists sudoku;""")
    cursor.execute("""drop table if exists solution;""")

    connection.commit()


def create_all_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username text
        ); """)

    cursor.execute("""
        CREATE TABLE sudoku (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            initial_setup TEXT,
            answer TEXT,
            difficulty TEXT
        ); """)

    cursor.execute("""
        CREATE TABLE solution (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            sudoku_id INTEGER,
            is_correct INTEGER,
            time INTEGER,
            points INTEGER,
            FOREIGN KEY(user_id) REFERENCES user(id),
            FOREIGN KEY(sudoku_id) REFERENCES sudoku(id)
        ); """)

    connection.commit()


def initialize_database():
    db_conn = DatabaseConnection()
    connection = db_conn.connect_to_database()

    drop_all_tables(connection)
    create_all_tables(connection)

    db_conn.close_database_connection()


if __name__ == "__main__":
    initialize_database()
