#tell me about yourself page DB objects
import sqlite3
from sqlite3 import Error
def sql_connection():
    try:
        conn = sqlite3.connect("website_db.db")
        print ("Connection Established: Database created in memory")
        return conn
    except Error:
        print(Error)

def sql_table(conn):
    cursorObj = conn.cursor()
    cursorObj.execute("Create Table testWebDB(last_name, first_name, favorite_color, favorite_animal)")
    conn.commit()


con = sql_connection()
sql_table(con)

#firstname =

#lastname =
