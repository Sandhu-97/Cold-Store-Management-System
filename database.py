import sqlite3 as sql

user_conn = sql.connect('db/user.db')
inventory_conn = sql.connect('db/inventory.db')
sales_conn = sql.connect('db/sales.db')

user_cursor = user_conn.cursor()
inventory_cursor = inventory_conn.cursor()
sales_cursor = sales_conn.cursor()

def create_user_table():
    try:
        user_cursor.execute('CREATE TABLE USERS (ID INT, NAME VARCHAR(50), PASSWORD VARCHAR(50), IS_MANAGER INT)')
        print('table created!')
    except:
        print("user_table cannot be created")



user_conn.close()
inventory_conn.close()
sales_conn.close()