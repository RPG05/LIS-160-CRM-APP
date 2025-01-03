import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'BaekMin*499'

	)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE gidb")

print("Done.")