import pymysql as mq
obj = mq.connect(host='localhost',user='root',passwd='tabishshaikh764',db='school_for_learn')
cur = obj.cursor()

sel_id_query = 'SELECT * from student where st_id = %s'
upd_query = 'UPDATE student set %s = %s where st_id = %s'


upd_in = input('Enter the ID you want to update - ')

try:
    cur.execute(sel_id_query,upd_in)
    vw = cur.fetchone()
    print('{:^6} {:^30} {:^15} {:^25}'.format(vw[0],vw[1],vw[2],vw[3]))

    u_in = input('Enter what you want to update (id,name,class,email) - ')
    if u_in == 'id':
        n_id = input('Enter the new Id - ')

        upd_data = ('st_id',n_id,upd_in)
        cur.execute(upd_query,upd_data)
    elif u_in == 'name':
        n_name = input('Enter the new Id - ')

        upd_data = ('st_name',n_name,upd_in)
        cur.execute(upd_query,upd_data)
    elif u_in == 'class':
        n_class = input('Enter the new Id - ')

        upd_data = ('st_class',n_class,upd_in)
        cur.execute(upd_query,upd_data)
    elif u_in == 'email':
        n_email = input('Enter the new Id - ')

        upd_data = ('st_id',n_email,upd_in)
        cur.execute(upd_query,upd_data)

    print('Done')

except:
    print('Error')