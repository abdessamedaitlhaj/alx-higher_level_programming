#!/usr/bin/python3
"""
Script that lists all states with a name matches the argument
"""

import sys
import MySQLdb

if __name__ == "__main__":
    u = sys.argv[1]
    p = sys.argv[2]
    db = sys.argv[3]
    name = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", user=u,
                           passwd=p, db=db, port=3306)

    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (name,))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    conn.close()
