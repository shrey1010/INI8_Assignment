import sqlite3
from datetime import datetime

conn = sqlite3.connect('registration_database.db')
cursor = conn.cursor()

# Function to create the Registration table
def create_table():
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Registration (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Email TEXT NOT NULL,
                DateOfBirth DATE,
                CONSTRAINT unique_email UNIQUE (Email)
            )
        ''')
        conn.commit()
        print("Table created successfully.")
    except sqlite3.Error as e:
        print("Error creating table:", e)

# Function to create a new record
def create_record(name, email, date_of_birth):
    try:
        cursor.execute('''
            INSERT INTO Registration (Name, Email, DateOfBirth) 
            VALUES (?, ?, ?)
        ''', (name, email, date_of_birth))
        conn.commit()
        print("Record created successfully.")
    except sqlite3.Error as e:
        print("Error creating record:", e)

# Function to retrieve records
def read_records():
    try:
        cursor.execute("SELECT * FROM Registration")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print("Error retrieving records:", e)

# Function to update an existing record
def update_record(record_id, new_name, new_email, new_date_of_birth):
    try:
        cursor.execute('''
            UPDATE Registration 
            SET Name=?, Email=?, DateOfBirth=? 
            WHERE ID=?
        ''', (new_name, new_email, new_date_of_birth, record_id))
        conn.commit()
        print("Record updated successfully.")
    except sqlite3.Error as e:
        print("Error updating record:", e)

# Function to delete a record
def delete_record(record_id):
    try:
        cursor.execute("DELETE FROM Registration WHERE ID=?", (record_id,))
        conn.commit()
        print("Record deleted successfully.")
    except sqlite3.Error as e:
        print("Error deleting record:", e)

# Function to close the database connection
def close_connection():
    conn.close()
    print("Connection closed.")

# Example Usage
create_table()

create_record("John Doe", "john@example.com", "1990-01-01")
create_record("Jane Smith", "jane@example.com", "1985-05-15")

read_records()

update_record(1, "John Updated", "john.updated@example.com", "1990-01-01")

read_records()

delete_record(2)

read_records()

close_connection()
