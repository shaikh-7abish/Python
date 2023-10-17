# Joining tables

import pymysql as mq
obj = mq.connect(host='localhost',user='root',passwd='tabishshaikh764',db='school_for_learn')
cur = obj.cursor()

print("{:^6} {:^30} {:<10} {:^30}".format('id','student name','student class','student fees'))

# ------------------------------------------------
# Inner join

# try:
#     sel = "select student.st_id,student.st_name,student.st_class,fee.st_fee from student inner join fee on student.st_id=fee.st_id"
#     # select what you want from resp. tables then passing 'inner join table_name on' then showing which is common column between two tables
#     # if you select * from student then the index of fees tables changes in your for loop => d[6]
#     cur.execute(sel)
#     dt = cur.fetchall()
#     for d in dt:
#         print("{:^6} {:^30} {:^10} {:^30}".format(d[0],d[1],d[2],d[3]))
#         # print(d)
# except:
#     print('error ....')    

# ---------------------------------------------------
# left join

# try:
#     sel = "select student.st_id,student.st_name,student.st_class,fee.st_fee from student left join fee on student.st_id=fee.st_id"
#     # select what you want from resp. tables then passing 'left join table_name on' then showing which is common column between two tables
#     cur.execute(sel)
#     dt = cur.fetchall()
#     for d in dt:
#         print("{:^6} {:^30} {:^10} {:^30}".format(d[0],d[1],d[2],str(d[3])))
#         # putting str function in last because its none value not present in right table
#         # print(d)
# except:
#     print('error ....')

# ------------------------------------------------------
# right join

# try:
#     sel = "select student.st_id,student.st_name,student.st_class,fee.st_fee,fee.st_name from student right join fee on student.st_id=fee.st_id"
#     # select what you want from resp. tables then passing 'right join table_name on' then showing which is common column between two tables
#     cur.execute(sel)
#     dt = cur.fetchall()
#     for d in dt:
#         print("{:^6} {:^30} {:^10} {:^30} {:^30}".format(str(d[0]),str(d[1]),str(d[2]),d[3],d[4]))
#         # putting str function in 1st three because its none value not present in left table 
#         # print(d)
# except:
#     print('error ....')

# -----------------------------------------------------------
# equi join

# try:
#     sel = "select student.st_id,student.st_name,student.st_class,fee.st_fee from student, fee where student.st_id=fee.st_id"
#     # we didn't pass the join keyword instead we use select from both and where id is equal to id
#     cur.execute(sel)
#     dt = cur.fetchall()
#     for d in dt:
#         print("{:^6} {:^30} {:^10} {:^30}".format(d[0],d[1],d[2],d[3]))
#         # print(d)
# except:
#     print('error ....')

# ---------------------------------------------------------
# self join
# this doesn't work on our data

# try:
#     sel = 'SELECT * FROM fee as f1, fee as f2 where condition'
#     cur.execute(sel)
#     dt = cur.fetchall()
#     for d in dt:
#         print("{:^6} {:^30} {:^10} ".format(d[0],d[1],d[2]))

# except:
#     print('error....')

