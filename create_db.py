import sqlite3

def create_db():
    with open('init_db.sql') as db:
        sql = db.read()

    with sqlite3.connect('university.db') as conn:
        cur = conn.cursor()
        cur.executescript(sql)

if __name__ == '__main__':
    create_db()