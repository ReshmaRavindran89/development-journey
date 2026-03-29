from mysql import connector

connection = connector.connect(
host = "localhost",
user = "root",
password = "Password@123",
database = "gosell_db"
)

cursor = connection.cursor()

query = """

insert into vehicle(name,model,running_km,fuel_type,owner_type,place,owner) values (%s,%s,%s,%s,%s,%s,%s)

"""

data = ("Tiago","2024",2100,"petrol","first","Kannur","Kiran")

cursor.execute(query,data)

connection.commit()

cursor.close()

connection.close()

print("data inserted.....")