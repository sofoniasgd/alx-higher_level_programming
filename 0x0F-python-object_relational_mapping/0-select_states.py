#!/usr/bin/python3
"""GET ALL STATES(Task 0)"""

import MySQLdb
import sys

if __name__ == "__main__":
    # exit if arguments are not 3
    if len(sys.argv) != 4:
        sys.exit()
    # store arguments into more readable names
    username, password, dbname = sys.argv[1:4]
    # connect to database
    db = MySQLdb.connect(host='localhost', user=username, passwd=password,
                         db=dbname, port=3306)
    cur = db.cursor()
    # execute and print query
    cur.execute("SELECT * FROM states ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
