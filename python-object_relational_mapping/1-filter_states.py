#!/usr/bin/python3
"""
    Create a that lists all states with a name starting with N
"""


import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(
       user=sys.argv[1],
       password=sys.argv[2],
       db=sys.argv[3],
       host="localhost",
       port=3306
    )

    cur = conn.cursor()

    cur.execute("SELECT * FROM states \
        WHERE name LIKE BINARY 'N%' \
        ORDER BY id ASC")

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    conn.close()
