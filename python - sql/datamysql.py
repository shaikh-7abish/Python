# CREATING DATABASE AND INSERT QUERY

import pymysql as mq
# importing python mysql library

obj = mq.connect(host='localhost',user='root',password='tabishshaikh764',db='school_for_learn')
# creating object to connect mysql db to code and passing parameters as (hostname,username-root,password,db)

cur = obj.cursor()
# to execute this file you need to use cursor function 

# # using try and except to handle errors if occurred
# try:
#     db = "create database school_for_learn"
#     # command for creating database as school_for_learn 
#     cur.execute(db)
#     # now executing the command using cursor
#     print('database created !')
#     #printing this to see if it happens or not
# except:
#     print('database error....')
#     # if error occurred then this will print

# tc = "create table student(st_id INT auto_increment primary key, st_name varchar(50),st_class varchar(10), st_email varchar(30))"
# # putting the query to create table in a variable

# cur.execute(tc)
# # executing the query

# inserting data in table using try and except
# try:
#     ins = 'INSERT INTO student(st_name,st_class,st_email) values(%s,%s,%s)'
#     # writing insert query in a variable and passing values as a tuple 

#     # t = ('Md Tabish', 'b.tech','tabishshaikh764@gmail.com')
#     # t = ('sanib qureshi', 'b.s.c.','sanibquershi@gmail.com')
#     # f = ('Faizan khan', 'b.tech','faizankhan@gmail.com')
#     # m = ('mukhtar shaikh', 'd.pharmacy','shaikhmukhtar@gmail.com')
#     many = [('huzaifa shaikh', 'd.pharmacy','huzaifa@gmail.com'),('raza quershi','b.s.c.','rajaquresi@gmail.com'),('muzzamil shaikh','b.tech','mujju@gmail.com')]    # creating list of tuples to insert at a single time
#     # putting the data

#     # cur.execute(ins,t)
#     # executing the query and passing the values

#     cur.executemany(ins,many)
#     # to inserting more than one row you use execute many

#     obj.commit()
#     # committing or saving the changes in table and you have to use commit function in object

#     print('Data Inserted')
# except:
#     print('Error')
#     # if try code run into an error this will print

# -----------------------------------------------------------------------
# ADDING DATA FROM USER

u_name = input("Enter the NAME :- ")
u_class = input("Enter the CLASS :- ")
u_email = input("Enter the EMAIL :- ")
u_data = (u_name,u_class,u_email)
try: 
    ins = "INSERT INTO student(st_name,st_class,st_email) values(%s,%s,%s)"
    cur.execute(ins,u_data)
    obj.commit()
    print('DONE ....')
except:
    print('ERROR ....')

obj.commit()