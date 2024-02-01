
# Registration System

This project implements a simple Registration System using Python and SQLite. The system allows for the creation, retrieval, updating, and deletion of user registration records in a SQLite database.

## Prerequisites

- Python 3.x installed on your machine.
- Ensure that you have the required permissions to create and modify files on your system.

## Getting Started

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/shrey1010/INI8_Assignment.git
    cd INI8_Assignment
    ```

2. **Install Dependencies:**

    No external dependencies need to be installed for this project.

3. **Create a Virtual Environment (Optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
    ```

4. **Run the Code:**

    ```bash
    python main.py
    ```

    This will execute the Python script, which creates the 'Registration' table, performs CRUD operations, and prints the results.

## Project Structure

- **registration_system.py:** Python script containing the main code for the Registration System.
- **registration_database.db:** SQLite database file where registration records are stored.

## Code Overview

- **create_table():** Function to create the 'Registration' table.
- **create_record(name, email, date_of_birth):** Function to add a new registration record.
- **read_records():** Function to retrieve and print all registration records.
- **update_record(record_id, new_name, new_email, new_date_of_birth):** Function to update an existing record.
- **delete_record(record_id):** Function to delete a record.
- **close_connection():** Function to close the database connection.

## Example Usage

1. The table is created.
2. Two records are added.
3. All records are printed.
4. The first record is updated.
5. All records are printed again.
6. The second record is deleted.
7. All records are printed once more.

## Troubleshooting

- If you encounter any issues, ensure that you have the required permissions to create files and directories.
- Check that Python is installed correctly, and the version is 3.x.

## Closing the Application

To close the application and deactivate the virtual environment (if used):

```bash
deactivate
```

This completes the setup and execution of the Registration System on your local machine. If you encounter any issues, feel free to contact the project contributors.

---
