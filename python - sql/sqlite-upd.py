import sqlite3
con = sqlite3.connect('sqlite1.db')

upd = [
"UPDATE student SET st_id = 101,st_class = '10th' where st_name = 'TABISH'",
"UPDATE student SET st_id = 102 where st_name = 'ABISH'",
"UPDATE student SET st_id = 103 where st_name = 'BISH'",
"UPDATE student SET st_id = 104 where st_name = 'ISH'",
"UPDATE student SET st_id = 105 where st_name = 'SH' "
]

for i in range(0,4):
    con.execute(upd[i])
# passing one element at a time to execute update doesn't work in many  statements at a time

con.commit()
con.close()