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
table_name = input("Enter the Table Name to insert the data:  ")

if table_name not in available_tables:
    print("Invalid table name")

elif table_name == "Students":
        while True:
            id = int(input("Enter Student ID: "))
            name = input("Enter the Student Name: ")
            CPI = round(float(input("Enter the Student CPI: ")),2)
            branch = input("Enter the Student Branch: ")
            credits = int(input("Enter the Student Credits: "))
                

            execute_query=False
            if CPI<=10.00 and credits<=250:  #Just to check that user does not enter any random number
                execute_query=True
                print("*"*54)
            else:
                print("CPI is in range of [0,10] and credits is in range of [0,250]")
                print("*"*54)
            if execute_query:
                try:
                    SQL = "INSERT INTO Students VALUES(%s, %s, %s, %s, %s)"
                    values = (id,name,CPI,branch,credits)
                    
                    SQL_key="SELECT roll_no from students"
                    mycursor.execute(SQL_key)
                    roll_nos = mycursor.fetchall()
                    roll_nos = [i[0] for i in roll_nos]
                    
                    if id not in roll_nos:
                        mycursor.execute(SQL,values)
                        conn.commit()
                        break
                    else:
                        print(f"Student with id = {id} already exists in DB")
                        print("*"*54)
                except psycopg2.Error as e:               
                    print("Error: ",e)
                    print("*"*54)
                    conn.rollback()


elif table_name == 'company':
     while True:
            id = input("Enter Company ID: ")
            comp_name=input("Enter Company Name: ")
            name = input("Enter the HR Name: ")
            contact = input("Enter HR Contact: ")
            
            SQL_key="SELECT company_id from company"
            mycursor.execute(SQL_key)
            comp_ids = mycursor.fetchall()
            comp_ids = [i[0] for i in comp_ids]
            if len(contact)==10 : #phone number length should be 10 
                SQL="INSERT INTO company VALUES (%s, %s, %s, %s)"
                values = (id,comp_name,name,contact)    
                if id in comp_ids:                    
                    print(f"Company with id = {id} already exists in DB")
                else:
                    try:
                        mycursor.execute(SQL,values)
                        conn.commit() 
                        break
                    except Exception as e:
                        print(f"Error: {e}")
                        conn.rollback()            
            else:
                   print(f"Enter a valid contact number")


elif table_name == 'Jobs':
     while True:
            comp_id = input("Enter Company ID: ")
            Job_id=input("Enter Job Id: ")
            openings=int(input("Enter the number of openings: "))
            job_type = input("Enter the type of job: ")
            selection_process = input("Enter the selection process: ")
            package=int(input("Enter the package: "))
            onsite_input = input("Enter T for onsite and F for remote: ")
            
            onsite=False
            if onsite=="T" :
                print("set to true")
                onsite==True
                print(onsite)
            elif onsite=="F":
                print("set to False")                
                onsite=False
                
            if onsite==True or onsite==False:
                SQL_Jobid="SELECT Job_id from Jobs"
                mycursor.execute(SQL_Jobid)
                Job_ids = mycursor.fetchall()
                Job_ids = [i[0] for i in Job_ids]

                SQL_compid="SELECT company_id from company"
                mycursor.execute(SQL_compid)
                comp_ids=mycursor.fetchall()
                comp_ids=[i[0] for i in comp_ids]

                if comp_id in comp_ids : #phone number length should be 10 
                    SQL="INSERT INTO Jobs  VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    values = (comp_id,Job_id,openings,job_type,selection_process,package,onsite)    
                    if Job_id in Job_ids:                    
                        print(f"Company with id = {id} already exists in DB")

                    else:
                        try:
                            mycursor.execute(SQL,values)
                            conn.commit() 
                            break
                        except Exception as e:
                            print(f"Error: {e}")
                            conn.rollback() 
                else:
                     print(f"Comapny with id = {comp_id} does not exists")           
            else:
                print(onsite)
                print(f"Invalid entry for filed onsite :Press T for onsite and F for remote")

elif table_name=="basic_requirements_branch":
    branch_name = input("Enter branch name: ")
    while True:
        SQL_check = "SELECT branch from basic_requirements_branch"
        mycursor.execute(SQL_check)
        branches = mycursor.fetchall()
        branches = [i[0] for i in branches]
        print(branches)
        if  branch_name in branches:
            print(f"branch: {branch_name} already exists")
        else:
            try:
                SQL = "INSERT INTO basic_requirements_branch (branch) VALUES(%s) "
                values = (branch_name,)
                mycursor.execute(SQL, values)
                conn.commit()
                break
            except Exception as e:
                conn.rollback()

