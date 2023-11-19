#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    port = 3306

    con = MySQLdb.connect("127.0.0.1", username, password, dbname, port)

    cur = conn.cursor()
    query = "SELECT * FROM states ORDER BY id"
    cur.execute(query)
    states = cur.fetchall()
    for state in states:
        print("({}, {})".format(state.id, state.name))
    cur.close()
    conn.close()
