#!/usr/bin/python3
"""List all states from database hbtn_0e_0_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    user, passwd, db_name = sys.argv[1:5]
    database = MySQLdb.connect('localhost', user, passwd, db_name)
    cursor = database.cursor()
    # Execute the query
    cursor.execute("SELECT * FROM states "
                   "WHERE BINARY name='{}' "
                   "ORDER BY id".format(toMatch))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    # Clean up
    cursor.close()
    database.close()
