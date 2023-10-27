import pymysql

def mysqlconnect():
    try:
        # To connect to the MySQL database
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='owais381',
            db='classicmodels',
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Connected to the database successfully!")
        return conn
    except pymysql.MySQLError as e:
        print(f"Error connecting to the database: {e}")
        return None

def disconnect(conn):
    if conn:
        conn.close()
        print("Connection closed.")

# Driver Code
if __name__ == "__main":
    connection = mysqlconnect()
    if connection:
        # Perform database operations here
        disconnect(connection)
