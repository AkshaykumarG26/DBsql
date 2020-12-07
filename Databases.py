import sqlite3
# from sqlite3 import connect
try:
    my_connect = sqlite3.connect("Akshay.db")
    my_execution = my_connect.execute ("""create table Netzwerk('student' text, 'age' integer)""")
    
except Exception as e:
    print(e)

finally:
    my_connect.commit()
    my_connect.close()