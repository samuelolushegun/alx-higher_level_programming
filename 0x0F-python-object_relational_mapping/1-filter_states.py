#!/usr/bin/python3
'''This module lists all states with a name starting with N'''
import MySQLdb
import sys


if __name__ = "__main__":

    db = MySQLdb.connect(host='localost', port=3306, username=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
