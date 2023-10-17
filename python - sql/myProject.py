from sys import exc_info
import pymysql as mq
obj = mq.connect(host='localhost',user='root',passwd='tabishshaikh764',db='school_for_learn')
cur = obj.cursor()


ins_query = 'INSERT INTO student(st_name,st_class,st_email) values(%s,%s,%s)'
sel_query = 'SELECT * from student'
sel_id_query = 'SELECT * from student where st_id = %s'
del_query = 'DELETE from student where st_id=%s'
upd_query = 'UPDATE student set st_id = %s where st_id = %s'


while True:
    print('''
        1.   To Enter data
        2.   To View data
        3.   To Delete data by Id
        4.   To Update I'd
        5.   To Exit
    ''')
    user_input = int(input('enter your choice -- '))
    
    if user_input == 1:
        name_in= input('Enter the name - ')
        class_in= input('Enter the class - ')
        email_in= input('Enter the email - ')
        all_data = (name_in,class_in,email_in)

        try :
            cur.execute(ins_query,all_data)
            obj.commit()
            print('Inserted Successfully')
        except:
            print('Error Inserting Data')

    elif user_input == 2:
        try:
            cur.execute(sel_query)
            view_dt = cur.fetchall()
        
            print('{:^6} {:^30} {:^15} {:^25}'.format('ID','STUDENT NAME','CLASS','EMAIL'))
            for i in view_dt:
                print('{:^6} {:^30} {:^15} {:^25}'.format(i[0],i[1],i[2],i[3]))
        
        except:
            print('Error Viewing Data')

    elif user_input == 3:
        
        try:
            del_id = input('Enter the Id to Delete - ')
            cur.execute(del_query,del_id)
            obj.commit()
            print('Delete Successfully')

        except:
            print('Error')

    elif user_input == 4: # work in progress
        upd_in = input('Enter the ID you want to update - ')
        cur.execute(sel_id_query,upd_in)
        vw = cur.fetchone()
        print('{:^6} {:^30} {:^15} {:^25}'.format(vw[0],vw[1],vw[2],vw[3]))

        u_in = input('Enter the new Id - ')
        upd_data = (u_in,upd_in)
        try:
            cur.execute(upd_query,upd_data)
            obj.commit()
            print('Updated Successfully')
        except:
            print('Error')
        
    elif user_input == 5:
        break

    else :
        print('Invalid Input')



