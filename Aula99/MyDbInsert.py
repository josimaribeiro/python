import mysql.connector

# Establish a connection to the MySQL database
try:
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="your_username",
        password="your_password",
        database="your_database_name",
    )

    if connection.is_connected():
        print("Connected to the MySQL database")

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Define the data you want to insert
        data_to_insert = {"name": "John Doe", "email": "johndoe@example.com", "age": 30}

        # SQL query to insert data into a table
        insert_query = "INSERT INTO your_table_name (name, email, age) VALUES (%(name)s, %(email)s, %(age)s)"

        # Execute the insert query with the data
        cursor.execute(insert_query, data_to_insert)

        # Commit the changes to the database
        connection.commit()
        print("Data inserted successfully")

except mysql.connector.Error as error:
    print("Error:", error)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Database connection closed")
