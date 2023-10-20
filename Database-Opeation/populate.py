import csv
import psycopg2
from variables import *

conn =  psycopg2.connect(database=database_name,
                         host=host_name,
                         user=user_name,
                         password=password_val,
                         port=port_name)


mycursor=conn.cursor()

try:
    with open("Company.csv","r") as f:
        csv_reader = csv.reader(f)
        for record in csv_reader:
            line = "INSERT INTO company VALUES(%s, %s, %s )"
            values = (record[0],record[1],record[2])
            mycursor.execute(line,values)

    with open("Jobs.csv","r") as f:
        csv_reader = csv.reader(f)
        for record in csv_reader:
            line = "INSERT INTO Jobs (%s, %s, %s, %s, %s, %s, %s)"
            values = (record[0],record[1],int(record[2]),record[3],record[4],int(record[5]),bool(record[6]))
            mycursor.execute(line,values)


    with open("Student.csv","r") as f:
        csv_reader = csv.reader(f)
        for record in csv_reader:
            line = "INSERT INTO Students VALUES(%s, %s, %s, %s, %s)"
            values = (int(record[0]),record[1],float(record[2]),record[3],int(record[4]))
            mycursor.execute(line,values)


    with open("basic_requirements.csv","r") as f:
        csv_reader = csv.reader(f)
        for record in csv_reader:
            line = "INSERT INTO basic_requirements_branch VALUES (%s)"
            values = (record[0])
            mycursor.execute(line,values)


    with open("requirements.csv","r") as f:
        csv_reader = csv.reader(f)
        for record in csv_reader:
            line = "INSERT INTO requirements  VALUES (%s, %s, %s, %s, %s)"
            onsite = bool(record[3]) if record[3].lower() == 'true' else False
            values = (record[0], float(record[1]), record[2], onsite, record[4])
            # values = (record[0],float(record[1]),record[2] , int(record[3]) , record[4])
            mycursor.execute(line,values)


    with open("job_application.csv","r") as f:
        csv_reader = csv.reader(f)
        for record in csv_reader:
            line = "INSERT INTO job_application  VALUES (%s, %s, %s, %s)"
            values = (record[0],int(record[1]),record[2] , record[3])
            mycursor.execute(line,values)


    with open("courses.csv","r") as f:
        csv_reader = csv.reader(f)
        for record in csv_reader:
            line = "INSERT INTO courses VALUES (%s, %s)"
            values = (int(record[0]),record[1])
            mycursor.execute(line,values)

    with open("courses_taken.csv","r") as f:
        csv_reader = csv.reader(f)
        for record in csv_reader:
            line = "INSERT INTO courses_taken  VALUES (%s, %s, %s)"
            values = (int(record[0]),int(record[1]),record[2])
            mycursor.execute(line,values)


except psycopg2.Error as e:
    print("ERROR While adding data to the file: ",e)

mycursor.close()
conn.close()