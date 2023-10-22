import csv
import psycopg2
from variables import *
import time

conn =  psycopg2.connect(database=database_name,
                         host=host_name,
                         user=user_name,
                         password=password_val,
                         port=port_name)


mycursor=conn.cursor()

available_tables = ["courses_completed", "courses", "job_application", "requirements", "basic_requirements_branch", "Students", "Jobs", "company" ]
print(f"Tables: {available_tables}")
table_name = input("Enter the Table Name to Delete the data:  ")

if table_name not in available_tables:
    print("Invalid table name")

elif table_name=="Students":
    while True:
        roll_no = input("Enter the roll no. of Student you want to delete: ")

        mycursor.execute("SELECT roll_no FROM Students")
        SQL_key="SELECT roll_no from students"
        mycursor.execute(SQL_key)
        roll_nos = mycursor.fetchall()
        roll_nos = [i[0] for i in roll_nos]

        if roll_no not in roll_nos:
            print("Invalid Roll No: " + roll_no)
        try:
            SQL=f"DELETE FROM STUDENTS WHERE roll_no={roll_no}"
            mycursor.execute(SQL)
            conn.commit()
            break
        except Exception as e:
            conn.rollback()
            print("Error: " + str(e))

elif table_name=="company":
    while True:
        company_id = input("Enter the id of company you want to delete: ")

        SQL_key="SELECT company_id FROM company"
        mycursor.execute(SQL_key)
        ids = mycursor.fetchall()
        ids = [i[0] for i in ids]

        print(ids)
        if company_id not in ids:
            print("Invalid company id: " + company_id)
        else:
            try:
                #For VARCHAR Datatype you need to add in ''..
                SQL=f"DELETE FROM company WHERE company_id='{company_id}'"
                mycursor.execute(SQL)
                conn.commit()
                break
            except Exception as e:
                conn.rollback()
                print("Error: " + str(e))


elif table_name=="Jobs":
    while True:
        Job_id = input("Enter the Job id of Job you want to delete: ")

        SQL_key="SELECT Job_id FROM Jobs"
        mycursor.execute(SQL_key)
        ids = mycursor.fetchall()
        ids = [i[0] for i in ids]

        print(ids)
        if Job_id not in ids:
            print("Invalid Job id: " + Job_id)
        else:	
            try:
                SQL=f"DELETE FROM Jobs WHERE Job_id='{Job_id}'"
                mycursor.execute(SQL)
                conn.commit()
                break
            except Exception as e:
                conn.rollback()
                print("Error: " + str(e))

elif table_name=="basic_requirements_branch":
    while True:
        branch = input("Enter the branch name you want to delete: ")

        SQL_key="SELECT branch FROM basic_requirements_branch"
        mycursor.execute(SQL_key)
        ids = mycursor.fetchall()
        ids = [i[0] for i in ids]

        print(ids)
        if branch not in ids:
            print("Invalid branch name: " + branch)
        else:	
            try:
                SQL=f"DELETE FROM basic_requirements_branch WHERE branch='{branch}'"
                mycursor.execute(SQL)
                conn.commit()
                break
            except Exception as e:
                conn.rollback()
                print("Error: " + str(e))

elif table_name=="requirements":
    while True:
        Job_id = input("Enter the Job id whose requirements you want to delete: ")

        SQL_key="SELECT job_id FROM requirements"
        mycursor.execute(SQL_key)
        ids = mycursor.fetchall()
        ids = [i[0] for i in ids]

        print(ids)
        if Job_id not in ids:
            print("Invalid Job id: " + Job_id)
        else:	
            try:
                SQL=f"DELETE FROM requirements WHERE Job_id='{Job_id}'"
                mycursor.execute(SQL)
                conn.commit()
                break
            except Exception as e:
                conn.rollback()
                print("Error: " + str(e))

elif table_name == "courses":
    while True:
        course_id = input("Enter the course id of the course you want to delete: ")

        SQL_key = "SELECT course_id FROM courses"
        mycursor.execute(SQL_key)
        ids = mycursor.fetchall()
        ids = [str(i[0]) for i in ids]  # Convert database values to strings for comparison
        print(ids)
        if course_id not in ids:
            print("Invalid course id: " + course_id)
        else:
            try:
                SQL = f"DELETE FROM courses WHERE course_id = {int(course_id)}"  # Convert course_id to int
                mycursor.execute(SQL)
                conn.commit()
                print("Course deleted successfully.")
                break
            except Exception as e:
                conn.rollback()
                print("Error: " + str(e))

