import sqlite3
# importing sqlite module 
con = sqlite3.connect("sqlite1.db")
#connecting OR connecting and creating database file in same path as py file

# con.execute('''
#     Create table student(
#         st_id INT AUTO_INCREMENT PRIMARY KEY,
#         st_name VARCHAR(50),
#         st_class VARCHAR(10),
#         st_email VARCHAR(30)
# )
# ''')
# creating table and passing column names and data structure that they will carry

# ins = '''
#     insert into student (st_name,st_class,st_email) VALUES 
#     ('ABISH','12TH',"abishshaikh764@gmail.com"),
#     ('BISH','12TH',"bishshaikh764@gmail.com"),
#     ('ISH','12TH',"ishshaikh764@gmail.com"),
#     ('SH','12TH',"shshaikh764@gmail.com")
# '''
# # creating the insert query in variable

# con.execute(ins)
# # executing the insert query using execute function and passing our variable

# con.commit()
# # to make changes in to database you have to commit it

data = con.execute('SELECT * FROM student')   #(limit 0,1) limit 1st para= start point, 2nd para= how many row
# making variable for executing our select query and selecting everything from student table

for n in data:
    # print(n)    # to print everything in tuple data structure use this for loop
    print(n[0],' ',n[1],' ',n[2],' ',n[3])      # to print and iterate from tuple 

search = con.execute("SELECT * FROM student where st_name like '%T%'")   #putting name to search or filter
for n in search:
    print(n)









# con.close()
# closing file
