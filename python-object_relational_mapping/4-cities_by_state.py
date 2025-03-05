#!/usr/bin/python3
"""
This module connects to a MySQL database and retrieves data from
the 'states' table.
"""
import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name, states.name FROM cities \
        JOIN states ON cities.state_id = states.id ORDER BY cities.id"
    )
    results = cursor.fetchall()
    for result in results:
        print(result)
