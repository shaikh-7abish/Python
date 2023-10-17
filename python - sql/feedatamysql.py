import pymysql as mq
obj = mq.connect(host='localhost',user='root',passwd='tabishshaikh764',db='fees_data')
cur = obj.cursor()

# try:
#     db = "create database fees_data"
#     cur.execute(db)
#     obj.commit()
#     print('database created')
# except:
#     print('error')

# try:
#     tab_crt = "create table fee(st_id INT primary key auto_increment,st_name VARCHAR(50), st_fee INT)"
#     cur.execute(tab_crt)
#     obj.commit()
#     print('done')
# except:
#     print('error')