elif table_name == "job_application":
    while True:
        Job_id = input("Enter the Job id of the Job you want to delete: ")
        roll_no = input("Enter the roll no of the Student you want to delete: " )

        # Check if the Job ID exists in the 'Jobs' table
        SQL_check = "SELECT Job_id FROM Jobs"
        mycursor.execute(SQL_check)
        job_ids = mycursor.fetchall()
        job_ids = [i[0] for i in job_ids]


        # Check if the Roll No exists in the 'Students' table
        SQL_check = "SELECT roll_no FROM Students"
        mycursor.execute(SQL_check)
        roll_nos = mycursor.fetchall()
        roll_nos = [i[0] for i in roll_nos]

        #Check if the combination fo job_id,rollno does n
        SQL_check = "SELECT job_id,roll_no FROM job_application"
        mycursor.execute(SQL_check)
        jobid_rollno = mycursor.fetchall()
        jobid_rollno = [(i[0],i[1]) for i in jobid_rollno] # Convert database values to strings for comparison
        
        print(jobid_rollno)
        
        if Job_id not in job_ids:
            print(f"Job ID: {Job_id} does not exist")
        elif int(roll_no) not in roll_nos:
            print(f"Roll No: {roll_no} does not exist")
        elif (Job_id,int(roll_no)) not in jobid_rollno:
            print(f"Job ID: {Job_id} and Roll No: {roll_no} does not exists")
        else:
            try:
                SQL = f"DELETE FROM job_application WHERE Job_id = '{Job_id}' and roll_no={int(roll_no)}"  # Convert course_id to int
                mycursor.execute(SQL)
                conn.commit()
                break
            except Exception as e:
                conn.rollback()
                print("Error: " + str(e))

elif table_name == "courses_completed":
    while True:
        roll_no = input("Enter the roll no of the Student you want to delete: " )
        course_id = input("Enter the course id of the course you want to delete: ")

        # Check if the Job ID exists in the 'Jobs' table
        SQL_check = "SELECT course_id FROM courses_completed"
        mycursor.execute(SQL_check)
        course_ids = mycursor.fetchall()
        course_ids = [i[0] for i in course_ids]


        # Check if the Roll No exists in the 'Students' table
        SQL_check = "SELECT roll_no FROM Students"
        mycursor.execute(SQL_check)
        roll_nos = mycursor.fetchall()
        roll_nos = [i[0] for i in roll_nos]

        #Check if the combination fo job_id,rollno does n
        SQL_check = "SELECT course_id,roll_no FROM courses_completed"
        mycursor.execute(SQL_check)
        course_id_rollno = mycursor.fetchall()
        course_id_rollno = [(i[0],i[1]) for i in course_id_rollno] # Convert database values to strings for comparison

        print(course_id_rollno)

        if int(course_id) not in course_ids:
            print(f"COURSE ID: {course_id} does not exist")
        elif int(roll_no) not in roll_nos:
            print(f"Roll No: {roll_no} does not exist")
        elif (int(course_id),int(roll_no)) not in course_id_rollno:
            print(f"Job ID: {course_id} and Roll No: {roll_no} does not exists")
        else:
            try:
                SQL = f"DELETE FROM courses_completed WHERE course_id = {int(course_id)} and roll_no={int(roll_no)}"  # Convert course_id to int
                mycursor.execute(SQL)
                conn.commit()
                break
            except Exception as e:
                conn.rollback()
                print("Error: " + str(e))


SQL="SELECT * FROM Students "
mycursor.execute(SQL)
print("\n\nStudents ",mycursor.fetchall())

SQL="SELECT * FROM Company "
mycursor.execute(SQL)
print("\n\nCompany ",mycursor.fetchall())

SQL="SELECT * FROM Jobs "
mycursor.execute(SQL)
print("\n\nJobs ",mycursor.fetchall())

SQL="SELECT * FROM basic_requirements_branch "
mycursor.execute(SQL)
print("\n\nbasic_requirements_branch ",mycursor.fetchall())

SQL="SELECT * FROM requirements "
mycursor.execute(SQL)
print("\n\nRequirements ",mycursor.fetchall())

SQL="SELECT * FROM courses "
mycursor.execute(SQL)
print("\n\ncourses ",mycursor.fetchall())

SQL="SELECT * FROM courses_completed "
mycursor.execute(SQL)
print("\n\ncourses Completed ",mycursor.fetchall())

SQL="SELECT * FROM job_application"
mycursor.execute(SQL)
print("\n\nApplications ",mycursor.fetchall())

mycursor.close()
conn.close()