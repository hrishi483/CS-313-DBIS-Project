# import csv
import psycopg2
# from variables import *
# import time

# conn =  psycopg2.connect(database=database_name,
#                          host=host_name,
#                          user=user_name,
#                          password=password_val,
#                          port=port_name)


# mycursor=conn.cursor()



def update_data(conn,mycursor):
    available_tables = ["courses_completed", "courses", "job_application", "requirements", "basic_requirements_branch", "Students", "Jobs", "company" ]
    print(f"Tables : {available_tables}")
    table_name = input("Enter the Table Name to UPDATE the data:  ")

    if table_name not in available_tables:
        print("Invalid table name")

    elif table_name == "Students":
        while True:
            roll_no = input("Enter the roll no. of the student you want to update: ")
            new_student_name = input("Enter the updated student name: ")
            new_cpi = input("Enter the updated CPI: ")
            new_branch = input("Enter the updated branch: ")
            new_credits = input("Enter the updated credits: ")

            SQL_key = "SELECT roll_no FROM Students"
            mycursor.execute(SQL_key)
            roll_nos = mycursor.fetchall()
            roll_nos = [i[0] for i in roll_nos]

            if roll_no not in roll_nos:
                print("Invalid Roll No: " + roll_no)
            else:
                try:
                    SQL = f"UPDATE Students SET student_name = '{new_student_name}', cpi = {new_cpi}, branch = '{new_branch}', credits = {new_credits} WHERE roll_no = {roll_no}"
                    mycursor.execute(SQL)
                    conn.commit()
                    print("Student record updated successfully.")
                    break
                except Exception as e:
                    conn.rollback()
                    print("Error: " + str(e))

    elif table_name == 'company':
        while True:
            id = input("Enter Company ID to update: ")
            comp_name = input("Enter updated Company Name: ")
            name = input("Enter updated HR Name: ")
            contact = input("Enter updated HR Contact: ")

            SQL_key = "SELECT company_id FROM company"
            mycursor.execute(SQL_key)
            comp_ids = mycursor.fetchall()
            comp_ids = [i[0] for i in comp_ids]

            if id not in comp_ids:
                print(f"Company with ID = {id} does not exist in the database.")
            else:
                try:
                    SQL = f"UPDATE company SET company_name = '{comp_name}', hr_name = '{name}', hr_contact = '{contact}' WHERE company_id = '{id}'"
                    mycursor.execute(SQL)
                    conn.commit()
                    print(f"Company record with ID = {id} updated successfully.")
                    break
                except Exception as e:
                    conn.rollback()
                    print("Error: " + str(e))

    elif table_name == 'Jobs':
        while True:
            comp_id = input("Enter Company ID: ")
            Job_id = input("Enter Job ID to update: ")
            openings = int(input("Enter updated number of openings: "))
            job_type = input("Enter updated type of job: ")
            selection_process = input("Enter updated selection process: ")
            package = int(input("Enter updated package: "))
            onsite_input = input("Enter T for onsite and F for remote: ")

            onsite = False
            if onsite_input == "T":
                onsite = True
            elif onsite_input == "F":
                onsite = False

            SQL_Jobid = "SELECT Job_id FROM Jobs"
            mycursor.execute(SQL_Jobid)
            Job_ids = mycursor.fetchall()
            Job_ids = [i[0] for i in Job_ids]

            SQL_compid = "SELECT company_id FROM company"
            mycursor.execute(SQL_compid)
            comp_ids = mycursor.fetchall()
            comp_ids = [i[0] for i in comp_ids]

            if comp_id not in comp_ids:
                print(f"Company with ID = {comp_id} does not exist in the database.")
            elif onsite not in [True, False]:
                print("Invalid entry for the 'onsite' field. Press T for onsite and F for remote.")
            elif Job_id not in Job_ids:
                print(f"Job with ID = {Job_id} does not exist in the database.")
            else:
                try:
                    SQL = f"UPDATE Jobs SET no_of_openings = {openings}, job_type = '{job_type}', selection_process = '{selection_process}', package = {package}, onsite = {onsite} WHERE company_id = '{comp_id}' AND Job_id = '{Job_id}'"
                    mycursor.execute(SQL)
                    conn.commit()
                    print(f"Job record with Company ID = {comp_id} and Job ID = {Job_id} updated successfully.")
                    break
                except Exception as e:
                    conn.rollback()
                    print("Error: " + str(e))

    elif table_name == "basic_requirements_branch":
        branch_name = input("Enter the branch name you want to update: ")
        while True:
            SQL_check = "SELECT branch FROM basic_requirements_branch"
            mycursor.execute(SQL_check)
            branches = mycursor.fetchall()
            branches = [i[0] for i in branches]

            if branch_name not in branches:
                print(f"Branch: {branch_name} does not exist in the database.")
            else:
                new_branch_name = input("Enter the updated branch name: ")
                try:
                    SQL = f"UPDATE basic_requirements_branch SET branch = '{new_branch_name}' WHERE branch = '{branch_name}'"
                    mycursor.execute(SQL)
                    conn.commit()
                    print(f"Branch record '{branch_name}' updated to '{new_branch_name}' successfully.")
                    break
                except Exception as e:
                    conn.rollback()
                    print("Error: " + str(e))

    elif table_name == 'requirements':
        while True:
            Job_id = input("Enter Job ID for the requirement you want to update: ")
            new_min_cpi = round(float(input("Enter the updated minimum CPI required: "), 2))
            new_backlogs = int(input("Enter the updated number of backlogs allowed: "))
            new_job_type = input("Enter the updated job type: ")
            new_branch = input("Enter the updated branch: ")

            # Check if the Job ID exists
            SQL_Jobid = "SELECT Job_id FROM Jobs"
            mycursor.execute(SQL_Jobid)
            Job_ids = mycursor.fetchall()
            Job_ids = [i[0] for i in Job_ids]

            if Job_id not in Job_ids:
                print(f"Job with ID = {Job_id} does not exist in the DB.")
            else:
                try:
                    SQL = f"UPDATE requirements SET min_cpi = {new_min_cpi}, backlogs = {new_backlogs}, job_type = '{new_job_type}', branch = '{new_branch}' WHERE Job_id = '{Job_id}'"
                    mycursor.execute(SQL)
                    conn.commit()
                    print(f"Requirement for Job ID = {Job_id} updated successfully.")
                    break
                except Exception as e:
                    conn.rollback()
                    print("Error: " + str(e))

    elif table_name == 'courses':
        while True:
            course_id = int(input("Enter Course ID you want to update: "))
            new_course_name = input("Enter the updated course name: ")

            # Check if the Course ID exists
            SQL_course_ids = "SELECT course_id FROM courses"
            mycursor.execute(SQL_course_ids)
            course_ids = mycursor.fetchall()
            course_ids = [i[0] for i in course_ids]

            if course_id not in course_ids:
                print(f"Course with ID = {course_id} does not exist in the DB.")
            else:
                try:
                    SQL = f"UPDATE courses SET course_name = '{new_course_name}' WHERE course_id = {course_id}"
                    mycursor.execute(SQL)
                    conn.commit()
                    print(f"Course with ID = {course_id} updated successfully.")
                    break
                except Exception as e:
                    conn.rollback()
                    print("Error: " + str(e))

    elif table_name == 'courses_completed':
        while True:
            roll_no = int(input("Enter the roll no of the student: "))
            course_id = int(input("Enter the course id of the completed course: "))
            new_grade = input("Enter the updated grade for the course: ")

            # Check if the combination of roll_no and course_id exists in the 'courses_completed' table
            SQL_check = "SELECT roll_no, course_id FROM courses_completed"
            mycursor.execute(SQL_check)
            roll_no_courseid = mycursor.fetchall()
            roll_no_courseid = [(i[0], i[1]) for i in roll_no_courseid]

            if (roll_no, course_id) not in roll_no_courseid:
                print(f"Entry for Roll No={roll_no}, Course ID: {course_id} does not exist")
            else:
                try:
                    SQL = f"UPDATE courses_completed SET grade = '{new_grade}' WHERE roll_no = {roll_no} AND course_id = {course_id}"
                    mycursor.execute(SQL)
                    conn.commit()
                    print(f"Grade for Roll No={roll_no}, Course ID: {course_id} updated successfully.")
                    break
                except Exception as e:
                    conn.rollback()
                    print("Error: " + str(e))

    elif table_name == "job_application":
        while True:
            Job_id = input("Enter Job ID: ")
            roll_no = int(input("Enter Roll No: "))
            new_interview_schedule = input("Enter the updated interview schedule (YYYY-MM-DD): ")
            new_status = input("Enter the updated status: ")

            # Check if the combination of Job ID and Roll No exists in the 'job_application' table
            SQL_check = "SELECT Job_id, roll_no FROM job_application"
            mycursor.execute(SQL_check)
            jobid_rollno = mycursor.fetchall()
            jobid_rollno = [(i[0], i[1]) for i in jobid_rollno]

            if (Job_id, roll_no) not in jobid_rollno:
                print(f"Application for Job ID: {Job_id}, Roll No: {roll_no} does not exist")
            else:
                try:
                    SQL = f"UPDATE job_application SET interview_schedule = '{new_interview_schedule}', status = '{new_status}' WHERE Job_id = '{Job_id}' AND roll_no = {roll_no}"
                    mycursor.execute(SQL)
                    conn.commit()
                    print(f"Application for Job ID: {Job_id}, Roll No: {roll_no} updated successfully.")
                    break
                except Exception as e:
                    conn.rollback()
                    print("Error: " + str(e))

