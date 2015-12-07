import sqlite3
import os

class DbHelper:

    def create_table_on_db(self):

        if not os.path.isfile('database.db'):
            open('database.db', 'w')

        conn = sqlite3.connect('database.db')
        conn.execute('''CREATE TABLE IF NOT EXISTS ftable
                    (ID INTEGER PRIMARY KEY AUTOINCREMENT   NOT NULL,
                    name           TEXT    NOT NULL);''')
        conn.close()


    def insert_value_in_table(self,value):
        conn = sqlite3.connect('database.db')
        conn.execute('''INSERT INTO ftable (name) VALUES (?)''', [value])
        conn.commit()
        print('{0}->Executed '.format(value))
        conn.close()

    def drop_table():
        conn = sqlite3.connect('database.db')
        conn.execute('''DROP TABLE ftable''')
        conn.commit()
        print('table dropped successfully')
        conn.close()
