import streamlit as st
import streamlit as st
from variables import *
import psycopg2


# st.title("IIT Placement Cell")

# st.write("DBIS Lab Project ")

# Create a sidebar with options
options = ["Insert", "Delete", "Update","Search"]
selected_option = st.sidebar.radio("Select an option", options)

# Display the selected option
st.write(f"You selected: {selected_option}")

def insert_data(conn,mycursor):
    available_tables = ["courses_completed", "courses", "job_application", "requirements", "basic_requirements_branch", "Students", "Jobs", "company"]

    st.title("Table Name Input")

    st.write(f"Available Tables: {available_tables}")

    table_name = st.text_input("Enter the Table Name to insert the data:")

    if table_name:
        if table_name in available_tables:
            st.write(f"You entered: {table_name}")
        else:
            st.write("Invalid table name")
    
        

        if table_name == "Students":
                # while True:
                    with st.form(key="form1"):
                        id_input = st.number_input("Enter Student ID: ", key='id',min_value=0.0,value=150.0)
                        id_value = int(id_input)

                        name = st.text_input("Enter the Student Name: ", placeholder='Jolly')

                        CPI_input = st.number_input("Enter the Student CPI: ", key="CPI", min_value=0.0, max_value=10.0,value=8.5)
                        CPI_value = round(float(CPI_input), 3)

                        branch = st.text_input("Enter the Student Branch: ", placeholder='4', key="branch")

                        credits_input = st.number_input("Enter the Student Credits: ", key="credits", min_value=0.0, max_value=300.0,value=70.0)
                        credits_value = int(credits_input)
                        
                        submit=st.form_submit_button(label="Insert")
                    
                    if submit:
                        execute_query=False
                        if id_input and name and CPI_input and branch and credits:
                            if CPI_value<=10.00 and credits_value   <=250:  #Just to check that user does not enter any random number
                                execute_query=True
                                st.write("*"*54)
                            else:
                                st.write("CPI is in range of [0,10] and credits is in range of [0,250]")
                                st.write("*"*54)
                            if execute_query:
                                try:
                                    SQL_key = "INSERT INTO Students VALUES(%s, %s, %s, %s, %s)"
                                    values = (id_input,name,CPI_value,branch,credits_value)
                                    
                                    SQL_placeholder="SELECT roll_no from students"
                                    mycursor.execute(SQL_placeholder)
                                    roll_nos = mycursor.fetchall()
                                    roll_nos = [i[0] for i in roll_nos]
                                    
                                    
                                    if id_input not in roll_nos:
                                        mycursor.execute(SQL_key,values)
                                        conn.commit()
                                        st.success(f"Student with roll number {id_input,name,CPI_value,branch,credits_value} inserted successfully", icon="✅")
                                        # break
                                    else:
                                        st.error(f"Student with id = {id_input} already exists in DB")
                                        st.write("*"*54)
                                except psycopg2.Error as e:               
                                    st.write("Error: ",e)
                                    st.write("*"*54)
                                    conn.rollback()

        elif table_name == 'company':
            with st.form("form2"):
                id = st.text_input("Enter Company ID:", placeholder="company_id")
                comp_name = st.text_input("Enter Company Name:", placeholder="company_name")
                name = st.text_input("Enter the HR Name:", placeholder="hr_name")
                contact = st.text_input("Enter HR Contact:", placeholder="hr_contact")
                submit=st.form_submit_button(label="Insert")
                    
                if submit:
                    SQL_placeholder="SELECT company_id from company"
                    mycursor.execute(SQL_placeholder)
                    comp_ids = mycursor.fetchall()
                    comp_ids = [i[0] for i in comp_ids]
                    if len(contact)==10 : #phone number length should be 10 
                        SQL="INSERT INTO company VALUES (%s, %s, %s, %s)"
                        values = (id,comp_name,name,contact)    
                        if id in comp_ids:                    
                            st.error(f"Company with id = {id} already exists in DB")
                        else:
                            try:
                                mycursor.execute(SQL,values)
                                conn.commit() 
                                st.success(f"Company with {id,comp_name,name,contact} inserted successfully")
                            except Exception as e:
                                st.error(f"Error: {e}")
                                conn.rollback()            
                    else:
                        st.error(f"Enter a valid contact number")

        elif table_name == 'Jobs':
            with st.form(key="form3"):
                    st.title("Insert Job Data")

                    comp_id = st.text_input("Enter Company ID:")
                    Job_id = st.text_input("Enter Job ID:")
                    openings = st.number_input("Enter the number of openings:")
                    openings = int(openings)
                    job_type = st.text_input("Enter the type of job:")
                    selection_process = st.text_input("Enter the selection process:")
                    package = st.number_input("Enter the package:")
                    package = int(package)
                    onsite_input = st.text_input("Enter T for onsite and F for remote:")
                    submit = st.form_submit_button("Insert")
                    
                    if submit:
                        onsite=False
                        if onsite_input=="T" :
                            onsite==True                          
                        elif onsite_input=="F":
                            onsite=False
    
                        if onsite_input=="T" or onsite_input=="F":
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
                                    st.error(f"Company with id = {Job_id} already exists in DB")

                                else:
                                    try:
                                        mycursor.execute(SQL,values)
                                        conn.commit() 
                                        st.success(f"Company with {comp_id,Job_id,openings,job_type,selection_process,package,onsite_input} inserted successfully")
                                    except Exception as e:
                                        st.write(f"Error: {e}")
                                        conn.rollback() 
                            else:
                                st.error(f"Company with id = {comp_id} does not exists")           
                        else:
                            # st.write(onsite)
                            st.error(f"Invalid entry for filed onsite :Press T for onsite and F for remote")

        elif table_name=="basic_requirements_branch":
            with st.form(key="form4"):
                branch_name = st.text_input("Enter branch name: ",placeholder="branch_name")
                st.form_submit_button("Insert")

                SQL_check = "SELECT branch from basic_requirements_branch"
                mycursor.execute(SQL_check)
                branches = mycursor.fetchall()
                branches = [i[0] for i in branches]
                if  branch_name in branches:
                    st.error(f"branch: {branch_name} already exists")
                else:
                    try:
                        SQL = "INSERT INTO basic_requirements_branch (branch) VALUES(%s) "
                        values = (branch_name,)
                        mycursor.execute(SQL, values)
                        conn.commit()
                        st.success(f"Branch: {branch_name} inserted successfully")
                    except Exception as e:
                        conn.rollback()

        elif table_name == 'requirements':
            with st.form(key="form5"):
                Job_id = st.text_input("Enter Job Id:", placeholder='job_id')

                min_cpi = st.number_input("Enter the min CPI required:", placeholder='min_cpi',min_value=0.00,max_value=10.00)
                min_cpi = round(float(min_cpi), 2)

                backlogs = st.number_input("Enter number of backlogs Allowed:", placeholder='backlogs',min_value=0.00,max_value=5.00)
                backlogs = int(backlogs)

                job_type = st.text_input("Enter the type of job:", placeholder='job_type')
                branch = st.text_input("Enter the branch:", placeholder='branch')
                submit = st.form_submit_button("Insert")
                
                if submit:
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
                            st.error(f"Job with ID = {Job_id} does not exists in the DB")
                        elif Job_id in exist_Jobids:
                            st.error("Job id already exists in requirements Table")  
                        elif branch not in branches:
                            st.error(f"branch={branch} does not exists in basic_requirements_branch Table")
                        else:
                            SQL = "INSERT INTO requirements (Job_id, min_cpi, backlogs, job_type, branch) VALUES (%s, %s, %s, %s, %s)"
                            values = (Job_id, min_cpi, backlogs, job_type, branch)
                        
                            try:
                                mycursor.execute(SQL, values)
                                conn.commit()
                                
                                st.success(f"Requirement entry: {Job_id, min_cpi, backlogs, job_type, branch} inserted successfully")
                            except Exception as e:
                                st.write(f"Error: {e}")
                                conn.rollback()
                    else:
                        st.error("CPI should be in the range of [0, 10]")
                    
        elif table_name=="courses":
            with st.form(key="form5"):
                course_id = st.number_input("Enter Course id: ",placeholder='183')
                course_id = int(course_id)
                course_name = st.text_input("Enter Course name: ",placeholder='Data Science')

                SQL_courses = "SELECT course_id from courses"
                mycursor.execute(SQL_courses)
                course_ids=mycursor.fetchall()
                course_ids=[i[0] for i in course_ids]
                submit = st.form_submit_button("Insert")

                if submit :
                    if course_id in course_ids:
                        st.error("Course id already exists in course table")
                    else:
                        try:
                            SQL="Insert into courses (course_id, course_name) VALUES(%s, %s)"
                            values=(course_id,course_name)
                            mycursor.execute(SQL,values)
                            conn.commit()
                            st.success(f"course:{course_id,course_name} inserted successfully" )
                        except Exception as e:
                            st.error("Error: ",e )
                            conn.rollback()

        elif table_name=="courses_completed":
            with st.form("form 6"):
                roll_no = st.number_input("Enter roll no: ",placeholder='10')
                roll_no = int(roll_no)
                course_id = st.number_input("Enter course id: ",placeholder='11')
                course_id = int(course_id)
                grade = st.text_input("Enter grade for the course: ",placeholder='course_grade')
                submit = st.form_submit_button("Insert")
                # Check if the course_id exists in the 'courses' table
                if submit:
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
                        st.error(f"Course ID: {course_id} does not exist")
                        print(course_ids)
                    elif roll_no not in roll_nos:
                        st.error(f"Roll No: {roll_no} does not exist")
                        print(roll_nos)
                    elif (roll_no, course_id) in roll_no_courseid:
                        st.error(f"Entry for Roll No={roll_no}, Course ID: {course_id} already exists")
                    else:
                        try:
                            SQL = "INSERT INTO courses_completed (roll_no, course_id, grade) VALUES (%s, %s, %s)"
                            values = (roll_no, course_id, grade)
                            mycursor.execute(SQL, values)
                            conn.commit()
                            st.write("courses_completed: ",roll_no, course_id, grade)
                            st.success()
                        except Exception as e:
                            conn.rollback()

        elif table_name == "job_application":
            with st.form(key="form7"):
                Job_id = st.text_input("Enter Job ID: ",placeholder='job_id')
                roll_no = st.number_input("Enter Roll No: ",placeholder='12')
                roll_no = int(roll_no)
                interview_schedule = st.date_input("Enter Interview Schedule (YYYY-MM-DD): ",placeholder='schedule')
                status = st.text_input("Enter Status: ",placeholder='status')

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
                    st.write(f"Job ID: {Job_id} does not exist")
                elif roll_no not in roll_nos:
                    st.write(f"Roll No: {roll_no} does not exist")
                elif (Job_id,roll_no) in jobid_rollno:
                    st.write(f"Job ID: {Job_id} and Roll No: {roll_no} alreaady exists")
                else:
                    try:
                        SQL = "INSERT INTO job_application (Job_id, roll_no, interview_schedule, status) VALUES (%s, %s, %s, %s)"
                        values = (Job_id, roll_no, interview_schedule, status)
                        mycursor.execute(SQL, values)
                        conn.commit()
                        st.success(f"Record {Job_id, roll_no, interview_schedule, status} Inserted successfully")
                        
                    except Exception as e:
                        conn.rollback()
                        st.write(f"Error: {e}")

