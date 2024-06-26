#!/usr/bin/python3
"""
Script to list all states with a name starting with `N` from
database `hbtn_0e_0_usa`
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the SQL query to retrieve states starting with 'N'
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cur.execute(query)

    # Fetch and print all the results of the query
    for row in cur.fetchall():
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.close()
