import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mysql1234",
    database = "node-app",
)

if mydb.is_connected():
    print("Baglantı Başarılı")
else:
    print("Baglantı Başarısız")

print(mydb)