def delete_data(conn,mycursor):
    available_tables = ["courses_completed", "courses", "job_application", "requirements", "basic_requirements_branch", "Students", "Jobs", "company" ]
    st.write(f"Tables : {available_tables}")
    
    st.title("Table Name Input")

    st.write(f"Available Tables: {available_tables}")

    table_name = st.text_input("Enter the Table Name to DELETE the data:")
    if table_name not in available_tables:
        st.error("Invalid table name")

    elif table_name=="Students":
        with st.form(key="form 9"):
            roll_no = st.text_input("Enter the roll no. of Student you want to delete: ")
            submit = st.form_submit_button("Delete")
            if submit:
                mycursor.execute("SELECT roll_no FROM Students")
                SQL_placeholder="SELECT roll_no from students"
                mycursor.execute(SQL_placeholder)
                roll_nos = mycursor.fetchall()
                roll_nos = [i[0] for i in roll_nos]

                if roll_no not in roll_nos:
                    st.error("Invalid Roll No: " + roll_no)
                try:
                    SQL=f"DELETE FROM STUDENTS WHERE roll_no={roll_no}"
                    mycursor.execute(SQL)
                    conn.commit()
                    st.success("Student with roll_no={roll_no} Successfully deleted")
                except Exception as e:
                    conn.rollback()
                    st.write("Error: " + str(e))

    elif table_name=="company":
        with st.form(key="form 10"):
            company_id = st.text_input("Enter the id of company you want to delete: ")
            submit = st.form_submit_button("Delete")
            if submit:
                SQL_placeholder="SELECT company_id FROM company"
                mycursor.execute(SQL_placeholder)
                ids = mycursor.fetchall()
                ids = [i[0] for i in ids]

                if company_id not in ids:
                    st.error("Invalid company id: " + company_id)
                else:
                    try:
                        #For VARCHAR Datatype you need to add in ''..
                        SQL=f"DELETE FROM company WHERE company_id='{company_id}'"
                        mycursor.execute(SQL)
                        conn.commit()
                        st.success("Company with company_id '{company_id}' deleted successfully")
                    except Exception as e:
                        conn.rollback()
                        st.write("Error: " + str(e))


    elif table_name=="Jobs":
        with st.form("form 11"):
            Job_id = st.text_input("Enter the Job id of Job you want to delete: ")
            submit = st.form_submit_button("Delete")
            if submit:
                SQL_placeholder="SELECT Job_id FROM Jobs"
                mycursor.execute(SQL_placeholder)
                ids = mycursor.fetchall()
                ids = [i[0] for i in ids]

                # st.write(ids)
                if Job_id not in ids:
                    st.error("Invalid Job id: " + Job_id)
                else:	
                    try:
                        SQL=f"DELETE FROM Jobs WHERE Job_id='{Job_id}'"
                        mycursor.execute(SQL)
                        conn.commit()
                        st.success(f"Job with id={Job_id} deleted successfully")
                    except Exception as e:
                        conn.rollback()
                        st.write("Error: " + str(e))

    elif table_name=="basic_requirements_branch":
        with st.form("form 12"):
            branch = st.text_input("Enter the branch name you want to delete: ")
            submit = st.form_submit_button("Delete")
            if submit:
                SQL_placeholder="SELECT branch FROM basic_requirements_branch"
                mycursor.execute(SQL_placeholder)
                ids = mycursor.fetchall()
                ids = [i[0] for i in ids]

                # st.write(ids)
                if branch not in ids:
                    st.write("Invalid branch name: " + branch)
                else:	
                    try:
                        SQL=f"DELETE FROM basic_requirements_branch WHERE branch='{branch}'"
                        mycursor.execute(SQL)
                        conn.commit()
                        st.success("branch requirement Successfully deleted")
                    except Exception as e:
                        conn.rollback()
                        st.write("Error: " + str(e))

    elif table_name=="requirements":
        with st.form("form 12"):
            Job_id = st.text_input("Enter the Job id whose requirements you want to delete: ")
            submit = st.form_submit_button("Delete")
            if submit:
                SQL_placeholder="SELECT job_id FROM requirements"
                mycursor.execute(SQL_placeholder)
                ids = mycursor.fetchall()
                ids = [i[0] for i in ids]

                if Job_id not in ids:
                    st.error("Invalid Job id: " + Job_id)
                else:	
                    try:
                        SQL=f"DELETE FROM requirements WHERE Job_id='{Job_id}'"
                        mycursor.execute(SQL)
                        conn.commit()
                        st.success(f"Requirements for Job_id {Job_id} deleted successfully")
                    except Exception as e:
                        conn.rollback()
                        st.write("Error: " + str(e))

    elif table_name == "courses":
        with st.form("form 13"):
            course_id = st.text_input("Enter the course id of the course you want to delete: ")
            submit = st.form_submit_button("Delete")
            if submit:
                SQL_key = "SELECT course_id FROM courses"
                mycursor.execute(SQL_key)
                ids = mycursor.fetchall()
                ids = [str(i[0]) for i in ids]  # Convert database values to strings for comparison
                # st.write(ids)
                if course_id not in ids:
                    st.error("Invalid course id: " + course_id)
                else:
                    try:
                        SQL = f"DELETE FROM courses WHERE course_id = {int(course_id)}"  # Convert course_id to int
                        mycursor.execute(SQL)
                        conn.commit()
                        st.write("Course deleted successfully.")
                        st.success(f"Course with course_id={course_id} deleted successfully")
                    except Exception as e:
                        conn.rollback()
                        st.write("Error: " + str(e))

    elif table_name == "job_application":
        with st.form("form 14"):
            Job_id = st.text_input("Enter the Job id of the Job you want to delete: ")
            roll_no = st.text_input("Enter the roll no of the Student you want to delete: " )
            submit = st.form_submit_button("Delete")
            if submit:
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
                
                # st.write(jobid_rollno)
                
                if Job_id not in job_ids:
                    st.error(f"Job ID: {Job_id} does not exist")
                elif int(roll_no) not in roll_nos:
                    st.error(f"Roll No: {roll_no} does not exist")
                elif (Job_id,int(roll_no)) not in jobid_rollno:
                    st.error(f"Job ID: {Job_id} and Roll No: {roll_no} does not exists")
                else:
                    try:
                        SQL = f"DELETE FROM job_application WHERE Job_id = '{Job_id}' and roll_no={int(roll_no)}"  # Convert course_id to int
                        mycursor.execute(SQL)
                        conn.commit()
                        st.success("Job application of  Job ID: Roll No: {roll_no} for Job id:{Job_id} deleted Successfully")
                    except Exception as e:
                        conn.rollback()
                        st.write("Error: " + str(e))

    elif table_name == "courses_completed":
        with st.form("form 15"):
            roll_no = st.text_input("Enter the roll no of the Student you want to delete: " )
            course_id = st.text_input("Enter the course id of the course you want to delete: ")

            submit = st.form_submit_button("Delete")
            if submit:
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

                # st.write(course_id_rollno)

                if int(course_id) not in course_ids:
                    st.error(f"COURSE ID: {course_id} does not exist")
                elif int(roll_no) not in roll_nos:
                    st.error(f"Roll No: {roll_no} does not exist")
                elif (int(course_id),int(roll_no)) not in course_id_rollno:
                    st.error(f"Job ID: {course_id} and Roll No: {roll_no} does not exists")
                else:
                    try:
                        SQL = f"DELETE FROM courses_completed WHERE course_id = {int(course_id)} and roll_no={int(roll_no)}"  # Convert course_id to int
                        mycursor.execute(SQL)
                        conn.commit()
                        st.success(f"Entry for Roll No:{roll_no} and Course ID: {course_id} deeleted Successfully")
                    except Exception as e:
                        conn.rollback()
                        st.write("Error: " + str(e))

