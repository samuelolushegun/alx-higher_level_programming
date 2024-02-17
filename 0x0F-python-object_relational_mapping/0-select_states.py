#!/usr/bin/python3
'''This script lists all states from the database'''
import MySQLdb
import sys


def select_states(username, password, database):
    '''This function done the select task'''
    db = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:]
    select_states(username, password, database)
