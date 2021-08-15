#!/usr/bin/python3
"""List all states from database hbtn_0e_0_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
	user, passwd, db_name = sys.argv[1:4]
	database = MySQLdb.connect('localhost', user, passwd, db_name, 3306)
	cursor = database.cursor()
	# Execute the query
	cursor.execute("SELECT * FROM states ORDER BY id;")
	rows = cursor.fetchall()
	for row in rows:
		print("({}, '{}')".format(*row))
	# Clean up
	cursor.close()
	database.close()
