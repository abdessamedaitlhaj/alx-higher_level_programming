#!/usr/bin/python3
"""
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""
if __name__ == "__main__":

    import MySQLdb
    import sys

    connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
    )

    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id"
        .format(sys.argv[4]))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    connection.close()