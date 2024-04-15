#!/usr/bin/python3
"""SEARCH ALL STATES WITH KEYWORD(Task 3) SQL injection prevention"""

import MySQLdb
import sys

if __name__ == "__main__":
    # store arguments into more readable names
    username, password, dbname = sys.argv[1:4]
    # connect to database
    db = MySQLdb.connect(host='localhost', user=username, passwd=password,
                         db=dbname, port=3306)
    cur = db.cursor()
    # execute and print query
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
                LEFT JOIN states ON state_id=states.id ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
