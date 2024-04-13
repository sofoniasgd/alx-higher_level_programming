#!/usr/bin/python3
"""MySQLdb tutorial"""

import MySQLdb

db = MySQLdb.connect(host='localhost', user='soficon1', passwd='soficon1', db='test')
if (db):
    print("database connected")
else:
    print("database not connected")

cur = db.cursor()
cur.execute("SELECT * FROM tt")
