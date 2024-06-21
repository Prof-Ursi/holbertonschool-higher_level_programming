#!/usr/bin/python3
"""
Module that lists all cities of a state
from the database 'hbtn_0e_4_usa'.
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
                   SELECT cities.name FROM cities
                   JOIN states ON cities.state_id = states.id
                   WHERE states.name LIKE BINARY %s
                   ORDER BY cities.id
                   """, (sys.argv[4],))
    results = cursor.fetchall()
    print(", ".join(row[0] for row in results))
    cursor.close()
    db.close()
