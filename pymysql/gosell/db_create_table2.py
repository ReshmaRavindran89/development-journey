"""
vehicle(id,name,model,running_km,fuel_type,owner_type,place,owner)

"""

from mysql import connector

connection = connector.connect(
host = "localhost",
user = "root",
password = "Password@123",
database = "gosell_db"
)

cursor = connection.cursor()

query = """
create table vehicle (
id int auto_increment primary key,
name varchar(200) not null unique,
model varchar(50),
running_km int,
fuel_type enum("petrol","diesel","cng") default "petrol",
owner_type varchar(100) not null,
place varchar(100) not null,
owner varchar(100) not null unique
)

"""
cursor.execute(query)

connection.commit()

print("table created")

cursor.close()

connection.close()