elif table_name == 'requirements':
     while True:
        Job_id=input("Enter Job Id: ")
        min_cpi=round(float(input("Enter the min CPI required: ")),2)
        backlogs=int(input("Enter number of backlogs Allowed: "))
        job_type = input("Enter the type of job: ")
        branch = input("Enter the branch: ")
            
        
        if min_cpi <= 10 and min_cpi >= 0:
            # Check if the Job ID exists
            SQL_Jobid = "SELECT Job_id FROM Jobs"
            mycursor.execute(SQL_Jobid)
            Job_ids = mycursor.fetchall()
            Job_ids = [i[0] for i in Job_ids]
            
            SQL_Jobids_existing = "Select job_id from requirements"
            mycursor.execute(SQL_Jobids_existing)
            exist_Jobids = mycursor.fetchall()
            exist_Jobids = [i[0] for i in exist_Jobids]

            SQL_branch = "SELECT branch FROM basic_requirements_branch"
            mycursor.execute(SQL_branch)
            branches = mycursor.fetchall()
            branches = [i[0] for i in branches]

            

            if Job_id not in Job_ids:
                print("Job ids = ",Job_id)
                print(f"Job with ID = {Job_id} does not exists in the DB")
            elif Job_id in exist_Jobids:
                print("Job id already exists in requirements Table")  
            elif branch not in branches:
                print(f"branch={branch} does not exists in basic_requirements_branch Table")
            else:
                SQL = "INSERT INTO requirements (Job_id, min_cpi, backlogs, job_type, branch) VALUES (%s, %s, %s, %s, %s)"
                values = (Job_id, min_cpi, backlogs, job_type, branch)
            
                try:
                    mycursor.execute(SQL, values)
                    conn.commit()
                    print(f"Job with ID = {Job_id} inserted into the requirements table.")
                    break
                except Exception as e:
                    print(f"Error: {e}")
                    conn.rollback()
        else:
            print("CPI should be in the range of [0, 10]")
            
elif table_name=="courses":
    while True:
        course_id = int(input("Enter Course id: "))
        course_name = input("Enter Course name: ")

        SQL_courses = "SELECT course_id from courses"
        mycursor.execute(SQL_courses)
        course_ids=mycursor.fetchall()
        course_ids=[i[0] for i in course_ids]

        if course_id in course_ids:
            print("Course id already exists in course table")
        else:
            try:
                SQL="Insert into courses (course_id, course_name) VALUES(%s, %s)"
                values=(course_id,course_name)
                mycursor.execute(SQL,values)
                conn.commit()
                break
            except Exception as e:
                print("Error: ",e )
                conn.rollback()


elif table_name=="courses_completed":
     while True:
        roll_no = int(input("Enter roll no: "))
        course_id = int(input("Enter course id: "))
        grade = input("Enter grade for the course: ")

        # Check if the course_id exists in the 'courses' table
        SQL_check = "SELECT course_id FROM courses"
        mycursor.execute(SQL_check)
        course_ids = mycursor.fetchall()
        course_ids = [i[0] for i in course_ids]

        # Check if the roll_no exists in the 'Students' table
        SQL_check = "SELECT roll_no FROM Students"
        mycursor.execute(SQL_check)
        roll_nos = mycursor.fetchall()
        roll_nos = [i[0] for i in roll_nos]

        # Check if the combination of roll_no and course_id already exists in 'courses_completed' table
        SQL_check = "SELECT roll_no, course_id FROM courses_completed"
        mycursor.execute(SQL_check)
        roll_no_courseid = mycursor.fetchall()
        roll_no_courseid = [(i[0], i[1]) for i in roll_no_courseid]

        if course_id not in course_ids:
            print(f"Course ID: {course_id} does not exist")
        elif roll_no not in roll_nos:
            print(f"Roll No: {roll_no} does not exist")
        elif (roll_no, course_id) in roll_no_courseid:
            print(f"Entry for Roll No={roll_no}, Course ID: {course_id} already exists")
        else:
            try:
                SQL = "INSERT INTO courses_completed (roll_no, course_id, grade) VALUES (%s, %s, %s)"
                values = (roll_no, course_id, grade)
                mycursor.execute(SQL, values)
                conn.commit()
                print("Inserted successfully")
                break
            except Exception as e:
                conn.rollback()

if table_name == "job_application":
    while True:
        Job_id = input("Enter Job ID: ")
        roll_no = int(input("Enter Roll No: "))
        interview_schedule = input("Enter Interview Schedule (YYYY-MM-DD): ")
        status = input("Enter Status: ")

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

        SQL_check = "SELECT job_id,roll_no FROM job_application"
        mycursor.execute(SQL_check)
        jobid_rollno = mycursor.fetchall()
        jobid_rollno = [(i[0],i[1]) for i in jobid_rollno]
        
        if Job_id not in job_ids:
            print(f"Job ID: {Job_id} does not exist")
        elif roll_no not in roll_nos:
            print(f"Roll No: {roll_no} does not exist")
        elif (Job_id,roll_no) in jobid_rollno:
            print(f"Job ID: {Job_id} and Roll No: {roll_no} alreaady exists")
        else:
            try:
                SQL = "INSERT INTO job_application (Job_id, roll_no, interview_schedule, status) VALUES (%s, %s, %s, %s)"
                values = (Job_id, roll_no, interview_schedule, status)
                mycursor.execute(SQL, values)
                conn.commit()
                print("Inserted successfully")
                break
            except Exception as e:
                conn.rollback()
                print(f"Error: {e}")


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
print("\n\ncourses completed ",mycursor.fetchall())

SQL="SELECT * FROM job_application"
mycursor.execute(SQL)
print("\n\nApplications ",mycursor.fetchall())

mycursor.close()
conn.close()