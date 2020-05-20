import sqlite3

db_name = " monitoramento.db"
table_name = "monitoramento"

sql_create_table = f"CREATE TABLE IF NOT EXISTS {table_name} (id integer PRIMARY KEY AUTOINCREMENT, mensagem text NOT NULL UNIQUE)"


def createTable(cursor, sql):
    cursor.execute(sql)


def popularDb(cursor, mensagem):
    sql = f"INSERT INTO {table_name} (mensagem) VALUES (?)"
    cursor.execute(sql, (mensagem))


def init():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    createTable(cursor, sql_create_table)
    try:
        popularDb(cursor, "Aluno")
        popularDb(cursor, "Aluno 2")
        popularDb(cursor, "Aluno 3")
        popularDb(cursor, "Aluno 4")
    except:
        pass
    cursor.close()
    connection.commit()
    connection.close()


init()
