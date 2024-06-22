#!/usr/bin/python3
"""
Script that takes state name as an argument and lists all cities from
that state using database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    try:
        # Connect to MySQL database
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], database=sys.argv[3], host="localhost", port=3306)
        cur = db.cursor()

        # Execute the SQL query to retrieve cities of the given state
        query = ("SELECT cities.`name` FROM cities "
                 "JOIN states ON cities.`state_id` = states.`id` "
                 "WHERE states.`name` = %s "
                 "COLLATE 'latin1_general_cs' "
                 "ORDER BY cities.`id` ASC")
        cur.execute(query, (sys.argv[4],))

        # Fetch all rows and join city names into a comma-separated string
        cities_list = ', '.join(map(lambda x: x[0], cur.fetchall()))

        # Print the list of cities
        print(cities_list)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL DB: {e}")

    finally:
        # Close cursor and database connection in finally block
        if cur:
            cur.close()
        if db:
            db.close()
