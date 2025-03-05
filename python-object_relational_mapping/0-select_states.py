#!/usr/bin/python3
"""
This module connects to a MySQL database and retrieves data from
the 'states' table.
"""


import MySQLdb
import sys

db = MySQLdb.connect(
    host="localhost",
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3],
    port=3306
)

cursor = db.cursor()
cursor.execute("SELECT * FROM states ORDER BY states.id")
results = cursor.fetchall()
for result in results:
    print(result)
