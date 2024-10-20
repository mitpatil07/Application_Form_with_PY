import mysql.connector

try:
    connection  = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpass",
    database="ladkibahin"
    )

    cursor = connection .cursor()

except Exception as e:
    print(e)

