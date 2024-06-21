#!/usr/bin/python3
"""
Script that displays all values in the 'states' table
from the database 'hbtn_0e_0_usa' AND safe from MySQL injections.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute("""
                   SELECT * FROM states
                   WHERE name LIKE BINARY %s
                   ORDER BY states.id
                   """, (sys.argv[4],))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
