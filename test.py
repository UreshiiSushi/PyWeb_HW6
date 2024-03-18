import sqlite3

def execute_query(query, params=()):
    with open(query, "r") as f:
        sql = f.read()
        
    with sqlite3.connect("university.db") as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    
if __name__ == "__main__":
    print(execute_query("query_01.sql"))
    print(execute_query("query_02.sql"))
    print(execute_query("query_03.sql"))
    print(execute_query("query_04.sql"))
    print(execute_query("query_05.sql"))
    print(execute_query("query_06.sql"))
    print(execute_query("query_07.sql"))
    print(execute_query("query_08.sql"))
    print(execute_query("query_09.sql"))
    print(execute_query("query_10.sql"))