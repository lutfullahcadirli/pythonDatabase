import pyodbc


server = "DESKTOP-GS0CPS2\SQLEXPRESS"
database = "schooldb"


try: 
    # baglangıt oluştur.
    connection = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;')
    print("Bağlantı başarılı!")

    # cursor ile sorgu oluşturma
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM student") # ornek sorgu
    for row in cursor.fetchall():
        print(row)

except Exception as e:
    print("Hata oluştu:", e)

finally:
    # Bağlantıyı kapat
    if 'connection' in locals() and connection is not None:
        connection.close()