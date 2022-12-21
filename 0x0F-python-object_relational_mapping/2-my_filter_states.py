#!/usr/bin/python3
"""List all values in the states table where name matches the argument"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    qs = f"SELECT * FROM states WHERE name='{argv[4]}' ORDER BY states.id ASC"
    cur.execute(qs)
    qrows = cur.fetchall()
    for row in qrows:
        print(row)
    cur.close()
    conn.close()
