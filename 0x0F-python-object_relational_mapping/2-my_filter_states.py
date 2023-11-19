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
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(name)
    cur.execute(query)
    rws = cur.fetchall()
    for rw in rws:
        print(rw)
    cur.close()
    conn.close()
