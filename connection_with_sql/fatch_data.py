from flask import jsonify, session
import pyodbc

# Database connection details
def fatch_information(username, password):
    server = 'LAPTOP-USGC4371\\SQLEXPRESS'
    database = 'woman_project'
    trusted_connection = 'yes'

    # Create a connection string
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection}'

    # Connect to the SQL Server
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM user_information WHERE (Email = ? OR MobileNumber = ?) AND Password = ?", username, username, password)
    result = cursor.fetchone()

    if result:
        # Set session and return success
        session['user_id'] = result[0]
        return True
        
    else:
        # Return failure message if login fails
        return False
