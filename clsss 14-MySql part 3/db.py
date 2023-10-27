import pymysql

def mysqlconnect():

    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='owais381', 
        db='classicmodels',
        cursorclass=pymysql.cursors.DictCursor
    )
    cur = conn.cursor()
    return conn, cur

def disconnect(conn):
    conn.close()

if __name__ == "__main__":
    connection, cursor = mysqlconnect()
    

    cursor.execute("SELECT * FROM your_table")
    result = cursor.fetchall()
    print(result)
    

    disconnect(connection)
