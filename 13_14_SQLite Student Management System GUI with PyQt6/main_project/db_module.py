import db_settings
import sqlite3
import mysql.connector


class UniversalDatabase:
    def __init__(self):
        self.db_type = db_settings.DATABASE_TYPE
        self.host = db_settings.HOST
        self.user = db_settings.USER
        self.password = db_settings.PASSWORD
        self.database = db_settings.DATABASE
        self.connection = None
        self.cursor = None

    def connect(self):
        if self.db_type == 'SQLITE':
            self.connection = sqlite3.connect(self.database)
        elif self.db_type == 'MYSQL':
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, values):

        if self.db_type == 'SQLITE':
            query = query.replace('%s', '?')

        self.cursor.execute(query, values)
        self.connection.commit()

    def fetch_data(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()


