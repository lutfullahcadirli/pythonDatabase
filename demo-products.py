import pyodbc
from connection import connection
from datetime import datetime


class Student:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self,id,name,price):
        self.id = id
        self.name = name
        self.price = price


    def saveStudent(self):
        sql = "INSERT INTO products (id, name, price) VALUES (?, ?, ?)"
        value = (self.id,self.name,self.price)
        Student.mycursor.execute(sql,value)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt eklendi')
        except Exception as e:
            print("Hata oluştu:", e)
        finally:
            Student.connection.close()
    
    
    @staticmethod
    def saveStudents(students):
        sql = "INSERT INTO products(id,name,price) VALUES (?,?,?)"
        values = students
        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kayıt eklendi')
        except Exception as e:
            print("Hata oluştu:", e)
        finally:
            Student.connection.close()




def getProducts():
    server = "DESKTOP-GS0CPS2\\SQLEXPRESS"
    database = "node-app"

    connection = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;')
    print("Bağlantı başarılı!")

    connection = connection
    cursor = connection.cursor()
    # cursor.execute('Select * from products ')
    cursor.execute('Select name,price from products ')
    # result = cursor.fetchall()
    result = cursor.fetchall()
    for product in result:
        print(f'name: {product[0]} price: {product[1]}')

getProducts()


urunler = [
    ("9","lenova laptop",3456),
    ("10","dell laptop",5099),
]

# Student.saveStudents(urunler)

