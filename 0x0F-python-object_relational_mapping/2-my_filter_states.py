#!/usr/bin/python3
"""List all values in the states table where name matches the argument"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    qs = "SELECT * FROM states WHERE LIKE BINARY '{}' ORDER BY states.id ASC" \
        .format(argv[4])
    cur.execute(qs)
    qrows = cur.fetchall()
    for row in qrows:
        print(row)
    cur.close()
    conn.close()
