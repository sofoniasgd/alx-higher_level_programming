#!/usr/bin/python3
"""GET ALL STATES(Task 0)"""

import MySQLdb
import sys

if __name__ == "__main__":
    # exit if arguments are not 3
    if len(sys.argv) != 4:
        sys.exit()
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    # connect to database
    db = MySQLdb.connect(host='localhost', user=username, passwd=password,
                         port=3306)
    try:
        db.select_db(dbname)
    except MySQLdb.OperationalError:
        cur = db.cursor()
        cur.execute(f"CREATE DATABASE IF NOT EXISTS {dbname}")
        db.commit()
        cur.close()
        db.select_db(dbname)
    # create the table
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS states \
            (id INT NOT NULL AUTO_INCREMENT, \
            name VARCHAR(256) NOT NULL, \
            PRIMARY KEY (id) )")
    cur.execute("INSERT INTO states (name) VALUES \
            ('California'), ('Arizona'), ('Texas'), \
            ('New York'), ('Nevada')")
    cur.execute("SELECT * FROM states ORDER BY id")
    db.commit()
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
