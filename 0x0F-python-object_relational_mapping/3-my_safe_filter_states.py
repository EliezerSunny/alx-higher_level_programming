#!/usr/bin/python3
"""
SQL injection safe query to retrieve rows from the states table where
name matches an argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], database=sys.argv[3])
        cur = db.cursor()

        # Execute the parameterized query with case-sensitive collation
        cur.execute("SELECT * FROM states "
                    "WHERE name = %s "
                    "COLLATE 'latin1_general_cs' "
                    "ORDER BY id ASC", (sys.argv[4],))

        # Fetch and print all the rows
        for row in cur.fetchall():
            print(row)
        
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL DB: {e}")
    
    finally:
        # Close cursor and database connection in finally block
        if cur:
            cur.close()
        if db:
            db.close()
