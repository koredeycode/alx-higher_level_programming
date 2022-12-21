#!/usr/bin/python3

from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    qs = """SELECT cities.name FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name LIKE %s ORDER BY cities.id ASC"""
    cur.execute(qs, (argv[4], ))
    qrows = cur.fetchall()
    print(*[row[0] for row in qrows], sep=", ")
    cur.close()
    conn.close()
