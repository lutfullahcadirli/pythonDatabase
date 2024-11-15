import pyodbc
from connection import connection

def insertProduct(id,name,price):
    server = "DESKTOP-GS0CPS2\\SQLEXPRESS"
    database = "node-app"
    try:
        # baglangıt oluştur.
        connection = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;')
        print("Bağlantı başarılı!")
        cursor = connection.cursor()

        sql = "INSERT INTO products(id,name,price) VALUES (?,?,?)"
        values = (id,name,price)
        cursor.execute(sql,values)
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi ")
        # print(f"son eklenen kayıtın id numarasi: {cursor.lastrowid}")
    except Exception as e:
        print("Hata oluştu:", e)


    finally:
        if 'connection' in locals() and connection is not None:
            connection.close()
            print("database baglantisi kapandi.")



def insertProducts(list):
    server = "DESKTOP-GS0CPS2\\SQLEXPRESS"
    database = "node-app"
    try:
        # baglangıt oluştur.
        connection = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;')
        print("Bağlantı başarılı!")
        cursor = connection.cursor()

        sql = "INSERT INTO products(id,name,price) VALUES (?,?,?)"
        values = list
        cursor.executemany(sql,values)
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi ")
        # print(f"son eklenen kayıtın id numarasi: {cursor.lastrowid}")
    except Exception as e:
        print("Hata oluştu:", e)


    finally:
        if 'connection' in locals() and connection is not None:
            connection.close()
            print("database baglantisi kapandi.")



list = []
while True:
    id = input("İd Numarasi: ")
    name = input("Urun adı: ")
    price = input("Urun fiyatı: ")

    list.append((id,name,price))

    result = input("Devam etmek istiyormusunuz? (e/h)")
    if result == 'h':
        print("Kayitlarınız veritabanina aktarılıyor.")
        print(list)
        insertProducts(list)
        break






# insertProduct(id,name,price)
