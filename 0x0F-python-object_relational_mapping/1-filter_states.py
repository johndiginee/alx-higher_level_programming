#!/usr/bin/python3
"""
Script that lists all states with a name 
starting with N
"""

import MySQLdb as db
from sys import argv

"""
Access DB and get the states.
"""

if __name__ == "__main__":
    db_connect = db.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], db=argv[3], charset="utf8")
    db_cursor = db_connect.cursor()

    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
            ORDER BY states.id ASC")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)