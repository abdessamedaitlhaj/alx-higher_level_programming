#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    host = "localhost"

    conn = MySQLdb.connect(host, user, passwd, db)

    cur = conn.cursor()
    query = "SELECT * FROM states"
    cur.execute(query)
    states = cur.fetchall()
    for state in states:
        print("({}, {})".format(state.id, state.name))
    cur.close()
    conn.close()
