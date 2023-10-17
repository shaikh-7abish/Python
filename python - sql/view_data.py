import pymysql as sql
obj = sql.connect(host= 'localhost',user='root',passwd='',db= 'dbName')
cur = obj.cursor()

def get_dates():
    from_date = input('Get data From {YYYY-MM-DD}: ')
    to_date = input('To {YYYY-MM-DD} : ')
    get_dates.dates = (from_date,to_date)

def pay_func():
    pay_query = 'SELECT * FROM payments WHERE pay_date BETWEEN %s AND %s'
    cur.execute(str(pay_query),get_dates.dates)
    data1 = cur.fetchall()
    print('{:^6} {:^40} {:^25} {:^15} {:^10} {:^25}'.format('ID','NEFT ID','ORDER ITEM ID','SATEL VALUE','PAY DATE','CREATED ON'))
    for i in data1:
        print('{:^6} {:^40} {:^25} {:^15} {:^10} {:^25}'.format(i[0],i[1],i[2],i[3],i[4],str(i[5])))

def return_order_func():
    return_order_query = 'SELECT * FROM return_order WHERE return_date BETWEEN %s AND %s'
    cur.execute(str(return_order_query),get_dates.dates)
    data1 = cur.fetchall()
    print('{:^6} {:^40} {:^25} {:^30} {:^25} {:^10}'.format('ID','INVOICE NUMBER','RETURN TYPE','RETURN TRACK ID','RETURN DATE','M ID'))
    for i in data1:
        print('{:^6} {:^40} {:^25} {:^30} {:^25} {:^10}'.format(i[0],i[1],i[2],i[3],str(i[4]),str(i[5])))

def manifest_func():
    manifest_query = 'SELECT * FROM manifest WHERE manifest_date BETWEEN %s AND %s'
    cur.execute(str(manifest_query),get_dates.dates)
    data1 = cur.fetchall()
    for i in data1:
        for j in i:
            print(j, end='\t')
        print('\n')
        
while True:
    user_inp = int(input('''
        Payments        --enter 1
        Return orders   --enter 2
        Manifest        --enter 3
        Exit            --enter 4
'''))
    if user_inp == 1:
        get_dates()
        pay_func()

    elif user_inp == 2:
        get_dates()
        return_order_func()

    elif user_inp == 3:
        get_dates()
        manifest_func()

    elif user_inp == 4:
        break;
   
    else :
        print('Invalid Input')