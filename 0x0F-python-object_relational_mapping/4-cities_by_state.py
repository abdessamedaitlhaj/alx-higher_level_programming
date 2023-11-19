#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    u = sys.argv[1]
    p = sys.argv[2]
    db = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", user=u,
                           passwd=p, db=db, port=3306)

    cur = conn.cursor()
    query = """
        SELECT cities.id, cities.name, states.name FROM cities
        INNER JOIN states ON cities.id = states.id
        """
    cur.execute(query)
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    conn.close()