def update_data(conn,mycursor):
    available_tables = ["courses_completed", "courses", "job_application", "requirements", "basic_requirements_branch", "Students", "Jobs", "company" ]
    st.title("Table Name Input")

    st.write(f"Available Tables: {available_tables}")

    table_name = st.text_input("Enter the Table Name to Update the data:")

    if table_name not in available_tables:
        st.write("Invalid table name")

    elif table_name == "Students":
        with st.form("form 16"):
            roll_no = st.text_input("Enter the roll no. of the student you want to update: ")
            roll_no = int(roll_no)
            new_student_name = st.text_input("Enter the updated student name: ")
            new_cpi = st.text_input("Enter the updated CPI: ")
            new_cpi = float(new_cpi)
            new_branch = st.text_input("Enter the updated branch: ")
            new_credits = st.text_input("Enter the updated credits: ")
            new_credits=int(new_credits)

            submit = st.form_submit_button("Update")
            if submit:
                SQL_key = "SELECT roll_no FROM Students"
                mycursor.execute(SQL_key)
                roll_nos = mycursor.fetchall()
                roll_nos = [i[0] for i in roll_nos]
                # st.write(roll_nos)
                if roll_no not in roll_nos:
                    st.error("Invalid Roll No: " + roll_no)
                else:
                    try:
                        SQL = f"UPDATE Students SET student_name = '{new_student_name}', cpi = {new_cpi}, branch = '{new_branch}', credits = {new_credits} WHERE roll_no = {roll_no}"
                        mycursor.execute(SQL)
                        conn.commit()
                        st.success("Student record with {roll_no} updated successfully")
                    except Exception as e:
                        conn.rollback()
                        st.write("Error: " + str(e))

    elif table_name == 'company':
        with st.form("form 17"):
            id = st.text_input("Enter Company ID to update: ")
            comp_name = st.text_input("Enter updated Company Name: ")
            name = st.text_input("Enter updated HR Name: ")
            contact = st.text_input("Enter updated HR Contact: ")
            submit = st.form_submit_button("Update")
            if submit:
                SQL_key = "SELECT company_id FROM company"
                mycursor.execute(SQL_key)
                comp_ids = mycursor.fetchall()
                comp_ids = [i[0] for i in comp_ids]

                if id not in comp_ids:
                    st.error(f"Company with ID = {id} does not exist in the database.")
                else:
                    try:
                        SQL = f"UPDATE company SET company_name = '{comp_name}', hr_name = '{name}', hr_contact = '{contact}' WHERE company_id = '{id}'"
                        mycursor.execute(SQL)
                        conn.commit()
                        st.success(f"Company record with ID = {id} updated successfully.")

                    except Exception as e:
                        conn.rollback()
                        st.write("Error: " + str(e))

    elif table_name == 'Jobs':
        with st.form("form 18"):
            comp_id = st.text_input("Enter Company ID: ")
            Job_id = st.text_input("Enter Job ID to update: ")
            openings = st.number_input("Enter updated number of openings: ")
            job_type = st.text_input("Enter updated type of job: ")
            selection_process = st.text_input("Enter updated selection process: ")
            package = st.number_input("Enter updated package: ")
            onsite_input = st.text_input("Enter T for onsite and F for remote: ")
            submit = st.form_submit_button("Update")
            if submit:
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
                    st.error(f"Company with ID = {comp_id} does not exist in the database.")
                elif onsite not in [True, False]:
                    st.error("Invalid entry for the 'onsite' field. Press T for onsite and F for remote.")
                elif Job_id not in Job_ids:
                    st.error(f"Job with ID = {Job_id} does not exist in the database.")
                else:
                    try:
                        SQL = f"UPDATE Jobs SET no_of_openings = {openings}, job_type = '{job_type}', selection_process = '{selection_process}', package = {package}, onsite = {onsite} WHERE company_id = '{comp_id}' AND Job_id = '{Job_id}'"
                        mycursor.execute(SQL)
                        conn.commit()
                        st.success(f"Job record with Company ID = {comp_id} and Job ID = {Job_id} updated successfully.")
                    except Exception as e:
                        conn.rollback()
                        st.write("Error: " + str(e))

    elif table_name == "basic_requirements_branch":
        with st.form("form 19"):
            branch_name = st.text_input("Enter the branch name you want to update: ")
            new_branch_name = st.text_input("Enter the updated branch name: ")
            submit = st.form_submit_button("Update")
            if submit:
                SQL_check = "SELECT branch FROM basic_requirements_branch"
                mycursor.execute(SQL_check)
                branches = mycursor.fetchall()
                branches = [i[0] for i in branches]

                if branch_name not in branches:
                    st.error(f"Branch: {branch_name} does not exist in the database.")
                else:                    
                    try:
                        SQL = f"UPDATE basic_requirements_branch SET branch = '{new_branch_name}' WHERE branch = '{branch_name}'"
                        mycursor.execute(SQL)
                        conn.commit()
                        st.success(f"Branch record '{branch_name}' updated to '{new_branch_name}' successfully.")
                    except Exception as e:
                        conn.rollback()
                        st.write("Error: " + str(e))

    elif table_name == 'requirements':
        with st.form("form 20"):
            Job_id = st.text_input("Enter Job ID for the requirement you want to update: ")
            new_min_cpi = float(st.number_input("Enter the updated minimum CPI required: "))
            new_min_cpi =round(new_min_cpi, 2)
            new_backlogs = int(st.number_input("Enter the updated number of backlogs allowed: "))
            new_job_type = st.text_input("Enter the updated job type: ")
            new_branch = st.text_input("Enter the updated branch: ")
            submit = st.form_submit_button("Update")
            if submit:
                # Check if the Job ID exists
                SQL_Jobid = "SELECT Job_id FROM Jobs"
                mycursor.execute(SQL_Jobid)
                Job_ids = mycursor.fetchall()
                Job_ids = [i[0] for i in Job_ids]

                if Job_id not in Job_ids:
                    st.error(f"Job with ID = {Job_id} does not exist in the DB.")
                else:
                    try:
                        SQL = f"UPDATE requirements SET min_cpi = {new_min_cpi}, backlogs = {new_backlogs}, job_type = '{new_job_type}', branch = '{new_branch}' WHERE Job_id = '{Job_id}'"
                        mycursor.execute(SQL)
                        conn.commit()
                        st.success(f"Requirement for Job ID = {Job_id} updated successfully.")
                        
                    except Exception as e:
                        conn.rollback()
                        st.write("Error: " + str(e))

    elif table_name == 'courses':
         with st.form("form 20"):
            course_id = int(st.number_input("Enter Course ID you want to update: "))
            new_course_name = st.text_input("Enter the updated course name: ")
            submit = st.form_submit_button("Update")
            if submit:            
            # Check if the Course ID exists
                SQL_course_ids = "SELECT course_id FROM courses"
                mycursor.execute(SQL_course_ids)
                course_ids = mycursor.fetchall()
                course_ids = [i[0] for i in course_ids]

                if course_id not in course_ids:
                    st.error(f"Course with ID = {course_id} does not exist in the DB.")
                else:
                    try:
                        SQL = f"UPDATE courses SET course_name = '{new_course_name}' WHERE course_id = {course_id}"
                        mycursor.execute(SQL)
                        conn.commit()
                        st.success(f"Course with ID = {course_id} updated successfully.")
                        
                    except Exception as e:
                        conn.rollback()
                        st.write("Error: " + str(e))

    elif table_name == 'courses_completed':
        with st.form("form 21"):
            roll_no = int(st.number_input("Enter the roll no of the student: "))
            course_id = int(st.number_input("Enter the course id of the completed course: "))
            new_grade = st.text_input("Enter the updated grade for the course: ")
            submit = st.form_submit_button("Update")
            if submit:
                # Check if the combination of roll_no and course_id exists in the 'courses_completed' table
                SQL_check = "SELECT roll_no, course_id FROM courses_completed"
                mycursor.execute(SQL_check)
                roll_no_courseid = mycursor.fetchall()
                roll_no_courseid = [(i[0], i[1]) for i in roll_no_courseid]
                if (roll_no, course_id) not in roll_no_courseid:
                    st.error(f"Entry for Roll No={roll_no}, Course ID: {course_id} does not exist")
                else:
                    try:
                        SQL = f"UPDATE courses_completed SET grade = '{new_grade}' WHERE roll_no = {roll_no} AND course_id = {course_id}"
                        mycursor.execute(SQL)
                        conn.commit()
                        st.success(f"Grade for Roll No={roll_no}, Course ID: {course_id} updated successfully.")
                    except Exception as e:
                        conn.rollback()
                        st.write("Error: " + str(e))

    elif table_name == "job_application":
        with st.form("form 22"):
            Job_id = st.text_input("Enter Job ID: ")
            roll_no = int(st.number_input("Enter Roll No: "))
            new_interview_schedule = st.date_input("Enter the updated interview schedule (YYYY-MM-DD): ")
            new_status = st.text_input("Enter the updated status: ")
            submit = st.form_submit_button("Update")
            if submit:
                SQL_check = "SELECT Job_id, roll_no FROM job_application"
                mycursor.execute(SQL_check)
                jobid_rollno = mycursor.fetchall()
                jobid_rollno = [(i[0], i[1]) for i in jobid_rollno]
                st.write(jobid_rollno)
                if (Job_id, roll_no) not in jobid_rollno:
                    st.error(f"Application for Job ID: {Job_id}, Roll No: {roll_no} does not exist")
                else:
                    try:
                        SQL = f"UPDATE job_application SET interview_schedule = '{new_interview_schedule}', status = '{new_status}' WHERE Job_id = '{Job_id}' AND roll_no = {roll_no}"
                        mycursor.execute(SQL)
                        conn.commit()
                        st.success(f"Application for Job ID: {Job_id}, Roll No: {roll_no} updated successfully.")
                    except Exception as e:
                        conn.rollback()
                        st.write("Error: " + str(e))

