#!/usr/bin/python3
"""
Script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import MySQLdb as db
from sys import argv

if __name__ == "__main__":
    """
    Access DB and get the states.
    """
    db_connect = db.connect(host="localhost", port=3306, user=argv[1],
                            password=argv[2], db=argv[3], charset="utf8")
    db_cursor = db_connect.cursor()

    db_cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \
            states.id ASC".format(argv[4]))
    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
