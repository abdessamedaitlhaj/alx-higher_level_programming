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

    conn = MySQLdb.connect(host="localhost", user=u,
                           passwd=p, db=db, port=3306)

    cur = conn.cursor()
    query = "SELECT * FROM states ORDER BY id"
    cur.execute(query)
    rws = cur.fetchall()
    for rw in rws:
        print(rw)
    cur.close()
    conn.close()
