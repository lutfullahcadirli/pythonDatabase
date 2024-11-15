import pyodbc

server = "DESKTOP-GS0CPS2\\SQLEXPRESS"
database = "node-app"

connection = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;')
print("Bağlantı başarılı!")

