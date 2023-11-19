#!/usr/bin/python3
"""
Script that lists all states with a name starting with N
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
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cur.execute(query)
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    conn.close()
