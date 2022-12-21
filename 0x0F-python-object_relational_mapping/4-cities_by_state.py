#!/usr/bin/python3
"""lists all cities from the database"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    qs = """SELECT cities.id, cities.name, states.name
            FROM cities JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC"""
    cur.execute(qs)
    qrows = cur.fetchall()
    for row in qrows:
        print(row)
    cur.close()
    conn.close()
