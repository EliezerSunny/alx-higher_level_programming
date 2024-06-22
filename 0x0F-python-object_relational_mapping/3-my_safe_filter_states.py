#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and search term from arguments
    username, password, database, search_name = sys.argv[1:5]

    # Connect to the MySQL database
    db = MySQLdb.connect(user=username, passwd=password, db=database, host="localhost", port=3306)
    
    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query with a parameterized statement to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (search_name,))

    # Fetch and print all the results
    results = cursor.fetchall()
    for row in results:
        print(row)
    
    # Close the cursor and database connection
    cursor.close()
    db.close()
