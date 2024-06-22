#!/usr/bin/python3
"""
Query to retrieve all cities of a given state from the cities table
in hbtn_0e_4_usa database.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py <username> <password> <database_name> <state_name>")
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:5]

    try:
        # Connect to MySQL database
        db = MySQLdb.connect(user=username, passwd=password, db=database, host="localhost", port=3306)
        cursor = db.cursor()

        # Execute the SQL query with JOIN to retrieve cities of the given state
        query = ("SELECT cities.name "
                 "FROM cities "
                 "JOIN states ON cities.state_id = states.id "
                 "WHERE states.name = %s "
                 "ORDER BY cities.id ASC")
        cursor.execute(query, (state_name,))

        # Fetch all rows and join city names into a comma-separated string
        results = cursor.fetchall()
        cities_list = ", ".join(row[0] for row in results)

        # Print the list of cities
        print(cities_list)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL DB: {e}")

    finally:
        # Close cursor and database connection in finally block
        if cursor:
            cursor.close()
        if db:
            db.close()
