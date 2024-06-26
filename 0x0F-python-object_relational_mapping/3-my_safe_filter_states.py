#!/usr/bin/python3
"""SEARCH ALL STATES WITH KEYWORD(Task 3) SQL injection prevention"""

import MySQLdb
import sys

if __name__ == "__main__":
    # store arguments into more readable names
    username, password, dbname, state_name = sys.argv[1:5]
    # connect to database
    db = MySQLdb.connect(host='localhost', user=username, passwd=password,
                         db=dbname, port=3306)
    cur = db.cursor()
    # prevent sql injection
    if (state_name.find(";") >= 0 or state_name.find("=") >= 0):
        sys.exit()
    # execute and print query
    cur.execute("SELECT * FROM states WHERE BINARY name=\'{}\' ORDER BY id ASC"
                .format(state_name))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
