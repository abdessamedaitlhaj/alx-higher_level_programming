#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    u = sys.argv[1]
    p = sys.argv[2]
    db = sys.argv[3]

    conn = MySQLdb.connect(host="127.0.0.1", user=u, passwd=p, db=db)

    cur = conn.cursor()
    query = "SELECT * FROM states ORDER BY id"
    cur.execute(query)
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    conn.close()
