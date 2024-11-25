import sqlite3
from sqlite3 import Error


class Database:
    def __init__(self):
        self.create_tables()

    def create_connection(self):
        try:
            conn = sqlite3.connect('../passwords.db')
            return conn
        except Error as e:
            print(e)
            return None

    def create_tables(self):
        conn = self.create_connection()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS passwords (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        usuario TEXT NOT NULL,
                        contrasena TEXT NOT NULL,
                        servicio TEXT NOT NULL
                    )
                ''')
                conn.commit()
            except Error as e:
                print(e)
            finally:
                conn.close()

    def add_password(self, usuario, contrasena, servicio):
        conn = self.create_connection()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO passwords (usuario, contrasena, servicio)
                    VALUES (?, ?, ?)
                ''', (usuario, contrasena, servicio))
                conn.commit()
                return True
            except Error as e:
                print(e)
                return False
            finally:
                conn.close()

    def get_all_passwords(self):
        conn = self.create_connection()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM passwords')
                return cursor.fetchall()
            except Error as e:
                print(e)
                return []
            finally:
                conn.close()

    def update_password(self, id, usuario, contrasena, servicio):
        conn = self.create_connection()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE passwords
                    SET usuario = ?, contrasena = ?, servicio = ?
                    WHERE id = ?
                ''', (usuario, contrasena, servicio, id))
                conn.commit()
                return True
            except Error as e:
                print(e)
                return False
            finally:
                conn.close()

    def delete_password(self, id):
        conn = self.create_connection()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM passwords WHERE id = ?', (id,))
                conn.commit()
                return True
            except Error as e:
                print(e)
                return False
            finally:
                conn.close()