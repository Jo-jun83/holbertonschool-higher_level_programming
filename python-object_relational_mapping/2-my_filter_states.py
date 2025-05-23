#!/usr/bin/python3
"""
This module connects to a MySQL database and retrieves data from
the 'states' table.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=password,
        db=database,
        port=3306
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE CONVERT(name USING Latin1) \
        COLLATE Latin1_General_CS = '{}' \
        ORDER BY states.id;".format(sys.argv[4],)
    )
    results = cursor.fetchall()
    for result in results:
        print("{}".format(result))
