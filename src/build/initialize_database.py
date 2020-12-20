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
            name TEXT,
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
            FOREIGN KEY(user_id) REFERENCES user(id),
            FOREIGN KEY(sudoku_id) REFERENCES sudoku(id)
        ); """)

    connection.commit()


def add_sudokus_to_database(connection):
    sudoku_repo = SudokuRepository(connection)
    sudokus = []

    sudokus.append(Sudoku('Easy 1',
                          '800930002009000040702100960200000090060000070070006005027008406030000500500062008',
                          '846937152319625847752184963285713694463859271971246385127598436638471529594362718',
                          'easy'))
    sudokus.append(Sudoku('Easy 2',
                          '000006080009105372080700016000000034000351000730000000610008020823904600070600000',
                          '157236489469185372382749516591867234246351798738492165614578923823914657975623841',
                          'easy'))
    sudokus.append(Sudoku('Easy 3',
                          '830029000090700060400010200048002019009000400120900350004060007050001020000350041',
                          '836529174291743865475816293548632719369175482127984356914268537753491628682357941',
                          'easy'))
    sudokus.append(Sudoku('Medium 1',
                          '009000000427060098000290370005000030003519600040000200032076000850030724000000900',
                          '369758412427163598518294376795642831283519647641387259932476185856931724174825963',
                          'medium'))
    sudokus.append(Sudoku('Medium 2',
                          '020408100107000008060003070200006300080000040003240005050800090800000701002507080',
                          '529478136137659428468123579245986317681735942973241865756814293894362751312597684',
                          'medium'))
    sudokus.append(Sudoku('Medium 3',
                          '006300000420000600070641300000000030030150070060207000005718060002000017000003800',
                          '156392748423875691879641325791486532238159476564237189945718263382564917617923854',
                          'medium'))
    sudokus.append(Sudoku('Hard 1',
                          '000500070020034008001020405070003000609000301000800020904050800800690050050007000',
                          '493518672526734198781926435278163549649275381315849726964352817837691254152487963',
                          'hard'))
    sudokus.append(Sudoku('Hard 2',
                          '900000486000090100200506000016035040020000060090680230000908004002050000649000008',
                          '953721486467893152281546973716235849328419765594687231175968324832154697649372518',
                          'hard'))
    sudokus.append(Sudoku('Hard 3',
                          '008003700905700000030009000023004870000002000079380240000900020000007305006500400',
                          '268453719945718632731269584523194876814672953679385241457936128192847365386521497',
                          'hard'))
    for sudoku in sudokus:
        sudoku_repo.create(sudoku)


def initialize_database(test=False):
    db_conn = DatabaseConnection(test)
    connection = db_conn.connect_to_database()

    drop_all_tables(connection)
    create_all_tables(connection)
    add_sudokus_to_database(connection)

    db_conn.close_database_connection()


if __name__ == "__main__":
    initialize_database()
