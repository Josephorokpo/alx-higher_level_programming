#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument and
lists all cities of that state,
using the database hbtn_0e_4_usa (safe from MySQL injection).
"""

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    query = """
        SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
        FROM cities
        INNER JOIN states ON states.id = cities.state_id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (sys.argv[4],))

    result = cursor.fetchone()

    if result[0]:
        print(result[0])
    else:
        print("No cities found for the specified state.")

    cursor.close()
    db.close()
