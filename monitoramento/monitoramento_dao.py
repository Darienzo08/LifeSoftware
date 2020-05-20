import sqlite3
from model.disciplina import Disciplina
from contextlib import closing

db_name = "monitoramentos.db"
model_name = "monitoramento"


def con():
    return sqlite3.connect(db_name)


def listar():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(f"SELECT id, mensagem FROM {model_name}")
        rows = cursor.fetchall()
        registros = []
        for (id, mensagem) in rows:
            monitoramento = Monitoramento.criar_com_id(id, mensagem)
            if monitoramento != None:
                registros.append(monitoramento)
        return registros


def consultar(id):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(
            f"SELECT id, mensagem FROM {model_name} WHERE id = ?", (int(id),))
        row = cursor.fetchone()
        if row == None:
            return None
        return Disciplina.criar_com_id(row[0], row[1])


def consultar_por_mensagem(mensagem):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute(
            f"SELECT id, mensagem FROM {model_name} WHERE mensagem = ?", (mensagem,))
        row = cursor.fetchone()
        if row == None:
            return None
        return Monitoramento.criar_com_id(row[0], row[1])


def cadastrar(monitoramento):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"INSERT INTO {model_name} (mensagem) VALUES (?)"
        result = cursor.execute(
            sql, (monitoramento.mensagem))
        connection.commit()
        if cursor.lastrowid:
            monitoramento.associar_id(cursor.lastrowid)
            return monitoramento
        else:
            return None


def alterar(monitoramento):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"UPDATE {model_name} SET mensagem = ? WHERE id = ?"
        cursor.execute(
            sql, (monitoramento.id, monitoramento.mensagem, monitoramento.professor_id))
        connection.commit()
        if cursor.rowcount > 0:
            return True
        return False


def remover(monitoramento):
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        sql = f"DELETE FROM {model_name} WHERE id = ?"
        cursor.execute(sql, f"{monitoramento.id}")
        connection.commit()
        if cursor.rowcount > 0:
            return True
        return False
