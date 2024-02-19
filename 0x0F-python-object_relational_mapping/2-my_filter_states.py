#!/usr/bin/python3
'''This Module print all matches states with the input'''
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    que = ("SELECT * FROM states\
WHERE name = {} ORDER BY id ASC".format(sys.argv[4]))
    curs.execute(que)

    rows = curs.fetchall()
    for row in rows:
        print(row)

    curs.close()
    db.close()
