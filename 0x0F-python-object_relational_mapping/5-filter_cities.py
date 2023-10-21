#!/usr/bin/python3
"""
lists all cities of state (typed as argument), using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3]
                        )
    mycursor = db.cursor()
    sql_query = "SELECT ct.name FROM cities as ct \
                JOIN states as st ON ct.state_id = st.id \
                WHERE st.name LIKE %s"
    mycursor.execute(sql_query, (sys.argv[4], ))
    rows = mycursor.fetchall()

    results = ""
    for row in rows:
        results += row[0] + ", "
    print(results[:-2:])
