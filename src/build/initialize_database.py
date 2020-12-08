from build.database_connection import DatabaseConnection
from repositories.sudoku_repository import SudokuRepository
from entities.sudoku import Sudoku


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


def add_sudokus_to_table(connection):
    sudoku_repo = SudokuRepository()
    sudokus = []

    sudokus.append(Sudoku('800930002009000040702100960200000090060000070070006005027008406030000500500062008',
                          '846937152319625847752184963285713694463859271971246385127598436638471529594362718',
                          'easy'))
    sudokus.append(Sudoku('000006080009105372080700016000000034000351000730000000610008020823904600070600000',
                          '157236489469185372382749516591867234246351798738492165614578923823914657975623841',
                          'easy'))
    sudokus.append(Sudoku('830029000090700060400010200048002019009000400120900350004060007050001020000350041',
                          '836529174291743865475816293548632719369175482127984356914268537753491628682357941',
                          'easy'))
    sudokus.append(Sudoku('009000000427060098000290370005000030003519600040000200032076000850030724000000900',
                          '369758412427163598518294376795642831283519647641387259932476185856931724174825963',
                          'medium'))
    sudokus.append(Sudoku('000500070020034008001020405070003000609000301000800020904050800800690050050007000',
                          '493518672526734198781926435278163549649275381315849726964352817837691254152487963',
                          'hard'))
    for sudoku in sudokus:
        sudoku_repo.create(sudoku)


def initialize_database():
    db_conn = DatabaseConnection()
    connection = db_conn.connect_to_database()

    drop_all_tables(connection)
    create_all_tables(connection)
    add_sudokus_to_table(connection)

    db_conn.close_database_connection()


if __name__ == "__main__":
    initialize_database()
