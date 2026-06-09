import pymysql

try:
    db= pymysql.connect(host='localhost',user='root',password='',database='my_db')
    print("Database Connected!")
except Exception as e:
 print(e)  

cr = db.cursor()  

create_tbl = "create table mydetails (id integer primary key, auto_increment name text, city text,education text)"
try:
   cr.execute(create_tbl)
   print("Table created")
except Exception as e:
   print(e)   