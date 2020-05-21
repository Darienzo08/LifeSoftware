import sqlite3
from model.disciplina import Disciplina
from contextlib import closing

db_name = "disciplinas.db"
model_name = "disciplina"
model_name_relationship = "disciplina_aluno"


def con():
    return sqlite3.connect(db_name)


def listar():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT id, nome, professor_id FROM {model_name}")
        rows = cursor.fetchall()
        registros = []
        for (id, nome, professor_id) in rows:
            disciplina = Disciplina.criar_com_id(id, nome, professor_id)
            if disciplina != None:
                registros.append(disciplina)
        return registros


def consultar(id):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(
            f"SELECT id, nome, professor_id FROM {model_name} WHERE id = ?", (int(id),))
        row = cursor.fetchone()
        if row == None:
            return None
        return Disciplina.criar_com_id(row[0], row[1], row[2])


def consultar_por_nome(nome):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(
            f"SELECT id, nome, professor_id FROM {model_name} WHERE nome = ?", (nome,))
        row = cursor.fetchone()
        if row == None:
            return None
        return Disciplina.criar_com_id(row[0], row[1], row[2])


def cadastrar(disciplina):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"INSERT INTO {model_name} (nome, professor_id) VALUES (?, ?)"
        result = cursor.execute(
            sql, (disciplina.nome, disciplina.professor_id))
        connection.commit()
        if cursor.lastrowid:
            disciplina.associar_id(cursor.lastrowid)
            return disciplina
        else:
            return None


def alterar(disciplina):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"UPDATE {model_name} SET id = ?, nome = ? WHERE professor_id = ?"
        cursor.execute(
            sql, (disciplina.id, disciplina.nome, disciplina.professor_id))
        connection.commit()
        if cursor.rowcount > 0:
            return True
        return False


def remover(disciplina):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"DELETE FROM {model_name} WHERE id = ?"
        cursor.execute(sql, f"{disciplina.id}")
        connection.commit()
        if cursor.rowcount > 0:
            return True
        return False

# Disciplina-aluno


def cadastrar_aluno(disciplina, aluno_id):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"INSERT INTO {model_name_relationship} (disciplina_id, aluno_id) VALUES (?, ?)"
        result = cursor.execute(sql, (disciplina, aluno_id))
        connection.commit()
        if cursor.lastrowid:
            return aluno_id, disciplina
        else:
            return None


def remover_aluno(disciplina, aluno_id):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(
            f"DELETE FROM {model_name_relationship} WHERE aluno_id = ? AND disciplina_id = ?", (aluno_id, disciplina))

        connection.commit()
        if cursor.rowcount > 0:
            return True
        return False


def consultar_alunos(disciplina):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(
            f"SELECT aluno_id FROM {model_name_relationship} WHERE disciplina_id = ?", (disciplina,))
        rows = cursor.fetchall()
        registros = []
        for aluno_id in rows:
            if aluno_id != None:
                registros.append(aluno_id[0])
        return registros
