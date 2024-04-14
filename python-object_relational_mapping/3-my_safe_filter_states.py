#!/usr/bin/python3
"""
    script that takes in an argument and displays all
    values in the states table of hbtn_0e_0_usa
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
    cursor = conn.cursor()
    sql = """ SELECT * FROM states
        WHERE name = %s
        ORDER BY id ASC """

    cursor.execute(sql, (sys.argv[4],))
    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    conn.close()
