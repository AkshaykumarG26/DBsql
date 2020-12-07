# Database creation and insertion



import sqlite3
import time

try:
    sqliteConn = sqlite3.connect("sql_python2.db")     #DB will create
    cursor = sqliteConn.cursor()
    print("___DB created___")

    my_execution = sqliteConn.execute ("""create table NetzwerkDB('ID' integer, 'Name' text, 'EmailId' string, 'Contact_Number' integer, 'salary' integer)""")  # Table will create

    # def insert_data_into_table():
    #     data = input("plz add the contents into table: ")
        

    
    
    sql_insert = """ INSERT INTO NetzwerkDB
                 (ID, Name, EmailId, Contact_Number, salary)
               
                VALUES 
                (1, 'Akshaykumar', 'akshay@mail.com', 123456789, 40000) """
    
    # VALUES = input("Plz enter the data: ")
    # wait = time.sleep(5)
    count = cursor.execute(sql_insert)
    sqliteConn.commit()
    print("Data has been inserted into the Table ",cursor.rowcount)
    cursor.close()


except sqlite3.Error as e:
    print("_____Failed_____", e)

finally:
    if(sqliteConn):
        sqliteConn.close()
        print("The SQL connection is closed")