def search_data(conn,cursor):
    available_tables = ["courses_completed", "courses", "job_application", "requirements", "basic_requirements_branch", "Students", "Jobs", "company" ]
    # st.write(f"Tables : {available_tables}")
    st.title("Table Name Input")
    # st.write(f"Available Tables: {available_tables}")
    table_name = st.selectbox("Enter the Table Name to Update the data:",options=available_tables,index=None)
    
    if table_name not in available_tables:
        st.write("Invalid table name")
        
    elif table_name=="Students":
        with st.form("form 22"):
            table_columns = ["roll_no","student_name","cpi","branch","credits"]
            columns  = st.multiselect("Select one or more columns:", table_columns)
            condition = st.text_input("Enter the column name and condition: ")
            submit = st.form_submit_button("Search")
            if submit:
                flag=True
                for col in columns:
                    if col not in table_columns:
                        st.write("Invalid column: " + col)
                        flag=False
                if flag==True:
                    
                    SQL_Query = f"SELECT {', '.join(columns)} FROM Students WHERE {condition}"
                    st.write("Generated SQl Query: ")
                    st.code(SQL_Query)
                    try:
                        cursor.execute(SQL_Query)
                        results = cursor.fetchall()
                        if results:
                            for row in results:
                                st.write(row)
                        else:
                            st.info("No results found.")
                    except Exception as e:
                        st.write("Invalid Condition " , e)
                        st.write("If you want , enter custom query below ")
                        custom_query=False
                        custom_query_input = st.text_input("(Press N to try again )Custom Query ")
                        if custom_query_input != "N":
                            try:
                                cursor.execute(custom_query_input) 
                                results = cursor.fetchall()
                                if results:
                                    for row in results:
                                        st.write(row)
                                else:
                                    st.write("No results found.")
                            except Exception as e:
                                st.write("Invalid Custom Query " , e)

    elif table_name == "company":
        with st.form("form 23"):
            # Define the table columns and get user input for columns and condition
            table_columns = ["company_id", "company_name", "hr_name", "hr_contact"]
            columns  = st.multiselect("Select one or more columns:", table_columns)
            # st.write("Table columns: ", table_columns)
            condition = st.text_input("Enter the column name and condition (e.g., company_name='XYZ'): ")
            submit = st.form_submit_button("Search")
            if submit:              
                # Check if the entered columns are valid
                flag = all(col in table_columns for col in columns)
                if not flag:
                    st.error("Invalid column(s) in the input.")           
                # Get user input for the condition
                
                
                # Check if the user wants to enter a custom query
                
                    # Build and execute the SQL query based on selected columns and condition
                SQL_Query = f"SELECT {', '.join(columns)} FROM company WHERE {condition}"
                
                st.write("Generated SQL Query:")
                st.code(SQL_Query)
                
                try:
                    cursor.execute(SQL_Query)
                    results = cursor.fetchall()
                    
                    if results:
                        for row in results:
                            st.write(row)
                            
                    else:
                        st.info("No results found.")
                except Exception as e:
                    custom_query = st.text_input("Enter your custom SQL query: ")
                    SQL_Query = custom_query
                    if len(custom_query) >=5:
                        try:
                            cursor.execute(custom_query)
                            results = cursor.fetchall()
                            if results:
                                for row in results:
                                    st.write(row)                            
                            else:
                                st.info("No results found.")

                        except Exception as e:
                            st.write("Error ",e)
                    else:
                        st.error("Invalid Condition or Query: ", e)
                
    elif table_name == "Jobs":
        with st.form("form 24"):
            # Define the table columns and get user input for columns and condition
            table_columns = ["company_id", "Job_id", "no_of_openings", "job_type", "selection_process", "package", "onsite"]
            # st.write("Table columns: ", table_columns)
            # Get user input for columns to select
            columns_input = st.multiselect("Enter the columns you want in the output separated by commas: ",options=table_columns)
            # Get user input for the condition
            condition = st.text_input("Enter the column name and condition (e.g., no_of_openings>10): ")
            
            # columns = [col.strip() for col in columns_input.split(",")]
            submit = st.form_submit_button("Search")
            if submit:

                # Check if the entered columns are valid
                flag = True
                if not flag:
                    st.info("Invalid column(s) in the input.")
                try:
                    # Build and execute the SQL query based on selected columns and condition
                    SQL_Query = f"SELECT {', '.join(columns_input)} FROM Jobs WHERE {condition}"
                    st.write("Generated SQL query:")
                    st.code(SQL_Query)
                    
                    cursor.execute(SQL_Query)
                    results = cursor.fetchall()
                    
                    if results:
                        for row in results:
                            st.write(row)
                    else:
                        st.info("No results found.")
                except Exception as e:
                    st.write("Query execution failed. Please enter a custom SQL query:",e)
                                           
                    custom_query = st.text_input("Enter your custom SQL query: ")
                    if len(custom_query) >= 5:
                        try:
                            st.write(custom_query)
                            cursor.execute(custom_query)
                            results = cursor.fetchall()
                            if results:
                                for row in results:
                                    st.write(row)
                            else:
                                st.info("No results found.")
                        except Exception as e:
                            st.error("Invalid custom query: ", e)      

    elif table_name == "basic_requirements_branch":
        with st.form("form 25"):
            # Define the table columns and get user input for columns and condition
            table_columns = ["branch"]
                     
            # Get user input for columns to select
            columns_input = st.multiselect("Enter the columns you want in the output separated by commas: ",options=table_columns)
            condition = st.text_input("Enter the condition for the columns")
            submit = st.form_submit_button("Search")
            if submit:
                flag = True
                if not flag:
                    st.error("Invalid column(s) in the input.")
                                
                # Get user input for the condition
                try:
                    # Build and execute the SQL query based on selected columns and condition
                    SQL_Query = f"SELECT {', '.join(columns_input)} FROM basic_requirements_branch WHERE {condition}"
                    st.write("Executing the following query:")
                    st.write(SQL_Query)
                    
                    cursor.execute(SQL_Query)
                    results = cursor.fetchall()
                    
                    if results:
                        for row in results:
                            st.write(row)
                    else:
                        st.write("No results found.")
                except Exception as e:
                    st.write("Query execution failed. Please enter a custom SQL query:")
                    custom_query = st.text_input("Enter your custom SQL query: ")
                    if len(custom_query)>=5:
                        try:
                            cursor.execute(custom_query)
                            results = cursor.fetchall()
                            if results:
                                for row in results:
                                    st.write(row)
                            else:
                                st.write("No results found.")
                        except Exception as e:
                            st.write("Invalid custom query: ", e)      


    elif table_name == "requirements":
        with st.form("form 26"):
            # Define the table columns and get user input for columns and condition
            table_columns = ["Job_id", "min_cpi", "job_type", "backlogs", "branch"]
            # Get user input for columns to select
            columns_input = st.multiselect("Enter the columns you want in the output separated by commas: ",options=table_columns)
            condition = st.text_input("Enter the column name and condition (e.g., Job_id='ABC' AND min_cpi<9.0): ")
            submit = st.form_submit_button("Search")
            if submit:
                flag = True
                if not flag:
                    st.write("Invalid column(s) in the input.")
            
                # Get user input for the condition
                
                try:
                    # Build and execute the SQL query based on selected columns and condition
                    SQL_Query = f"SELECT {', '.join(columns_input)} FROM requirements WHERE {condition}"
                    st.write("Executing the following query:")
                    st.write(SQL_Query)
                    
                    cursor.execute(SQL_Query)
                    results = cursor.fetchall()
                    
                    if results:
                        for row in results:
                            st.write(row)
                    else:
                        st.info("No results found.")
                except Exception as e:
                    conn.rollback()
                    st.write("Query execution failed. Please enter a custom SQL query:")
                    custom_query = st.text_input("Enter your custom SQL query: ")
                    if len(custom_query)>5:
                        try:
                            cursor.execute(custom_query)
                            results = cursor.fetchall()
                            if results:
                                for row in results:
                                    st.write(row)
                            else:
                                st.info("No results found.")
                        except Exception as e:
                            st.write("Invalid custom query: ", e)
            
    elif table_name == "job_application":
        with st.form("form 27"):
            # Define the table columns and get user input for columns and condition
            table_columns = ["Job_id", "roll_no", "interview_schedule", "status"]
            # Get user input for columns to select
            columns_input = st.multiselect("Enter the columns you want in the output separated by commas: ",options=table_columns)
            condition = st.text_input("Enter the column name and condition (e.g., Job_id='ABC' AND status='Pending'): ")
            submit = st.form_submit_button("Search")
            if submit:

            # Check if the entered columns are valid
                flag = True
                if not flag:
                    st.error("Invalid column(s) in the input.")
                
                # Get user input for the condition
                
                try:
                    # Build and execute the SQL query based on selected columns and condition
                    SQL_Query = f"SELECT {', '.join(columns_input)} FROM job_application WHERE {condition}"
                    st.write("Executing the following query:")
                    st.code(SQL_Query)
                    
                    cursor.execute(SQL_Query)
                    results = cursor.fetchall()
                    
                    if results:
                        for row in results:
                            st.write(row)
                    else:
                        st.info("No results found.")

                except Exception as e:
                    conn.rollback()
                    st.write("Query execution failed. Please enter a custom SQL query:")
                    custom_query = st.text_input("Enter your custom SQL query: ")
                    if len(custom_query)>5:
                        try:
                            cursor.execute(custom_query)
                            results = cursor.fetchall()
                            if results:
                                for row in results:
                                    st.write(row)
                            else:
                                st.info("No results found.")
                            
                        except Exception as e:
                            st.write("Invalid custom query: ", e)

    elif table_name == "courses":
        with st.form("form 28"):
            # Define the table columns and get user input for columns and condition
            table_columns = ["course_id", "course_name"]
            
            # Get user input for columns to select
            columns_input = st.multiselect("Enter the columns you want in the output separated by commas: ",options=table_columns)
            condition=st.text_input("Enter the condition for the columns")
            # Check if the entered columns are valid
            submit = st.form_submit_button("Search")
            if submit:
                try:
                    # Build and execute the SQL query based on selected columns and condition
                    SQL_Query = f"SELECT {', '.join(columns_input)} FROM courses WHERE {condition}"
                    st.write("Executing the following query:")
                    st.write(SQL_Query)
                    
                    cursor.execute(SQL_Query)
                    results = cursor.fetchall()
                    
                    if results:
                        for row in results:
                            st.write(row)
                    else:
                        st.write("No results found.")

                except Exception as e:
                    conn.rollback()
                    st.write("Query execution failed. Please enter a custom SQL query:")
                    custom_query = st.text_input("Enter your custom SQL query: ")
                    if len(custom_query) >5:
                        try:
                            cursor.execute(custom_query)
                            results = cursor.fetchall()
                            if results:
                                for row in results:
                                    st.write(row)
                            else:
                                st.write("No results found.")
                        except Exception as e:
                            st.write("Invalid custom query: ", e)

    elif table_name == "courses_completed":
        with st.form("form 29"):
            # Define the table columns and get user input for columns and condition
            table_columns = ["roll_no", "course_id", "grade"]
            
            # Get user input for columns to select
            columns_input = st.multiselect("Enter the columns you want in the output separated by commas: ",options=table_columns)          
            # Get user input for the condition
            condition = st.text_input("Enter the column name and condition (e.g., roll_no=102): ")
            submit = st.form_submit_button("Search")
            if submit:
                try:
                    # Build and execute the SQL query based on selected columns and condition
                    SQL_Query = f"SELECT {', '.join(columns_input)} FROM courses_completed WHERE {condition}"
                    st.write("Executing the following query:")
                    st.code(SQL_Query)
                    
                    cursor.execute(SQL_Query)
                    results = cursor.fetchall()
                    
                    if results:
                        for row in results:
                            st.write(row)
                    else:
                        st.info("No results found.")
                except Exception as e:
                    conn.rollback()
                    st.write("Query execution failed. Please enter a custom SQL query:")
                    custom_query = st.text_input("Enter your custom SQL query: ")
                    try:
                        cursor.execute(custom_query)
                        results = cursor.fetchall()
                        if results:
                            for row in results:
                                st.write(row)
                        else:
                            st.info("No results found.")
                    except Exception as e:
                        st.write("Invalid custom query: ", e)



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

