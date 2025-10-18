import mysql.connector

try:
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '@1Awspolicyss'
    )

    if not mydb.is_connected:
        print('Error while connecting to Mysql')

    mycursor = mydb.cursor()

    mycursor.execute('CREATE DATABASE IF NOT EXISTS alx_book_store')
    print("Database 'alx_book_store' created successfully!")
except mysql.connector.errors as err:
    print(f'Error {err} Encountered')