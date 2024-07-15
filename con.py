import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, user='', passwd='', database='', host=''):
        self.user = user
        self.passwd = passwd
        self.database = database
        self.host = host
        self.connection = None

    def conectar(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.passwd,
                database=self.database
            )
            if self.connection.is_connected():
                return True
        except Error as e:
            return {"error": str(e)}

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()

    def read_students(self):
        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM estudantes")
                rows = cursor.fetchall()
                return rows
        except Error as e:
            return {"error": str(e)}

    def read_students_paginate(self, page=1, per_page=10):
        try:
            offset = (page - 1) * per_page
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM estudantes")
                total_records = cursor.fetchone()[0]
                cursor.execute(f"SELECT * FROM estudantes LIMIT {per_page} OFFSET {offset}")
                rows = cursor.fetchall()
                return rows, total_records
        except Error as e:
            return {"error": str(e)}, 0

    def atualizar_estudante_no_banco(self, student_id, data):
        try:
            with self.connection.cursor() as cursor:
                sql = "UPDATE estudantes SET NAME=%s, BRANCH=%s, ROLL=%s, SECTION=%s, AGE=%s WHERE ID=%s"
                cursor.execute(sql, (data['name'], data['branch'], data['roll'], data['section'], data['age'], student_id))
                self.connection.commit()
                return True
        except Error as e:
            return {"error": str(e)}

    def deletar_estudante(self, student_id):
        try:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM estudantes WHERE ID=%s"
                cursor.execute(sql, (student_id,))
                self.connection.commit()
                return True
        except Error as e:
            return {"error": str(e)}

    def inserir_estudante(self, data):
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO estudantes (NAME, BRANCH, ROLL, SECTION, AGE) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (data['name'], data['branch'], data['roll'], data['section'], data['age']))
                self.connection.commit()
                return True
        except Error as e:
            return {"error": str(e)}
