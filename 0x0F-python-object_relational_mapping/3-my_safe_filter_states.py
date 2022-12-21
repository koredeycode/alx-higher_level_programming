#!/usr/bin/python3
"""displays all values in the states table where name matches the argument
    free from sql injection"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    qs = f"SELECT * FROM states WHERE name LIKE %s ORDER BY states.id ASC"
    cur.execute(qs, (argv[4], ))
    qrows = cur.fetchall()
    for row in qrows:
        print(row)
    cur.close()
    conn.close()
