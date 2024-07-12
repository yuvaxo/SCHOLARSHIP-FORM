create table location(
                        
                        s_code NUMBER(12) PRIMARY KEY,
                        r_u CHAR(1),
                        addr1 VARCHAR(100),
                        addr2 VARCHAR(200),
                        p_name VARCHAR(100),
                        d_name VARCHAR(100),
                        states VARCHAR(50),
                        CONSTRAINT fk_student FOREIGN KEY(s_code) REFERENCES student(s_code)
                    );

drop table location;
COMMIT;
desc location;


CREATE TABLE college(
                    s_code NUMBER(12) PRIMARY KEY,
                    c_code NUMBER(4),
                    c_name VARCHAR(200),
                    l_name NUMBER(12),
                    CONSTRAINT fk_cstudent FOREIGN KEY(s_code) REFERENCES student(s_code)
                );


ALTER TABLE student MODIFY is_superuser NUMBER(1) Default 0;
ALTER TABLE student MODIFY is_admin NUMBER(1) Default 0;
ALTER TABLE student MODIFY password VARCHAR(100);

drop TABLE college;
DESC college;

CREATE TABLE student(s_code NUMBER(10) PRIMARY KEY,
                    s_name VARCHAR(200),
                    sex char(1),
                    dob DATE,
                    edu_year NUMBER(4),
                    f_m_name VARCHAR(200),
                    community CHAR(10),
                    p_income NUMBER(8),
                    community_attach BLOB,
                    income_attach BLOB,
                    addr1 VARCHAR(200),
                    addr2 VARCHAR(200),
                    perm_addr VARCHAR(200),
                    l_code NUMBER(12),
                    c_code NUMBER(4),
                    CONSTRAINT fk_location1 FOREIGN KEY(l_code) REFERENCES location(l_code),
                    CONSTRAINT fk_college FOREIGN KEY(c_code) REFERENCES college(c_code)
                    );
ALTER TABLE student add is_superuser NUMBER(1, 0);
ALTER TABLE student ADD last_login TIMESTAMP;
ALTER TABLE student RENAME COLUMN passwd to password;

desc student;



CREATE TABLE student_transaction(s_code NUMBER(10) PRIMARY KEY,
                                 year NUMBER(4),
                                 amount NUMBER(8),
                                 l_code NUMBER(12),
                                 c_code NUMBER(4),
                                 CONSTRAINT fk_location2 FOREIGN KEY(l_code) REFERENCES location(l_code),
                                 CONSTRAINT fk_college1 FOREIGN KEY(c_code) REFERENCES college(c_code)
                    );

CREATE TABLE bank(
                    
                    acc_no NUMBER(12) PRIMARY KEY,
                    s_code NUMBER(12),
                    ifsc VARCHAR(11),
                    b_name VARCHAR(200),
                    b_loc VARCHAR(100),
                    b_addr VARCHAR(200),
                    
                    CONSTRAINT fk_bstudent FOREIGN KEY(s_code) REFERENCES student(s_code)

                );





desc bank;
COMMIT;