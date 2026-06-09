import pymysql

try:
    db=pymysql.connect(host='localhost',user='root',password='',database='topsdata')
    print('Database connected!')
except Exception as e:
    print(e)    

cr = db.cursor()

# create_table ="CREATE TABLE playerinfo (id integer PRIMARY KEY AUTO_INCREMENT,name varchar(20),frenchise varchar(20))"

# try:
#     cr.execute(create_table)
#     print("Table created")
# except Exception as e:
#     print(e)  

# insert_data = "insert into playerinfo (name,frenchise)values ('Virat','RCB'),('Rohit','MI'),('Abhishek','SRH'),('Jadeja','RJ')" 
# try:
#     cr.execute(insert_data)
#     db.commit()
#     print("Record inserted")      
# except Exception as e:
#     print(e)

# update_data = "update playerinfo set name='param',frenchise='GT' where id = 10"
# try:
#     cr.execute(update_data)
#     db.commit()
#     print('Record update')
# except Exception as e :
#     print(e)    

# delete_data = "delete from playerinfo where id = 11"
# try:
#     cr.execute(delete_data)
#     db.commit()
#     print("Record delete")
# except Exception as e:
#     print(e) 

show_data = "select * from playerinfo"
try:
    cr.execute(show_data)
    data = cr.fetchall()
    print("data")
except Exception as e:
    print(e)    
    
