#!/usr/bin/python3
'''This Module print all matches states with the input'''
import MySQLdb
import sys


if __name__ == "__main__":
    try:
        db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
        curs = db.cursor()
        sh = sys.argv[4]
        q = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(sh)
        curs.execute(q)

        rows = curs.fetchall()
        if rows:
            for row in rows:
                print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        if 'db' in locals() and db.open:
            curs.close()
            db.close()
