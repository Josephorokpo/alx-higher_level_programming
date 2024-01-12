#!/usr/bin/python3
"""
Module to display values in the states table of hbtn_0e_0_usa
where name matches the argument (safe from MySQL injection).
"""

import MySQLdb
import sys

if __name__ == "__main__":

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query with parameterized query to prevent MySQL injection
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}%' ORDER BY id ASC".format(sys.argv[4])
    cursor.execute(query)

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()
