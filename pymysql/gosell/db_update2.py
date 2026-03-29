from mysql import connector

connection = connector.connect(
host = "localhost",
user = "root",
password = "Password@123",
database = "gosell_db"
)

cursor = connection.cursor()

query =" update vehicle set name = %s where id = %s"

data = ("fronx",2)

cursor.execute(query,data)

connection.commit()

cursor.close()
connection.close()
print("table updated......")