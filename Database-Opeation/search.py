import psycopg2


def search_data(conn,cursor):
    available_tables = ["courses_completed", "courses", "job_application", "requirements", "basic_requirements_branch", "Students", "Jobs", "company" ]
    print(f"Tables : {available_tables}")
    table_name = input("Enter the Table Name to Query the data:  ")

    if table_name not in available_tables:
        print("Invalid table name")
        
    elif table_name=="Students":
        while True:
            table_columns = ["roll_no","student_name","cpi","branch","credits"]
            print("Table columns ",table_columns)
            columns = input("Enter the columns you want in output separated by commas: ")
            columns = [col.strip() for col in columns.split(",")]
            print(columns)
            flag=True
            for col in columns:
                if col not in table_columns:
                    print("Invalid column: " + col)
                    flag=False
            if flag==True:
                condition = input("Enter the column name and condition: ")
                SQL_Query = f"SELECT {', '.join(columns)} FROM Students WHERE {condition}"
                print(SQL_Query)
                try:
                    cursor.execute(SQL_Query)
                    results = cursor.fetchall()
                    if results:
                        for row in results:
                            print(row)
                    else:
                        print("No results found.")
                    break
                except Exception as e:
                    print("Invalid Condition " , e)
                    print("If you want , enter custom query below ")
                    custom_query=False
                    custom_query_input = input("(Press N to try again )Custom Query ")
                    if custom_query_input != "N":
                        try:
                            cursor.execute(custom_query_input) 
                            results = cursor.fetchall()
                            if results:
                                for row in results:
                                    print(row)
                            else:
                                print("No results found.")
                        except Exception as e:
                            print("Invalid Custom Query " , e)

    elif table_name == "company":
        while True:
            # Define the table columns and get user input for columns and condition
            table_columns = ["company_id", "company_name", "hr_name", "hr_contact"]
            print("Table columns: ", table_columns)
            
            # Get user input for columns to select
            columns_input = input("Enter the columns you want in the output separated by commas: ")
            columns = [col.strip() for col in columns_input.split(",")]
            
            # Check if the entered columns are valid
            flag = all(col in table_columns for col in columns)
            if not flag:
                print("Invalid column(s) in the input.")
                continue
            
            # Get user input for the condition
            condition = input("Enter the column name and condition (e.g., company_name='XYZ'): ")
            
            # Check if the user wants to enter a custom query
            
                # Build and execute the SQL query based on selected columns and condition
            SQL_Query = f"SELECT {', '.join(columns)} FROM company WHERE {condition}"
            
            print("Executing the following query:")
            print(SQL_Query)
            
            try:
                cursor.execute(SQL_Query)
                results = cursor.fetchall()
                
                if results:
                    for row in results:
                        print(row)
                        
                else:
                    print("No results found.")
                break
            except Exception as e:
                custom_query_input = input("Do you want to enter a custom query (Y/N)? ").strip().lower()
            
                if custom_query_input == 'y':
                    custom_query = input("Enter your custom SQL query: ")
                    SQL_Query = custom_query
                    try:
                        cursor.execute(custom_query)
                        results = cursor.fetchall()
                        if results:
                            for row in results:
                                print(row)
                            break
                        else:
                            print("No results found.")
                        break
                    except Exception as e:
                        print("Error ",e)
                else:
                    print("Invalid Condition or Query: ", e)
            
    elif table_name == "Jobs":
        while True:
            # Define the table columns and get user input for columns and condition
            table_columns = ["company_id", "Job_id", "no_of_openings", "job_type", "selection_process", "package", "onsite"]
            print("Table columns: ", table_columns)
            
            # Get user input for columns to select
            columns_input = input("Enter the columns you want in the output separated by commas: ")
            columns = [col.strip() for col in columns_input.split(",")]
            
            # Check if the entered columns are valid
            flag = all(col in table_columns for col in columns)
            if not flag:
                print("Invalid column(s) in the input.")
                continue
            
            # Get user input for the condition
            condition = input("Enter the column name and condition (e.g., no_of_openings>10): ")
            
            try:
                # Build and execute the SQL query based on selected columns and condition
                SQL_Query = f"SELECT {', '.join(columns)} FROM Jobs WHERE {condition}"
                print("Executing the following query:")
                print(SQL_Query)
                
                cursor.execute(SQL_Query)
                results = cursor.fetchall()
                
                if results:
                    for row in results:
                        print(row)
                else:
                    print("No results found.")
                break
            except Exception as e:
                print("Query execution failed. Please enter a custom SQL query:")
                custom_query = input("Enter your custom SQL query: ")
                try:
                    cursor.execute(custom_query)
                    results = cursor.fetchall()
                    if results:
                        for row in results:
                            print(row)
                        break
                    else:
                        print("No results found.")
                    break
                except Exception as e:
                    print("Invalid custom query: ", e)      

    elif table_name == "basic_requirements_branch":
        while True:
            # Define the table columns and get user input for columns and condition
            table_columns = ["branch"]
            print("Table columns: ", table_columns)
            
            # Get user input for columns to select
            columns_input = input("Enter the columns you want in the output separated by commas: ")
            columns = [col.strip() for col in columns_input.split(",")]
            
            # Check if the entered columns are valid
            flag = all(col in table_columns for col in columns)
            if not flag:
                print("Invalid column(s) in the input.")
                continue
            
            # Get user input for the condition
            condition = input("Enter the column name and condition (e.g., branch='Computer Science'): ")
            
            try:
                # Build and execute the SQL query based on selected columns and condition
                SQL_Query = f"SELECT {', '.join(columns)} FROM basic_requirements_branch WHERE {condition}"
                print("Executing the following query:")
                print(SQL_Query)
                
                cursor.execute(SQL_Query)
                results = cursor.fetchall()
                
                if results:
                    for row in results:
                        print(row)
                else:
                    print("No results found.")
                break
            except Exception as e:
                print("Query execution failed. Please enter a custom SQL query:")
                custom_query = input("Enter your custom SQL query: ")
                try:
                    cursor.execute(custom_query)
                    results = cursor.fetchall()
                    if results:
                        for row in results:
                            print(row)
                    else:
                        print("No results found.")
                    break
                except Exception as e:
                    print("Invalid custom query: ", e)      


    elif table_name == "requirements":
        while True:
            # Define the table columns and get user input for columns and condition
            table_columns = ["Job_id", "min_cpi", "job_type", "backlogs", "branch"]
            print("Table columns: ", table_columns)
            
            # Get user input for columns to select
            columns_input = input("Enter the columns you want in the output separated by commas: ")
            columns = [col.strip() for col in columns_input.split(",")]
            
            # Check if the entered columns are valid
            flag = all(col in table_columns for col in columns)
            if not flag:
                print("Invalid column(s) in the input.")
                continue
            
            # Get user input for the condition
            condition = input("Enter the column name and condition (e.g., Job_id='ABC' AND min_cpi<9.0): ")
            
            try:
                # Build and execute the SQL query based on selected columns and condition
                SQL_Query = f"SELECT {', '.join(columns)} FROM requirements WHERE {condition}"
                print("Executing the following query:")
                print(SQL_Query)
                
                cursor.execute(SQL_Query)
                results = cursor.fetchall()
                
                if results:
                    for row in results:
                        print(row)
                else:
                    print("No results found.")
                break  # Break out of the loop if the query executes successfully
            except Exception as e:
                print("Query execution failed. Please enter a custom SQL query:")
                custom_query = input("Enter your custom SQL query: ")
                try:
                    cursor.execute(custom_query)
                    results = cursor.fetchall()
                    if results:
                        for row in results:
                            print(row)
                    else:
                        print("No results found.")
                    break  # Break out of the loop if the custom query executes successfully
                except Exception as e:
                    print("Invalid custom query: ", e)
            
    elif table_name == "job_application":
        while True:
            # Define the table columns and get user input for columns and condition
            table_columns = ["Job_id", "roll_no", "interview_schedule", "status"]
            print("Table columns: ", table_columns)
            
            # Get user input for columns to select
            columns_input = input("Enter the columns you want in the output separated by commas: ")
            columns = [col.strip() for col in columns_input.split(",")]
            
            # Check if the entered columns are valid
            flag = all(col in table_columns for col in columns)
            if not flag:
                print("Invalid column(s) in the input.")
                continue
            
            # Get user input for the condition
            condition = input("Enter the column name and condition (e.g., Job_id='ABC' AND status='Pending'): ")
            
            try:
                # Build and execute the SQL query based on selected columns and condition
                SQL_Query = f"SELECT {', '.join(columns)} FROM job_application WHERE {condition}"
                print("Executing the following query:")
                print(SQL_Query)
                
                cursor.execute(SQL_Query)
                results = cursor.fetchall()
                
                if results:
                    for row in results:
                        print(row)
                else:
                    print("No results found.")
                break  # Break out of the loop if the query executes successfully

            except Exception as e:
                print("Query execution failed. Please enter a custom SQL query:")
                custom_query = input("Enter your custom SQL query: ")
                try:
                    cursor.execute(custom_query)
                    results = cursor.fetchall()
                    if results:
                        for row in results:
                            print(row)
                    else:
                        print("No results found.")
                    break  # Break out of the loop if the custom query executes successfully
                    
                except Exception as e:
                    print("Invalid custom query: ", e)

    elif table_name == "courses":
        while True:
            # Define the table columns and get user input for columns and condition
            table_columns = ["course_id", "course_name"]
            print("Table columns: ", table_columns)
            
            # Get user input for columns to select
            columns_input = input("Enter the columns you want in the output separated by commas: ")
            columns = [col.strip() for col in columns_input.split(",")]
            
            # Check if the entered columns are valid
            flag = all(col in table_columns for col in columns)
            if not flag:
                print("Invalid column(s) in the input.")
                continue
            
            # Get user input for the condition
            condition = input("Enter the column name and condition (e.g., course_id=1234): ")
            
            try:
                # Build and execute the SQL query based on selected columns and condition
                SQL_Query = f"SELECT {', '.join(columns)} FROM courses WHERE {condition}"
                print("Executing the following query:")
                print(SQL_Query)
                
                cursor.execute(SQL_Query)
                results = cursor.fetchall()
                
                if results:
                    for row in results:
                        print(row)
                else:
                    print("No results found.")
                break  # Break out of the loop if the query executes successfully

            except Exception as e:
                print("Query execution failed. Please enter a custom SQL query:")
                custom_query = input("Enter your custom SQL query: ")
                try:
                    cursor.execute(custom_query)
                    results = cursor.fetchall()
                    if results:
                        for row in results:
                            print(row)
                    else:
                        print("No results found.")
                    break  # Break out of the loop if the custom query executes successfully
                except Exception as e:
                    print("Invalid custom query: ", e)

    elif table_name == "courses_completed":
        while True:
            # Define the table columns and get user input for columns and condition
            table_columns = ["roll_no", "course_id", "grade"]
            print("Table columns: ", table_columns)
            
            # Get user input for columns to select
            columns_input = input("Enter the columns you want in the output separated by commas: ")
            columns = [col.strip() for col in columns_input.split(",")]
            
            # Check if the entered columns are valid
            flag = all(col in table_columns for col in columns)
            if not flag:
                print("Invalid column(s) in the input.")
                continue
            
            # Get user input for the condition
            condition = input("Enter the column name and condition (e.g., roll_no=102): ")
            
            try:
                # Build and execute the SQL query based on selected columns and condition
                SQL_Query = f"SELECT {', '.join(columns)} FROM courses_completed WHERE {condition}"
                print("Executing the following query:")
                print(SQL_Query)
                
                cursor.execute(SQL_Query)
                results = cursor.fetchall()
                
                if results:
                    for row in results:
                        print(row)
                else:
                    print("No results found.")
                break  # Break out of the loop if the query executes successfully
            except Exception as e:
                print("Query execution failed. Please enter a custom SQL query:")
                custom_query = input("Enter your custom SQL query: ")
                try:
                    cursor.execute(custom_query)
                    results = cursor.fetchall()
                    if results:
                        for row in results:
                            print(row)
                    else:
                        print("No results found.")
                    break  # Break out of the loop if the custom query executes successfully
                except Exception as e:
                    print("Invalid custom query: ", e)