#!/usr/bin/python3
"""Lists all states from the database"""
from sys import argv
import MySQLdb
if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute('SELECT * FROM states ORDER BY states.id ASC')
    qrows = cur.fetchall()
    for row in qrows:
        print(row)
    cur.close()
    conn.close()
