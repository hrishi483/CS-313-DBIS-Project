from insert import insert_data
from delete import *
from update import *
from search import *
from variables import *
import psycopg2

# Define connection parameters
connection_params = {
    "database": database_name,
    "user": user_name,
    "password": password_val,
    "host": host_name,
    "port": port_name,
}

# Establish a database connection
conn = psycopg2.connect(**connection_params)
cursor = conn.cursor()

print("Connected to Placement Cell Database")
# Main menu
while True:
    print("Main Menu:")
    print("1. Insert")
    print("2. Delete")
    print("3. Update")
    print("4. Search")
    print("5. Exit")
    
    flag_print = True
    choice = input("Select an option: ").strip()

    if choice == "1":
        insert_data(conn, cursor)

    elif choice == "2":
        delete_data(conn, cursor)

    elif choice == "3":
        update_data(conn, cursor)

    elif choice == "4":
        search_data(conn, cursor)
        flag_print = False
    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid option. Please select a valid option.")
    
    if flag_print:
        SQL="SELECT * FROM Students "
        cursor.execute(SQL)
        print("\n\nStudents ",cursor.fetchall())

        SQL="SELECT * FROM Company "
        cursor.execute(SQL)
        print("\n\nCompany ",cursor.fetchall())

        SQL="SELECT * FROM Jobs "
        cursor.execute(SQL)
        print("\n\nJobs ",cursor.fetchall())

        SQL="SELECT * FROM basic_requirements_branch "
        cursor.execute(SQL)
        print("\n\nbasic_requirements_branch ",cursor.fetchall())

        SQL="SELECT * FROM requirements "
        cursor.execute(SQL)
        print("\n\nRequirements ",cursor.fetchall())

        SQL="SELECT * FROM courses "
        cursor.execute(SQL)
        print("\n\ncourses ",cursor.fetchall())

        SQL="SELECT * FROM courses_completed "
        cursor.execute(SQL)
        print("\n\ncourses Completed ",cursor.fetchall())

        SQL="SELECT * FROM job_application"
        cursor.execute(SQL)
        print("\n\nApplications ",cursor.fetchall())

# Close the database connection
conn.close()


