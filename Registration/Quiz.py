import sqlite3
import Registration as r
#=======================================================================================================================
def quiz_Questions(name1,email1,reg1): ##Question and answer
    conn = sqlite3.connect("Quiz_Student.db")
    curs = conn.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS qanda(name text, email text,regno integer,question text,answer text,score integer)")
    set_ques = {
        "1) What is the colour of apple?\n1.Red\n2.White\n3.Yellow\nAns:\t": ["1", "Red", "red", "1.Red", "1 Red", "1 red",
                                                                           "1red", "1Red"],
        "2)What is the colour of Sky?\n1.Red\n2.White\n3.Yellow\nAns:\t": ["2", "White", "white", "2.White", "2 White",
                                                                         "white", "2White", "2white"],
        "3)Which of the following is leap year?\n1.2001\n2.2002\n3.2020\nAns:\t": ["3.2020", "3", "2020", "3 2020",
                                                                               "32020"],
        "4)What is the colour of Grapes?\n1.white\n2.Purple\n3.Yellow\nAns:\t": ["2", "Purple", "purple", "2.Purple",
                                                                               "2 Purple", "2 purple", "2Purple",
                                                                              "2purple"]}
    sum=0
    for i, k in set_ques.items():
        ans = input(i)
        if ans in k:
            sum+=1
            print("ok")
        else:
            print("Wrong Answer")
        list1=[name1,email1,reg1,i,ans,sum]
        curs.execute("INSERT INTO qanda(name,email,regno,question,answer,score) VALUES(?,?,?,?,?,?)",list1)
    print(f"Mark Scored:{sum}")

    conn.commit()
    conn.close()
def Result_of_student():# If needed it can be called
    conn = sqlite3.connect("Quiz_Student.db")
    curs = conn.cursor()
    curs.execute("SELECT * FROM qanda")
    x_items=curs.fetchall()
    for i in x_items:
        print(i)
#=======================================================================================================================
if __name__=="__main__":
    choice=input("what would you like to do?\n1.Register\n2.Quiz\t")
    if choice=="1":
        r.register()
    elif choice=="2":
        name=input("Enter your name: ")
        Emailid = input("Enter your MailId: ")
        if r.check(Emailid) == True:
            reg = int(input("Enter your Registration Number:"))
            if r.verification(name,Emailid, regno=reg) == True:
                print("ok")
                quiz_Questions(name,Emailid,reg)