available_tables = ["courses_completed", "courses", "job_application", "requirements", "basic_requirements_branch", "Students", "Jobs", "company" ]
# print(f"Tables: {available_tables}")
# table_name = input("Enter the Table Name to Delete the data:  ")
# update_data(table_name)


# SQL="SELECT * FROM Students "
# mycursor.execute(SQL)
# print("\n\nStudents ",mycursor.fetchall())

# SQL="SELECT * FROM Company "
# mycursor.execute(SQL)
# print("\n\nCompany ",mycursor.fetchall())

# SQL="SELECT * FROM Jobs "
# mycursor.execute(SQL)
# print("\n\nJobs ",mycursor.fetchall())

# SQL="SELECT * FROM basic_requirements_branch "
# mycursor.execute(SQL)
# print("\n\nbasic_requirements_branch ",mycursor.fetchall())

# SQL="SELECT * FROM requirements "
# mycursor.execute(SQL)
# print("\n\nRequirements ",mycursor.fetchall())

# SQL="SELECT * FROM courses "
# mycursor.execute(SQL)
# print("\n\ncourses ",mycursor.fetchall())

# SQL="SELECT * FROM courses_completed "
# mycursor.execute(SQL)
# print("\n\ncourses Completed ",mycursor.fetchall())

# SQL="SELECT * FROM job_application"
# mycursor.execute(SQL)
# print("\n\nApplications ",mycursor.fetchall())

# mycursor.close()
# conn.close()