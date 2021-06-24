import os
import mysql.connector

db_server_name = os.environ["DB_SERVER_NAME"]
db_admin_name = os.getenv("DB_ADMIN_NAME", "azureuser")
db_admin_password = os.getenv("DB_ADMIN_PASSWORD", "ChangePa$$w0rd24")

db_name = os.getenv("DB_NAME", "example-db1")
db_port = os.getenv("DB_PORT", 3306)

connection = mysql.connector.connect(user=f"{db_admin_name}@{db_server_name}",
    password=db_admin_password, host=f"{db_server_name}.mysql.database.azure.com",
    port=db_port, database=db_name, ssl_ca='./BaltimoreCyberTrustRoot.crt.pem')

cursor = connection.cursor()

"""
# Alternate pyodbc connection; include pyodbc in requirements.txt
import pyodbc

driver = "{MySQL ODBC 5.3 UNICODE Driver}"

connect_string = f"DRIVER={driver};PORT=3306;SERVER={db_server_name}.mysql.database.azure.com;" \
                 f"DATABASE={DB_NAME};UID={db_admin_name};PWD={db_admin_password}"

connection = pyodbc.connect(connect_string)
"""

table_name = "ExampleTable1"

sql_create = f"CREATE TABLE {table_name} (name varchar(255), code int)"

cursor.execute(sql_create)
print(f"Successfully created table {table_name}")

sql_insert = f"INSERT INTO {table_name} (name, code) VALUES ('Azure', 1)"
insert_data = "('Azure', 1)"

cursor.execute(sql_insert)
print("Successfully inserted data into table")

sql_select_values= f"SELECT * FROM {table_name}"

cursor.execute(sql_select_values)
row = cursor.fetchone()

while row:
    print(str(row[0]) + " " + str(row[1]))
    row = cursor.fetchone()

connection.commit()
