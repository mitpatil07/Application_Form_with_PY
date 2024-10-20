import mysql.connector

try:
    connection  = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mitesh",
    database="ladkibahin"
    )

    cursor = connection .cursor()

except Exception as e:
    print(e)

