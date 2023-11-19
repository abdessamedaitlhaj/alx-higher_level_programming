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
    state_name = sys.argv[4]
    conn = MySQLdb.connect(host="localhost", user=u,
                           passwd=p, db=db, port=3306)

    cur = conn.cursor()
    query = """
        SELECT cities.name FROM cities
        INNER JOIN states ON states.id = cities.state_id
        WHERE states.name = %s"""
    cur.execute(query, (state_name,))
    rws = cur.fetchall()
    for i, rw in enumerate(rws):
        if i > 0 and i < len(rws):
            print(", ", end="")
        print(rw[0], end="")
    print()
    cur.close()
    conn.close()
