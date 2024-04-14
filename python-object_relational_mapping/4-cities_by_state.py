#!/usr/bin/python3
"""
    A script that lists all cities from the database hbtn_0e_4_usa
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

    sql = """SELECT c.id, c.name, s.name
          FROM states s, cities c
          WHERE c.state_id = s.id
          ORDER BY c.id ASC"""

    cursor.execute(sql)
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    conn.close()
