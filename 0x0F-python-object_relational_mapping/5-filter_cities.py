#!/usr/bin/python3
"""SEARCH ALL STATES WITH KEYWORD(Task 2)"""

import MySQLdb
import sys

if __name__ == "__main__":
    # store arguments into more readable names
    username, password, dbname, state_name = sys.argv[1:5]
    # connect to database
    db = MySQLdb.connect(host='localhost', user=username, passwd=password,
                         db=dbname, port=3306)
    cur = db.cursor()
    # execute and print query
    cur.execute("SELECT GROUP_CONCAT(cities.name) FROM cities LEFT JOIN \
                states ON state_id=states.id WHERE states.name='{}' ORDER BY \
                cities.id".format(state_name))
    rows = cur.fetchall()
    if (rows[0][0] is None):
        cur.close()
        db.close()
        sys.exit()
    cities = ""
    for city in rows[0]:
        cities += city
    print(cities.replace(",", ", "))
    cur.close()
    db.close()
