#Import the needed modules
import random
import sqlite3
import re


num = "1234567890"
#===========================================================================================================================
def check(Email): # This is to check the email format
    global email
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, Email)):
        email=Email
        return True
    else:
        print("Check your mailid")
#==========================================================================================================================
def verifi(Email): # This is to check whether the mail id is already in use or not
    conn = sqlite3.connect("students.db")  # connected to student Db
    curs = conn.cursor()
    global email
    curs.execute("SELECT * FROM student") # details are fetched from the DB
    items = curs.fetchall()
    for item in items:
        if Email in item[1]:  # This part will check or verify the email id
            print("This mail id is already in use ")
            break
    else:
        #print("verified")
        return True
def display_all():
    conn = sqlite3.connect("students.db")  # connected to student Db
    curs = conn.cursor()
    curs.execute("SELECT * FROM student")
    items=curs.fetchall()
    for item in items:
        print(item)

def verification(name,email,regno):
    conn = sqlite3.connect("students.db")  # connected to student Db
    curs = conn.cursor()
    curs.execute("SELECT * FROM student")
    items=curs.fetchall()
    for item in items:
        if email == item[1]:
            if name==item[0]:
                if regno == item[2]:
                    print("verified")
                    return True
                else:
                    print("Please Check your reg no")
            else:
                print("No username found")
#=================================================================**Main**==================================================
def register():
    global Name
    global Email
    conn = sqlite3.connect("students.db")  # connected to student Db
    curs = conn.cursor()
    curs.execute(""" CREATE TABLE IF NOT EXISTS student(
       name text,
       email text,
       regno integer) 
       """)# Student table is created
    Name=input("Enter Your Name: ")
    Email=input("Enter your mailid: ")
    submit=input("Submit : y or no ")

    if submit in ["YES","Yes","yes","y","Y"]:
        if check(Email)==True:
           if verifi(Email) ==True:
                reg=''.join(random.choice(num) for i in range(5))
                print("Registration Number: "+reg)
                print("Successfully Submitted")
    elif submit in ["NO","No","no","N","n"]:
        print("Please submit it to attend the quiz")
    else:
        print("Invalid Option \nPlease check it")
    try:
        list_std = [Name, email,reg]
        curs.execute("INSERT INTO student(name,email,regno) VALUES(?,?,?)", list_std)
    except NameError:
        print("Please enter a proper email id")

    conn.commit()
    conn.close()


