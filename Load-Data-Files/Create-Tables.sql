CREATE TABLE  company (
          company_id VARCHAR(30),
          company_name VARCHAR(30),
          hr_name VARCHAR(50),
          hr_contact VARCHAR(30),           
          PRIMARY KEY (company_id)
);

 CREATE TABLE  Jobs (
          company_id VARCHAR(30),
          Job_id VARCHAR(30) NOT NULL, 
          no_of_openings int,
          job_type VARCHAR(30),
          selection_process VARCHAR(30),
          package int,
          onsite BOOLEAN NOT NULL,
          PRIMARY KEY (Job_id),
          CONSTRAINT C1 FOREIGN KEY (company_id) REFERENCES company(company_id)
);

CREATE TABLE Students(
          roll_no int NOT NULL,
          student_name VARCHAR(255) NOT NULL,
          cpi int NOT NULL,
          branch VARCHAR(255) NOT NULL,
          credits int ,
          PRIMARY KEY (roll_no)
);


CREATE Table basic_requirements_branch(
    branch VARCHAR(30) NOT NULL,
    PRIMARY KEY (branch)
);

CREATE TABLE  requirements (
          Job_id VARCHAR(30) NOT NULL, 
          min_cpi Numeric (5,3),
          job_type VARCHAR(30),
          backlogs int,
          branch VARCHAR(30) NOT NULL,
          PRIMARY KEY (Job_id),
          CONSTRAINT C2 FOREIGN KEY (Job_id) REFERENCES Jobs(Job_id),
          CONSTRAINT C3 FOREIGN KEY (branch) REFERENCES basic_requirements_branch (branch)
);


CREATE Table job_application(
        Job_id VARCHAR(30) NOT NULL,
        roll_no int NOT NULL,
        interview_schedule DATE,
        status VARCHAR(255) ,
        PRIMARY KEY(Job_id,roll_no),
        CONSTRAINT C5 FOREIGN KEY (Job_id) REFERENCES Jobs(Job_id),
        CONSTRAINT C6 FOREIGN KEY (roll_no) REFERENCES Students(roll_no)
);


CREATE Table courses (       
        course_id int NOT NULL,
        course_name varchar(255) ,
        PRIMARY KEY(course_id)
);


CREATE TABLE courses_completed(
        roll_no int NOT NULL,
        course_id int NOT NULL,
        grade VARCHAR(30),
        PRIMARY KEY(roll_no,course_id),
        CONSTRAINT C7 FOREIGN KEY (course_id) REFERENCES courses,
        CONSTRAINT C8 FOREIGN KEY (roll_no) REFERENCES    Students
);