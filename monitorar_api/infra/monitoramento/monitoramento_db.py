import sqlite3

db_name = " monitoramento.db"
table_name = "monitoramento"

sql_create_table = f"CREATE TABLE IF NOT EXISTS {table_name} (id integer PRIMARY KEY AUTOINCREMENT, aluno text NOT NULL UNIQUE, professor text NOT NULL UNIQUE, disciplina text NOT NULL UNIQUE)"


def createTable(cursor, sql):
    cursor.execute(sql)


def popularDb(cursor, aluno, professor, disciplina):
    sql = f"INSERT INTO {table_name} (aluno, professor, disciplina) VALUES (?, ?, ?)"
    cursor.execute(sql, (aluno, professor, disciplina))


def init():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    createTable(cursor, sql_create_table)
    try:
        popularDb(cursor, "Aluno cadastrado",
                  "Professor cadastrado", "Disciplina cadastrada")
        popularDb(cursor, "Aluno cadastrado 2",
                  "Professor cadastrado 2", "Disciplina cadastrada 2")
    except:
        pass
    cursor.close()
    connection.commit()
    connection.close()


init()
