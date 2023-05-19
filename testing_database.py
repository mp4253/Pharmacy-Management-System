import mysql.connector

conn=mysql.connector.connect(host="localhost",
                             username="root",
                             password="1032",
                             database="mypharmacy")
if conn.is_connected:
    print("success")
else:
    print("not")