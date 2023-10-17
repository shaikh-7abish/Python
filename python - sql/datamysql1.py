# SELECT, DELETE, UPDATE

import pymysql as mq
obj = mq.connect(host='localhost',user='root',passwd='tabishshaikh764',db='school_for_learn')
cur = obj.cursor()

# print("                 STUDENTS")
# # using formatting print function to print column name
# print("{:<6} {:<20} {:<10} {:<20}".format('Id','STUDENT NAME','CLASS','EMAIL'))

# try:
#     sec = "SELECT * FROM student"
#     cur.execute(sec)
#     ex = cur.fetchall()
#     # to passes one row at a time as a tuple then another row
#     for i in ex:
#         print("{:<6} {:<20} {:<10} {:<20}".format(i[0], i[1] , i[2] , i[3]))
#     print('THANKS')
# except:
#     print('ERROR')
# ------------------------------------------
# print("                 STUDENTS")
# # using formatting print function to print column name
# print("{:<20} {:<10}".format('STUDENT NAME','CLASS'))
# print("")

# try:
#     sec = "SELECT st_name,st_class FROM student"
#     cur.execute(sec)
#     ex = cur.fetchall()
#     # to passes one row at a time as a tuple then another row
#     for i in ex:
#         print("{:<20} {:<10}".format(i[0], i[1]))
#     print('THANKS !!!!')
# except:
#     print('ERROR ....')
# -----------------------------------------------

# print("{:^6} {:^20} {:^10} {:^20}".format('Id','STUDENT NAME','CLASS','EMAIL'))

# try:
#     sec = "SELECT * FROM student where st_id=10"
#     cur.execute(sec)
#     ex = cur.fetchone()
#     # to passes only one row at a time as a tuple 
#     print("{:<6} {:<20} {:<10} {:<20}".format(ex[0],ex[1],ex[2],ex[3]))
#     print('THANKS')
# except:
#     print('ERROR')
# -------------------------------------------------

# DELETE

# uid = input("Enter the I'd you want to delete:- ")
# try:
#     dele = "DELETE FROM student where st_id=%s"
#     cur.execute(dele,uid)
#     obj.commit()
#     print('DELETED SUCCESSFULLY !!!!')
# except:
#     print('ERROR ....')

# ---------------------------------------------------------

# # UPDATE

# u_id = input("Enter the I'd you want to update:- ")
# u_name = input("Enter the Name you want to update:- ")
# u_class = input("Enter the Class you want to update:- ")
# u_email = input("Enter the Email you want to update:- ")

# try:
#     upd = "UPDATE student set st_name=%s, st_class=%s, st_email=%s where st_id=%s"
#     data = (u_name,u_class,u_email,u_id)
#     cur.execute(upd,data)
#     obj.commit()
#     print('UPDATE SUCCESSFULLY !!!!')
# except:
#     print("ERROR ....")

# ---------------------------------------------------------------

# UPDATING AUTO INCREMENT OR MAKING IT RIGHT -- works only one time

# try:
#     for i in range(2,14):
#         l=[0,1,6,7,8,9,10,11,14,15,17,18,19,20]     #get these from the table st_id's
#         upd= "UPDATE student set st_id={} where st_id={}".format(i,l[i])        # passing new id and old id in format
#         print(l[i],'=>',i)      #just checking
#         cur.execute(upd)
#         # print('DONE !!!!')
# except:
#     print('ERROR ....')

# obj.commit()

# -------------------------------------------------------------------

# ORDER BY & LIMIT

# try:
#     slt = "select * from student order by st_id ASC limit 2,2"      #ASC/DESC       limit 1st para- start from 2nd- how many row from 1st para
#     cur.execute(slt)
#     tp = cur.fetchall()
#     for i in tp:
#         print("{:^6} {:^30} {:^20} {:^25}".format(i[0], i[1], i[2], i[3]))
# except:
#     print("Error ....")

# ------------------------------------------------------------------------
# Search 
# = means == 
# like -- if one letter is same then it will pass but you have to say it from where to search (% u_name=> left)(u_name %=> right)(%u_name%=> both side searching)

u_name = input("Enter the student name :- ")
u_class = input("enter the class :- ")

try:
    # slt = "select * from student where st_name like'%"+u_name+"%'"
    # slt = "select * from student where st_name like'%"+u_name+"%' and st_email like '%"+u_class+"%'"
    slt = "select * from student where st_name like'%"+u_name+"%' or st_email like '%"+u_class+"%'"
    cur.execute(slt)
    tp = cur.fetchall()
    for i in tp:
        print("{:^6} {:^30} {:^20} {:^25}".format(i[0], i[1], i[2], i[3]))
except:
    print("Error ....")