st.write("Connected to Placement Cell Database")
# Main menu
# while True:
#     st.write("Main Menu:")
#     st.write("1. Insert")
#     st.write("2. Delete")
#     st.write("3. Update")
#     st.write("4. Search")
#     st.write("5. Exit")
    
#     flag_st.write = True
#     choice = st.text_input("Select an option: ").strip()

#     if choice == "1":
#         insert_data(conn, cursor)

#     elif choice == "2":
#         delete_data(conn, cursor)

#     elif choice == "3":
#         update_data(conn, cursor)

#     elif choice == "4":
#         search_data(conn, cursor)
#         flag_st.write = False
#     elif choice == "5":
#         st.write("Exiting...")
#         break

#     else:
#         st.write("Invalid option. Please select a valid option.")
    
#     if flag_st.write:
#         SQL="SELECT * FROM Students "
#         cursor.execute(SQL)
#         st.write("\n\nStudents ",cursor.fetchall())

#         SQL="SELECT * FROM Company "
#         cursor.execute(SQL)
#         st.write("\n\nCompany ",cursor.fetchall())

#         SQL="SELECT * FROM Jobs "
#         cursor.execute(SQL)
#         st.write("\n\nJobs ",cursor.fetchall())

#         SQL="SELECT * FROM basic_requirements_branch "
#         cursor.execute(SQL)
#         st.write("\n\nbasic_requirements_branch ",cursor.fetchall())

#         SQL="SELECT * FROM requirements "
#         cursor.execute(SQL)
#         st.write("\n\nRequirements ",cursor.fetchall())

#         SQL="SELECT * FROM courses "
#         cursor.execute(SQL)
#         st.write("\n\ncourses ",cursor.fetchall())

#         SQL="SELECT * FROM courses_completed "
#         cursor.execute(SQL)
#         st.write("\n\ncourses Completed ",cursor.fetchall())

#         SQL="SELECT * FROM job_application"
#         cursor.execute(SQL)
#         st.write("\n\nApplications ",cursor.fetchall())

# Close the database connection
# conn.close()





# Create a text input field
# user_input = st.text_input("Enter some Table :")
# st.write(f"You entered: {user_input}")

if selected_option == "Insert":
    insert_data(conn, cursor)

if selected_option == "Delete":
    delete_data(conn, cursor)

if selected_option == "Update":
    update_data(conn, cursor)


if selected_option == "Search":
    search_data(conn, cursor)