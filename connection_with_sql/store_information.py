import pyodbc

# Database connection details
def store_data_information(name, mobile_number, email, password):
    server = 'LAPTOP-USGC4371\\SQLEXPRESS'
    database = 'woman_project'
    trusted_connection = 'yes'

    # Create a connection string
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection}'

    # Connect to the SQL Server
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()


    # Define the SQL query to insert data into the table
    insert_query = """
    INSERT INTO user_information (Username, MobileNumber, Email, Password)
    VALUES (?, ?, ?, ?)
    """
    
    # Execute the query with the data
    cursor.execute(insert_query, (name, mobile_number, email, password))
    
    # Commit the transaction
    conn.commit()
    cursor.close()
    conn.close()
    return "User information stored successfully"

# Example usage (replace with actual values from your function)
# store_user_information("John Doe", "1234567890", "johndoe@example.com", "hashed_password_here")

# Close the connection

