import sqlite3
# importing sqlite module 
con = sqlite3.connect("sqlite1.db")
#connecting OR connecting and creating database file in same path as py file

st_id = input('enter the id')
# getting input for id to delete

con.execute('DELETE FROM student where st_id='+st_id) 
# writing delete query  and passing input value 
con.commit()
con.close()