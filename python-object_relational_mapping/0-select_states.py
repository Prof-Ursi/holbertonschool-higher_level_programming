#!/usr/bin/python3
"""
Import the MySQLdb and sys module
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cursor = db.cursor()
    cursor.execute("SELECT states.id, states.name FROM states ORDER BY id ASC")
    for i in cursor:
        print(i)