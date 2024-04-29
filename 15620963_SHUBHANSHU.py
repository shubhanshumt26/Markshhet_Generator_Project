p_w='smt@2023'
#_________________________________________________________________________________________
#_________________________________________________________________________________________
#To create Student Database in MySQL
def database():
    import mysql.connector as mysql
    db=mysql.connect(host="localhost",user='root',passwd=p_w)
    cursor=db.cursor()
    cursor.execute('''CREATE DATABASE IF NOT EXISTS Student''')
    db.close()
#_________________________________________________________________________________________
#_________________________________________________________________________________________
#To create Student_Details table in mysql
def table():
    import mysql.connector as mysql
    db=mysql.connect(host="localhost",user='root',passwd=p_w,database='Student')
    cursor=db.cursor()  
    cursor.execute('''CREATE TABLE IF NOT EXISTS Student_Details (Name varchar(30) not null,Roll_Number char(7)
    primary key,Father_Name varchar(30) not null,Mother_Name varchar(30) not null,School varchar(60) not null)''')
    db.close()
#_________________________________________________________________________________________
#_________________________________________________________________________________________
#To create Marks table in mysql
def marks_science():
    import mysql.connector as mysql
    db=mysql.connect(host="localhost",user='root',passwd=p_w,database='Student')
    cursor=db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Marks (Roll_Number char(7) primary key,Physics float(4),
    Chemistry float(4),Mathematics float(4),C_S float(4),English float(4),Hindi float(4),Biology float(4),I_P
    float(4),Physics_pr float(4),Chemistry_pr float(4),Mathematics_pr float(4),C_S_pr float(4),English_pr float(4),
    Hindi_pr float(4),Biology_pr float(4),I_P_pr float(4))''')
    db.close()
#_________________________________________________________________________________________
#_________________________________________________________________________________________
#To create Grade table in mysql
def grade():
    import mysql.connector as mysql
    db=mysql.connect(host="localhost",user='root',passwd=p_w,database='Student')
    cursor=db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Grade  (Roll_Number char(7) primary key,Work_Experience varchar(3)
    not null,Physical_Health varchar(3) not null,General_Studies varchar(3) not null)''')
    db.close()
#_________________________________________________________________________________________
#_________________________________________________________________________________________
#To input Student Details:Name,roll_no,mother'sname,father'name,school
def Student_Details():
    import mysql.connector as mysql
    db=mysql.connect(host="localhost",user='root',passwd=p_w,database='Student')
    cursor=db.cursor()
    print("\t\t ________________________")
    print("\t\t|                        | ")
    print("\t\t| ENTER STUDENT DETAILS  |")
    print("\t\t|________________________|")
    print('All Details Are Mandatory.Please fill all the details properly.')
    name=str(input("Enter the Student's Name:"))
    roll=str(input("Enter the Student's Board Roll Number:"))
    fname=input("Enter the Student Father's Name:")
    mname=input("Enter the Student Mother's Name:")
    school='34026-KENDRIYA VIDYALAYA S C TARAPORE ROAD PUNE MR'
    insert='''INSERT INTO Student_Details(Name,Roll_Number,Father_Name,Mother_Name,School) values(%s,%s,%s,%s,%s)'''
    records=[name,roll,fname,mname,school]
    cursor.execute(insert,records)
    db.commit()
    print("Data Added Successfully.")
    db.close()
#_________________________________________________________________________________________
#_________________________________________________________________________________________
#To Enter the Student Marks in Different Subjects.
def Subject():
    while True:
        import mysql.connector as mysql
        db=mysql.connect(host="localhost",user='root',passwd=p_w,database='Student')
        cursor=db.cursor()
        print("\t\t ________________________")
        print("\t\t|                        | ")
        print("\t\t|  ENTER STUDENT MARKS   |")
        print("\t\t|________________________|")
        print("Marks can be entered for 1 time only on your unique board Roll Number.")
        print("Please Enter the decimal number upto 2 digit only.")
        print("Please Enter the Marks very carefully   :)")
        print("1:Physics,Chemistry,Mathematics,Computer Science,English")
        print("2:Physics,Chemistry,Mathematics,Hindi,English")
        print("3:Physics,Chemistry,Mathematics,Biology,English")
        print("4:Physics,Chemistry,Biology,Hindi,English")
        print("5:Physics,Chemistry,Biology,I.P.,English")
        print("If the student was Absent in that test then type his marks as 0(Zero)")
        choice=int(input("Enter the number for your stream:"))
        if choice==1:
                print("Please provide your Board Roll Number.")
                roll=str(input("Enter your board Roll Number:"))
                print("Total Marks: Physics,Chemistry,Cs=70 and English,Mathematics=80")
                phy=float(input("Enter the Marks in Physics:"))
                chem=float(input("Enter the Marks in Chemistry:"))
                maths=float(input("Enter the Marks in Mathematics:"))
                cs=float(input("Enter the Marks in Computer Science:"))
                eng=float(input("Enter the Marks in English:"))
                print("Practical Marks: Physics,Chemistry,CS=30 and Mathematics,English=20")
                phy_pr=float(input("Enter the Marks in Physics Practcal:"))
                chem_pr=float(input("Enter the Marks in Chemistry Practcal:"))
                maths_pr=float(input("Enter the Marks in Mathematics Practcal:"))
                cs_pr=float(input("Enter the Marks in Computer Science Practcal:"))
                eng_pr=float(input("Enter the Marks in English Practcal:"))
                insert='''INSERT INTO Marks(Roll_Number,Physics,Chemistry,Mathematics,C_S,English,Physics_pr,
                Chemistry_pr,Mathematics_pr,C_S_pr,English_pr) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
                records=[roll,phy,chem,maths,cs,eng,phy_pr,chem_pr,maths_pr,cs_pr,eng_pr]
                cursor.execute(insert,records)
                db.commit()
                print("Please Enter the Grades in the below subjects.")
                print("Grades allowed are A1,A2,B1,B2,C1 & C2.")
                we=input("Enter the Grade in Work Experience:")
                ph=input("Enter the Grade in Physical & Health Education:")
                gs=input("Enter the Grade in General Studies:")
                insert='''INSERT INTO Grade(Work_Experience,Physical_Health,
                General_Studies,Roll_Number) values(%s,%s,%s,%s)'''
                records=[we,ph,gs,roll]
                cursor.execute(insert,records)
                db.commit()
                db.close()
                print("Marks Added Successfully.")
            
        elif choice==2:
                print("Please provide your Board Roll Number.")
                roll=str(input("Enter your board Roll Number:"))
                print("Total Marks: Physics,Chemistry=70 and Mathematics,English,Hindi=80")
                phy=float(input("Enter the Marks in Physics:"))
                chem=float(input("Enter the Marks in Chemistry:"))
                maths=float(input("Enter the Marks in Mathematics:"))
                hindi=float(input("Enter the Marks in Hindi:"))
                eng=float(input("Enter the Marks in English:"))
                print("Practical Marks: Physics,Chemistry=30 and Mathematics,English,Hindi=20")
                phy_pr=float(input("Enter the Marks in Physics Practcal:"))
                chem_pr=float(input("Enter the Marks in Chemistry Practcal:"))
                maths_pr=float(input("Enter the Marks in Mathematics Practcal:"))
                hindi_pr=float(input("Enter the Marks in Hindi Practcal:"))
                eng_pr=float(input("Enter the Marks in English Practcal:"))
                insert='''INSERT INTO Marks(Roll_Number,Physics,Chemistry,Mathematics,Hindi,English,Physics_pr,
                Chemistry_pr,Mathematics_pr,Hindi_pr,English_pr) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
                records=[roll,phy,chem,maths,hindi,eng,phy_pr,chem_pr,maths_pr,hindi_pr,eng_pr]
                cursor.execute(insert,records)
                db.commit()
                print("Please Enter the Grades in the below subjects.")
                print("Grades allowed are A1,A2,B1,B2,C1 & C2.")
                we=input("Enter the Grade in Work Experience:")
                ph=input("Enter the Grade in Physical & Health Education:")
                gs=input("Enter the Grade in General Studies:")
                insert='''INSERT INTO Grade(Work_Experience,Physical_Health,
                General_Studies,Roll_Number) values(%s,%s,%s,%s)'''
                records=[we,ph,gs,roll]
                cursor.execute(insert,records)
                db.commit()
                db.close()
                print("Marks Added Successfully.")

        elif choice==3:
                print("Please provide your Board Roll Number.")
                roll=str(input("Enter your board Roll Number:"))
                print("Total Marks: Physics,Chemistry,Biology=70 and Mathematics,English=80")
                phy=float(input("Enter the Marks in Physics:"))
                chem=float(input("Enter the Marks in Chemistry:"))
                maths=float(input("Enter the Marks in Mathematics:"))
                bio=float(input("Enter the Marks in Biology:"))
                eng=float(input("Enter the Marks in English:"))
                print("Practical Marks: Physics,Chemistry,Biology=30 and Mathematics,English=20")
                phy_pr=float(input("Enter the Marks in Physics Practcal:"))
                chem_pr=float(input("Enter the Marks in Chemistry Practcal:"))
                maths_pr=float(input("Enter the Marks in Mathematics Practcal:"))
                bio_pr=float(input("Enter the Marks in Biology Practcal:"))
                eng_pr=float(input("Enter the Marks in English Practcal:"))
                insert='''INSERT INTO Marks(Roll_Number,Physics,Chemistry,Mathematics,Biology,English,Physics_pr,
                Chemistry_pr,Mathematics_pr,Biology_pr,English_pr) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
                records=[roll,phy,chem,maths,bio,eng,phy_pr,chem_pr,maths_pr,bio_pr,eng_pr]
                cursor.execute(insert,records)
                db.commit()
                print("Please Enter the Grades in the below subjects.")
                print("Grades allowed are A1,A2,B1,B2,C1 & C2.")
                we=input("Enter the Grade in Work Experience:")
                ph=input("Enter the Grade in Physical & Health Education:")
                gs=input("Enter the Grade in General Studies:")
                insert='''INSERT INTO Grade(Work_Experience,Physical_Health,
                General_Studies,Roll_Number) values(%s,%s,%s,%s)'''
                records=[we,ph,gs,roll]
                cursor.execute(insert,records)
                db.commit()
                db.close()
                print("Marks Added Successfully.")
            
        elif choice==4:
                print("Please provide your Board Roll Number.")
                roll=str(input("Enter your board Roll Number:"))
                print("Total Marks: Physics,Chemistry,Biology=70 and English,Hindi=80")
                phy=float(input("Enter the Marks in Physics:"))
                chem=float(input("Enter the Marks in Chemistry:"))
                bio=float(input("Enter the Marks in Biology:"))
                hindi=float(input("Enter the Marks in Hindi:"))
                eng=float(input("Enter the Marks in English:"))
                print("Practical Marks: Physics,Chemistry,Biology=30 and Hindi,English=20")
                phy_pr=float(input("Enter the Marks in Physics Practcal:"))
                chem_pr=float(input("Enter the Marks in Chemistry Practcal:"))
                bio_pr=float(input("Enter the Marks in Biology Practcal:"))
                hindi_pr=float(input("Enter the Marks in Hindi Practcal:"))
                eng_pr=float(input("Enter the Marks in English Practcal:"))
                insert='''INSERT INTO Marks(Roll_Number,Physics,Chemistry,Biology,Hindi,English,Physics_pr,
                Chemistry_pr,Biology_pr,Hindi_pr,English_pr) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
                records=[roll,phy,chem,bio,hindi,eng,phy_pr,chem_pr,bio_pr,hindi_pr,eng_pr]
                cursor.execute(insert,records)
                db.commit()
                print("Please Enter the Grades in the below subjects.")
                print("Grades allowed are A1,A2,B1,B2,C1 & C2.")
                we=input("Enter the Grade in Work Experience:")
                ph=input("Enter the Grade in Physical & Health Education:")
                gs=input("Enter the Grade in General Studies:")
                insert='''INSERT INTO Grade(Work_Experience,Physical_Health,
                General_Studies,Roll_Number) values(%s,%s,%s,%s)'''
                records=[we,ph,gs,roll]
                cursor.execute(insert,records)
                db.commit()
                db.close()
                print("Marks Added Successfully.")
            
        elif choice==5:
                print("Please provide your Board Roll Number.")
                roll=str(input("Enter your board Roll Number:"))
                print("Total Marks: Physics,Chemistry,I.P.,Biology=70 and English=80")
                phy=float(input("Enter the Marks in Physics:"))
                chem=float(input("Enter the Marks in Chemistry:"))
                bio=float(input("Enter the Marks in Biology:"))
                ip=float(input("Enter the Marks in Information Practices(I.P):"))
                eng=float(input("Enter the Marks in English:"))
                print("Practical Marks: Physics,Chemistry,Biology,I.P.=30 and English=20")
                phy_pr=float(input("Enter the Marks in Physics Practcal:"))
                chem_pr=float(input("Enter the Marks in Chemistry Practcal:"))
                ip_pr=float(input("Enter the Marks in Information Practices(I.P) Practcal:"))
                bio_pr=float(input("Enter the Marks in Biology Practcal:"))
                eng_pr=float(input("Enter the Marks in English Practcal:"))
                insert='''INSERT INTO Marks(Roll_Number,Physics,Chemistry,Biology,I_P,English,Physics_pr,
                Chemistry_pr,Biology_pr,I_P_pr,English_pr) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
                records=[roll,phy,chem,bio,ip,eng,phy_pr,chem_pr,bio_pr,ip_pr,eng_pr]
                cursor.execute(insert,records)
                db.commit()
                print("Please Enter the Grades in the below subjects.")
                print("Grades allowed are A1,A2,B1,B2,C1 & C2.")
                we=input("Enter the Grade in Work Experience:")
                ph=input("Enter the Grade in Physical & Health Education:")
                gs=input("Enter the Grade in General Studies:")
                insert='''INSERT INTO Grade(Work_Experience,Physical_Health,
                General_Studies,Roll_Number) values(%s,%s,%s,%s)'''
                records=[we,ph,gs,roll]
                cursor.execute(insert,records)
                db.commit()
                db.close()
                print("Marks Added Successfully.")
            
        else:
               print("Wrong choice.")
               print("Try Again!!")
               c=input("If you want to Enter the marks again then press 'Y' or 'y' else press any other button to exit:")
               if c=='Y' or c=='y':
                    continue
               else:
                    break
        db.close()
        c=input("If you want to Enter more marks then press 'Y' or 'y' else press any other button to exit:")
        if c=='Y' or c=='y':
            continue
        else:
            break
#_________________________________________________________________________________________
#_________________________________________________________________________________________
#To update the theory marks of a student.
def Update():
    print("\t\t ________________________")
    print("\t\t|                        | ")
    print("\t\t|     MARKS UPDATER      |")
    print("\t\t|________________________|")
    print("Welocme to Update Menu.")
    print("You can update marks of Theory Subjects.")
    import mysql.connector as mysql
    db=mysql.connect(host="localhost",user='root',passwd=p_w,database='Student')
    cursor=db.cursor()
    roll=str(input("Enter your Roll Number:"))
    print("1:Physics,Chemistry,Mathematics,Computer Science,English")
    print("2:Physics,Chemistry,Mathematics,Hindi,English")
    print("3:Physics,Chemistry,Mathematics,Biology,English")
    print("4:Physics,Chemistry,Biology,Hindi,English")
    print("5:Physics,Chemistry,Biology,I.P.,English")
    choice=int(input("Enter the number for your stream:"))
    if choice==1:
       while True: 
           print("1.Change in Physics.")
           print("2.Change in Chemistry.")
           print("3.Change in Maths.")
           print("4.Change in Computer Science.")
           print("5.Change in English.")
           ch=int(input("Enter your choice:"))
           if ch==1:
               p=str(input("Enter the Updated marks in Physics:"))
               cursor.execute("UPDATE Marks SET Physics='"+p+"'WHERE Roll_Number='"+roll+"'")
               db.commit()
               print("Marks Updated Successfully.")
           elif ch==2:
               c=str(input("Enter the Updated marks in Chemistry:"))
               cursor.execute("UPDATE Marks SET Chemistry='"+c+"'WHERE Roll_Number='"+roll+"'")
               db.commit()
               print("Marks Updated Successfully.")
           elif ch==3:
                m=str(input("Enter the Updated marks in Mathematics:"))
                cursor.execute("UPDATE Marks SET Mathematics='"+m+"'WHERE Roll_Number='"+roll+"'")
                db.commit()
                print("Marks Updated Successfully.")
           elif ch==4:
                cs=str(input("Enter the Updated marks in Computer Science:"))
                cursor.execute("UPDATE Marks SET C_S='"+cs+"'WHERE Roll_Number='"+roll+"'")
                db.commit()
                print("Marks Updated Successfully.")
           elif ch==5:
                e=str(input("Enter the Updated marks in English:"))
                cursor.execute("UPDATE Marks SET English='"+e+"'WHERE Roll_Number='"+roll+"'")
                db.commit()
                print("Marks Updated Successfully.")
           else:
                    print("Wrong Choice.")
                    print("Try Again.")
                    ch=input("Enter Y if want to continue else press any other key.")
                    if ch=='Y' or ch=='y':
                           continue
                    else:
                           break
           c=input("Want to Update More Marks Press Y else press any other key:")
           if c=='y' or c=='Y':
               continue
           else:
               break
    if choice==2:
       while True: 
           print("1.Change in Physics.")
           print("2.Change in Chemistry.")
           print("3.Change in Maths.")
           print("4.Change in Hindi.")
           print("5.Change in English.")
           ch=int(input("Enter your choice:"))
           if ch==1:
               p=str(input("Enter the Updated marks in Physics:"))
               cursor.execute("UPDATE Marks SET Physics='"+p+"'WHERE Roll_Number='"+roll+"'")
               db.commit()
               print("Marks Updated Successfully.")
           elif ch==2:
               c=str(input("Enter the Updated marks in Chemistry:"))
               cursor.execute("UPDATE Marks SET Chemistry='"+c+"'WHERE Roll_Number='"+roll+"'")
               db.commit()
               print("Marks Updated Successfully.")
           elif ch==3:
                m=str(input("Enter the Updated marks in Mathematics:"))
                cursor.execute("UPDATE Marks SET Mathematics='"+m+"'WHERE Roll_Number='"+roll+"'")
                db.commit()
                print("Marks Updated Successfully.")
           elif ch==4:
                h=str(input("Enter the Updated marks in Hindi:"))
                cursor.execute("UPDATE Marks SET Hindi='"+h+"'WHERE Roll_Number='"+roll+"'")
                db.commit()
                print("Marks Updated Successfully.")
           elif ch==5:
                e=str(input("Enter the Updated marks in English:"))
                cursor.execute("UPDATE Marks SET English='"+e+"'WHERE Roll_Number='"+roll+"'")
                db.commit()
                print("Marks Updated Successfully.")
           else:
                    print("Wrong Choice.")
                    print("Try Again.")
                    ch=input("Enter Y if want to continue else press any other key.")
                    if ch=='Y' or ch=='y':
                           continue
                    else:
                           break
           c=input("Want to Update More Marks Press Y else press any other key:")
           if c=='y' or c=='Y':
               continue
           else:
                break
    if choice==3:
       while True: 
           print("1.Change in Physics.")
           print("2.Change in Chemistry.")
           print("3.Change in Maths.")
           print("4.Change in Biology.")
           print("5.Change in English.")
           ch=int(input("Enter your choice:"))
           if ch==1:
               p=str(input("Enter the Updated marks in Physics:"))
               cursor.execute("UPDATE Marks SET Physics='"+p+"'WHERE Roll_Number='"+roll+"'")
               db.commit()
               print("Marks Updated Successfully.")
           elif ch==2:
               c=str(input("Enter the Updated marks in Chemistry:"))
               cursor.execute("UPDATE Marks SET Chemistry='"+c+"'WHERE Roll_Number='"+roll+"'")
               db.commit()
               print("Marks Updated Successfully.")
           elif ch==3:
                m=str(input("Enter the Updated marks in Mathematics:"))
                cursor.execute("UPDATE Marks SET Mathematics='"+m+"'WHERE Roll_Number='"+roll+"'")
                db.commit()
                print("Marks Updated Successfully.")
           elif ch==4:
                b=str(input("Enter the Updated marks in Biology:"))
                cursor.execute("UPDATE Marks SET Biology='"+b+"'WHERE Roll_Number='"+roll+"'")
                db.commit()
                print("Marks Updated Successfully.")
           elif ch==5:
                e=str(input("Enter the Updated marks in English:"))
                cursor.execute("UPDATE Marks SET English='"+e+"'WHERE Roll_Number='"+roll+"'")
                db.commit()
                print("Marks Updated Successfully.")
           else:
                    print("Wrong Choice.")
                    print("Try Again.")
                    ch=input("Enter Y if want to continue else press any other key.")
                    if ch=='Y' or ch=='y':
                           continue
                    else:
                           break
           c=input("Want to Update More Marks Press Y else press any other key:")
           if c=='y' or c=='Y':
               continue
           else:
                break
    if choice==4:
       while True: 
           print("1.Change in Physics.")
           print("2.Change in Chemistry.")
           print("3.Change in Hindi.")
           print("4.Change in Biology.")
           print("5.Change in English.")
           ch=int(input("Enter your choice:"))
           if ch==1:
               p=str(input("Enter the Updated marks in Physics:"))
               cursor.execute("UPDATE Marks SET Physics='"+p+"'WHERE Roll_Number='"+roll+"'")
               db.commit()
               print("Marks Updated Successfully.")
           elif ch==2:
               c=str(input("Enter the Updated marks in Chemistry:"))
               cursor.execute("UPDATE Marks SET Chemistry='"+c+"'WHERE Roll_Number='"+roll+"'")
               db.commit()
               print("Marks Updated Successfully.")
           elif ch==3:
                h=str(input("Enter the Updated marks in Hindi:"))
                cursor.execute("UPDATE Marks SET Hindi='"+h+"'WHERE Roll_Number='"+roll+"'")
                db.commit()
                print("Marks Updated Successfully.")
           elif ch==4:
                b=str(input("Enter the Updated marks in Biology:"))
                cursor.execute("UPDATE Marks SET Hindi='"+b+"'WHERE Roll_Number='"+roll+"'")
                db.commit()
                print("Marks Updated Successfully.")
           elif ch==5:
                e=str(input("Enter the Updated marks in English:"))
                cursor.execute("UPDATE Marks SET English='"+e+"'WHERE Roll_Number='"+roll+"'")
                db.commit()
                print("Marks Updated Successfully.")
           else:
                    print("Wrong Choice.")
                    print("Try Again.")
                    ch=input("Enter Y if want to continue else press any other key.")
                    if ch=='Y' or ch=='y':
                           continue
                    else:
                           break
           c=input("Want to Update More Marks Press Y else press any other key:")
           if c=='y' or c=='Y':
               continue
           else:
                break
    if choice==5:
       while True: 
           print("1.Change in Physics.")
           print("2.Change in Chemistry.")
           print("3.Change in Information Practices.")
           print("4.Change in Biology.")
           print("5.Change in English.")
           ch=int(input("Enter your choice:"))
           if ch==1:
               p=str(input("Enter the Updated marks in Physics:"))
               cursor.execute("UPDATE Marks SET Physics='"+p+"'WHERE Roll_Number='"+roll+"'")
               db.commit()
               print("Marks Updated Successfully.")
           elif ch==2:
               c=str(input("Enter the Updated marks in Chemistry:"))
               cursor.execute("UPDATE Marks SET Chemistry='"+c+"'WHERE Roll_Number='"+roll+"'")
               db.commit()
               print("Marks Updated Successfully.")
           elif ch==3:
                ip=str(input("Enter the Updated marks in Information Practices:"))
                cursor.execute("UPDATE Marks SET I_P='"+ip+"'WHERE Roll_Number='"+roll+"'")
                db.commit()
                print("Marks Updated Successfully.")
           elif ch==4:
                b=str(input("Enter the Updated marks in Biology:"))
                cursor.execute("UPDATE Marks SET Biology='"+b+"'WHERE Roll_Number='"+roll+"'")
                db.commit()
                print("Marks Updated Successfully.")
           elif ch==5:
                e=str(input("Enter the Updated marks in English:"))
                cursor.execute("UPDATE Marks SET English='"+e+"'WHERE Roll_Number='"+roll+"'")
                db.commit()
                print("Marks Updated Successfully.")
           else:
                    print("Wrong Choice.")
                    print("Try Again.")
                    ch=input("Enter Y if want to continue else press any other key.")
                    if ch=='Y' or ch=='y':
                           continue
                    else:
                           break
           c=input("Want to Update More Marks Press Y else press any other key:")
           if c=='y' or c=='Y':
               continue
           else:
                break
    
    else:
        print("Wrong Choice!")
        print("Try Again.")
    db.close()
#_________________________________________________________________________________________
#_________________________________________________________________________________________
#To show student details
def Delete():
    print("\t\t ________________________")
    print("\t\t|                        | ")
    print("\t\t|      DATA ERASER       |")
    print("\t\t|________________________|")
    print("Welcome to Deleting Menu.")
    print("All Data will be erased permanently.")
    print("Please provide your Roll Number for deleting the records.")
    roll=str(input("Enter your Board Roll Number:"))
    import mysql.connector as mysql
    db=mysql.connect(host="localhost",user='root',passwd=p_w,database='Student')
    cursor=db.cursor()
    cursor.execute("DELETE FROM Student_Details WHERE Roll_Number='"+roll+"'")
    cursor.execute("DELETE FROM Marks WHERE Roll_Number='"+roll+"'")
    cursor.execute("DELETE FROM Grade WHERE Roll_Number='"+roll+"'")
    db.commit()
    print("All Data has been Erased Successfully.")
    db.close()
    
#_________________________________________________________________________________________
#_________________________________________________________________________________________
#To print the student details
def Details():
    print("\t\t ________________________")
    print("\t\t|                        | ")
    print("\t\t|    STUDENT DETAILS     |")
    print("\t\t|________________________|")
    print("Welcome to Details Menu.")
    print("Please provide your Roll Number for printing the records.")
    roll=input("Enter your Board Roll Number:")
    import mysql.connector as mysql
    db=mysql.connect(host="localhost",user='root',passwd=p_w,database='Student')
    cursor=db.cursor()
    cursor.execute("Select Name,Mother_Name,Father_Name,School From Student_Details where Roll_Number='"+roll+"'")
    for m in cursor:
        l=['No use']
    p,q,r,s=m
    print("Name of the Student:",p)
    print("Mother's Name:",q)
    print("Father's Name:",r)
    print("School:",s)
    db.close()


#_________________________________________________________________________________________
#_________________________________________________________________________________________
#To give random sl. no. to the markheet.
def sno():
    x='0377367'
    import random
    z=random.randint(1,1000)
    y=str(z)
    random=x+y
    return random
#To do uppercase
def up(p):
    x=p.upper()
    return x
    
#To give  final grade
def grd(a):
    if a>=90 and a<=100:
        return ' A1 '
    elif a>100:
        return 'A1'
    elif a>=80 and a<=90:
        return ' A2 '
    elif a>=70 and a<=80:
        return ' B1 '
    elif a>=60 and a<=70:
        return ' B2 '
    elif a>=50 and a<=60:
        return ' C1 '
    elif a>=40 and a<=50:
        return ' C2 '
    elif a>=33 and a<=40:
        return ' D1 '
    else:
        return 'FAIL'
#To check passing in theory in cs,chem and phy
def t(a):
    if a>=24 and a<=70:
            return a
    elif a>=0 and a<=23:
            return ' FT '
    elif a>70:
            return 70.0
    elif a<0:
           return 0

#To check passing in theory in eng and math
def o(a):
    if a>=27 and a<=80:
        return a
    elif a>=0 and a<=26:
        return ' FT '
    elif a>80:
        return 80.0
    elif a<0:
        return 0
#To check passing in practicals in cs,chem and phy
def y(a):
    if a>=10 and a<=30:
        return a
    elif a>=0 and a<=9:
        return ' FP '
    elif a>30:
        return 30.0
    elif a<0:
        return 0
#To check passing in practicals in maths and eng
def f(a):
    if a>=7 and a<=20:
        return a
    elif a>=0 and a<=6:
        return ' FP '
    elif a>20:
        return 20.0
    elif a<0:
        return 0
#To check pass or fail
def pa(a,b,c,d,e,a1,b1,c1,d1,e1):
    if t(a)==' FT ' or t(b)==' FT ' or t(d)==' FT ' or o(c)==' FT ' or o(e)==' FT ':
        return 'FAIL'
    elif y(a1)==' FP ' or y(b1)==' FP ' or f(c1)==' FP ' or y(d1)==' FP ' or f(e1)==' FP ':
        return 'FAIL'
    else:
        return 'PASS'    
#_________________________________________________________________________________________
#_________________________________________________________________________________________
#To show the list of existing roll no.
def eroll():
    import mysql.connector as mysql
    db=mysql.connect(host="localhost",user='root',passwd=p_w,database='Student')
    cursor=db.cursor()
    cursor.execute('Select Roll_Number from Student_Details')
    l=[]
    for s in cursor:
        l.append(s)
    print("\t\t ______________________________")
    print("\t\t|                              | ")
    print("\t\t|  EXISTING ROLL NUMBER LIST   |")
    print("\t\t|______________________________|")    
    print(l)
    db.close()     
#_________________________________________________________________________________________
#_________________________________________________________________________________________
def Result():
    c='y'
    while c=='y' or c=='Y':
        print("\t\t ________________________")
        print("\t\t|                        | ")
        print("\t\t|  MARKSHEET GENERATOR   |")
        print("\t\t|________________________|")
        roll=str(input("Enter your board Roll Number:"))
        print("1:Physics,Chemistry,Mathematics,Computer Science,English")
        print("2:Physics,Chemistry,Mathematics,Hindi,English")
        print("3:Physics,Chemistry,Mathematics,Biology,English")
        print("4:Physics,Chemistry,Biology,Hindi,English")
        print("5:Physics,Chemistry,Biology,I.P.,English")
        ch=int(input("Enter the number for your stream:"))
        if ch==1:
            import mysql.connector as mysql
            db=mysql.connect(host="localhost",user='root',passwd=p_w,database='Student')
            cursor=db.cursor()
            cursor.execute("Select Name,Mother_Name,Father_Name,School From Student_Details where Roll_Number='"+roll+"'")
            for m in cursor:
                l=['No use']
            p,q,r,s=m
            cursor.execute("Select Physics,Chemistry,Mathematics,C_S,English From Marks where Roll_Number='"+roll+"'")
            for j1 in cursor:
                l=['No use']
            a,b,c,d,e=j1
            cursor.execute("Select Physics_pr,Chemistry_pr,Mathematics_pr,C_S_pr,English_pr From Marks where Roll_Number='"+roll+"'")
            for x in cursor:
                l=['No use']
            a1,b1,c1,d1,e1=x
            cursor.execute("Select Work_Experience,Physical_Health,General_Studies From Grade where Roll_Number='"+roll+"'")
            for x1 in cursor:
                l=['No use']
            g,h,i=x1
            a2=a+a1
            b2=b+b1
            c2=c+c1
            d2=d+d1
            e2=e+e1
            print("क्रमांक                                         केन्द्रीय माध्यमिक शिक्षा बोर्ड")
            print("S.No.SSCE/2020                       CENTRAL BOARD OF SECONDAY EDUCATION")
            print("                                         अंक विवरणिका परीक्षा MARKS STATEMENT")
            print("\t",    sno(),"                            सीनियर स्कूल सर्टिफिकेट परीक्षा,2020 ")
            print("ALL INDIA                          SENIOR SCHOOL CERTIFICATE EXAMINATION,2020")
            print("नाम Name",up(p),"                                              अनुक्रमांक Roll No.")
            print("माता का नाम Mother's Name",up(q) ,"\t\t\t\t\t\t",roll)
            print("पिता का नाम Father's Name",up(r))
            print("विद्यालय School",up(s))
            print(" ______________________________________________________________________")
            print("|विषय कोड|                  |    प्राप्तांक     MARKS OBTAINED |                |")
            print("|     |                   |___________________________|   स्थितीय ग्रेड       |")
            print("|SUB. |   विषय SUBJECT     |  लि.    |   प्रै.   | योग       |   POSITIONAL   |")
            print("|CODE |                   |  TH    |  PR    | TOTAL   |   GRADE        |")
            print("|_____|___________________|________|________|_________|________________|")
            print("|301  | ENGLISH CORE      | ",o(e)," | ",f(e1)," | ",e2,"  |  ",grd(e2),"        |")
            print("|041  | MATHEMATICS       | ",o(c)," | ",f(c1)," | ",c2,"  |  ",grd(c2),"        |")
            print("|042  | PHYSICS           | ",t(a)," | ",y(a1)," | ",a2,"  |  ",grd(a2),"        |")
            print("|043  | CHEMISTRY         | ",t(b)," | ",y(b1)," | ",b2,"  |  ",grd(b2),"        |")
            print("|083  | COMPUTER SCIENCE  | ",t(d)," | ",y(d1)," | ",d2,"  |  ",grd(d2),"        |")
            print("|500  | WORK EXPERIENCE   |        |        |         |   ",up(g),"         |")
            print("|502  | PHY & HEALTH EDUCA|        |        |         |   ",up(h),"         |")
            print("|503  | GENERAL STUDIES   |        |        |         |   ",up(i),"         |")
            print("|_____|___________________|________|________|_________|________________|")
            print("संक्षिप्तियों का अर्थ : Abbreviations")
            print("AB:विषय में अनुपस्थित Absent in the Subject              परिणाम    Result")
            print("EX:छूट-प्राप्त Exempted","\t\t\t\t\t", pa(a,b,c,d,e,a1,b1,c1,d1,e1))
            print("FP:प्रयोगात्म्क में असफल Fail in Practical")
            print("FT:लिखिल में असफल Fail in Theory                         ~SMT~                       ")
            print("दिल्ली Delhi                                           परीक्षा नियंत्रक                     ")
            print("दिनांक Dated                                   Controller of Examinations")
            db.close()
            
        elif ch==2:
            import mysql.connector as mysql
            db=mysql.connect(host="localhost",user='root',passwd=p_w,database='Student')
            cursor=db.cursor()
            cursor.execute("Select Name,Mother_Name,Father_Name,School From Student_Details where Roll_Number='"+roll+"'")
            for m in cursor:
                l=['No use']
            p,q,r,s=m
            cursor.execute("Select Physics,Chemistry,Mathematics,Hindi,English From Marks where Roll_Number='"+roll+"'")
            for j1 in cursor:
                l=['No use']
            a,b,c,d,e=j1
            cursor.execute("Select Physics_pr,Chemistry_pr,Mathematics_pr,Hindi_pr,English_pr From Marks where Roll_Number='"+roll+"'")
            for x in cursor:
                l=['No use']
            a1,b1,c1,d1,e1=x
            cursor.execute("Select Work_Experience,Physical_Health,General_Studies From Grade where Roll_Number='"+roll+"'")
            for x1 in cursor:
                l=['No use']
            g,h,i=x1
            a2=a+a1
            b2=b+b1
            c2=c+c1
            d2=d+d1
            e2=e+e1
            print("क्रमांक                                         केन्द्रीय माध्यमिक शिक्षा बोर्ड")
            print("S.No.SSCE/2020                       CENTRAL BOARD OF SECONDAY EDUCATION")
            print("                                         अंक विवरणिका परीक्षा MARKS STATEMENT")
            print("\t",    sno(),"                            सीनियर स्कूल सर्टिफिकेट परीक्षा,2020 ")
            print("ALL INDIA                          SENIOR SCHOOL CERTIFICATE EXAMINATION,2020")
            print("नाम Name",up(p),"                                                      अनुक्रमांक Roll No.")
            print("माता का नाम Mother's Name ",up(q), "\t\t\t\t\t\t",roll,)
            print("पिता का नाम Father's Name",up(r))
            print("विद्यालय School",up(s))
            print(" ______________________________________________________________________")
            print("|विषय कोड|                  |    प्राप्तांक     MARKS OBTAINED |                |")
            print("|     |                   |___________________________|   स्थितीय ग्रेड       |")
            print("|SUB. |   विषय SUBJECT     |  लि.    |   प्रै.   | योग       |   POSITIONAL   |")
            print("|CODE |                   |  TH    |  PR    | TOTAL   |   GRADE        |")
            print("|_____|___________________|________|________|_________|________________|")
            print("|301  | ENGLISH CORE      | ",o(e)," | ",f(e1)," | ",e2,"  |  ",grd(e2),"        |")
            print("|041  | MATHEMATICS       | ",o(c)," | ",f(c1)," | ",c2,"  |  ",grd(c2),"        |")
            print("|042  | PHYSICS           | ",t(a)," | ",y(a1)," | ",a2,"  |  ",grd(a2),"        |")
            print("|043  | CHEMISTRY         | ",t(b)," | ",y(b1)," | ",b2,"  |  ",grd(b2),"        |")
            print("|302  | HINDI             | ",t(d)," | ",y(d1)," | ",d2,"  |  ",grd(d2),"        |")
            print("|500  | WORK EXPERIENCE   |        |        |         |   ",up(g),"         |")
            print("|502  | PHY & HEALTH EDUCA|        |        |         |   ",up(h),"         |")
            print("|503  | GENERAL STUDIES   |        |        |         |   ",up(i),"         |")
            print("|_____|___________________|________|________|_________|________________|")
            print("संक्षिप्तियों का अर्थ : Abbreviations")
            print("AB:विषय में अनुपस्थित Absent in the Subject             परिणाम   Result")
            print("EX:छूट-प्राप्त Exempted","\t\t\t\t\t", pa(a,b,c,d,e,a1,b1,c1,d1,e1))
            print("FP:प्रयोगात्म्क में असफल Fail in Practical")
            print("FT:लिखिल में असफल Fail in Theory                         ~SMT~                       ")
            print("दिल्ली Delhi                                           परीक्षा नियंत्रक                     ")
            print("दिनांक Dated                                   Controller of Examinations")
            db.close()

        elif ch==3:
            import mysql.connector as mysql
            db=mysql.connect(host="localhost",user='root',passwd=p_w,database='Student')
            cursor=db.cursor()
            cursor.execute("Select Name,Mother_Name,Father_Name,School From Student_Details where Roll_Number='"+roll+"'")
            for m in cursor:
                l=['No use']
            p,q,r,s=m
            cursor.execute("Select Physics,Chemistry,Mathematics,Biology,English From Marks where Roll_Number='"+roll+"'")
            for j1 in cursor:
                l=['No use']
            a,b,c,d,e=j1
            cursor.execute("Select Physics_pr,Chemistry_pr,Mathematics_pr,Biology_pr,English_pr From Marks where Roll_Number='"+roll+"'")
            for x in cursor:
                l=['No use']
            a1,b1,c1,d1,e1=x
            cursor.execute("Select Work_Experience,Physical_Health,General_Studies From Grade where Roll_Number='"+roll+"'")
            for x1 in cursor:
                l=['No use']
            g,h,i=x1
            a2=a+a1
            b2=b+b1
            c2=c+c1
            d2=d+d1
            e2=e+e1
            print("क्रमांक                                         केन्द्रीय माध्यमिक शिक्षा बोर्ड")
            print("S.No.SSCE/2020                       CENTRAL BOARD OF SECONDAY EDUCATION")
            print("                                         अंक विवरणिका परीक्षा MARKS STATEMENT")
            print("\t",    sno(),"                            सीनियर स्कूल सर्टिफिकेट परीक्षा,2020 ")
            print("ALL INDIA                          SENIOR SCHOOL CERTIFICATE EXAMINATION,2020")
            print("नाम Name",up(p),"                                                      अनुक्रमांक Roll No.")
            print("माता का नाम Mother's Name ",up(q), "\t\t\t\t\t\t",roll,)
            print("पिता का नाम Father's Name",up(r))
            print("विद्यालय School",up(s))
            print(" ______________________________________________________________________")
            print("|विषय कोड|                  |    प्राप्तांक     MARKS OBTAINED |                |")
            print("|     |                   |___________________________|   स्थितीय ग्रेड       |")
            print("|SUB. |   विषय SUBJECT     |  लि.    |   प्रै.   | योग       |   POSITIONAL   |")
            print("|CODE |                   |  TH    |  PR    | TOTAL   |   GRADE        |")
            print("|_____|___________________|________|________|_________|________________|")
            print("|301  | ENGLISH CORE      | ",o(e)," | ",f(e1)," | ",e2,"  |  ",grd(e2),"        |")
            print("|041  | MATHEMATICS       | ",o(c)," | ",f(c1)," | ",c2,"  |  ",grd(c2),"        |")
            print("|042  | PHYSICS           | ",t(a)," | ",y(a1)," | ",a2,"  |  ",grd(a2),"        |")
            print("|043  | CHEMISTRY         | ",t(b)," | ",y(b1)," | ",b2,"  |  ",grd(b2),"        |")
            print("|044  | BIOLOGY           | ",t(d)," | ",y(d1)," | ",d2,"  |  ",grd(d2),"        |")
            print("|500  | WORK EXPERIENCE   |        |        |         |   ",up(g),"         |")
            print("|502  | PHY & HEALTH EDUCA|        |        |         |   ",up(h),"         |")
            print("|503  | GENERAL STUDIES   |        |        |         |   ",up(i),"         |")
            print("|_____|___________________|________|________|_________|________________|")
            print("संक्षिप्तियों का अर्थ : Abbreviations")
            print("AB:विषय में अनुपस्थित Absent in the Subject             परिणाम   Result")
            print("EX:छूट-प्राप्त Exempted","\t\t\t\t\t", pa(a,b,c,d,e,a1,b1,c1,d1,e1))
            print("FP:प्रयोगात्म्क में असफल Fail in Practical")
            print("FT:लिखिल में असफल Fail in Theory                         ~SMT~                       ")
            print("दिल्ली Delhi                                           परीक्षा नियंत्रक                     ")
            print("दिनांक Dated                                   Controller of Examinations")
            db.close()
        elif ch==4:
            import mysql.connector as mysql
            db=mysql.connect(host="localhost",user='root',passwd=p_w,database='Student')
            cursor=db.cursor()
            cursor.execute("Select Name,Mother_Name,Father_Name,School From Student_Details where Roll_Number='"+roll+"'")
            for m in cursor:
                l=['No use']
            p,q,r,s=m
            cursor.execute("Select Physics,Chemistry,Hindi,Biology,English From Marks where Roll_Number='"+roll+"'")
            for j1 in cursor:
                l=['No use']
            a,b,c,d,e=j1
            cursor.execute("Select Physics_pr,Chemistry_pr,Hindi_pr,Biology_pr,English_pr From Marks where Roll_Number='"+roll+"'")
            for x in cursor:
                l=['No use']
            a1,b1,c1,d1,e1=x
            cursor.execute("Select Work_Experience,Physical_Health,General_Studies From Grade where Roll_Number='"+roll+"'")
            for x1 in cursor:
                l=['No use']
            g,h,i=x1
            a2=a+a1
            b2=b+b1
            c2=c+c1
            d2=d+d1
            e2=e+e1
            print("क्रमांक                                         केन्द्रीय माध्यमिक शिक्षा बोर्ड")
            print("S.No.SSCE/2020                       CENTRAL BOARD OF SECONDAY EDUCATION")
            print("                                         अंक विवरणिका परीक्षा MARKS STATEMENT")
            print("\t",    sno(),"                            सीनियर स्कूल सर्टिफिकेट परीक्षा,2020 ")
            print("ALL INDIA                          SENIOR SCHOOL CERTIFICATE EXAMINATION,2020")
            print("नाम Name",up(p),"                                                      अनुक्रमांक Roll No.")
            print("माता का नाम Mother's Name ",up(q), "\t\t\t\t\t\t",roll,)
            print("पिता का नाम Father's Name",up(r))
            print("विद्यालय School",up(s))
            print(" ______________________________________________________________________")
            print("|विषय कोड|                  |    प्राप्तांक     MARKS OBTAINED |                |")
            print("|     |                   |___________________________|   स्थितीय ग्रेड       |")
            print("|SUB. |   विषय SUBJECT     |  लि.    |   प्रै.   | योग       |   POSITIONAL   |")
            print("|CODE |                   |  TH    |  PR    | TOTAL   |   GRADE        |")
            print("|_____|___________________|________|________|_________|________________|")
            print("|301  | ENGLISH CORE      | ",o(e)," | ",f(e1)," | ",e2,"  |  ",grd(e2),"        |")
            print("|302  | HINDI             | ",o(c)," | ",f(c1)," | ",c2,"  |  ",grd(c2),"        |")
            print("|042  | PHYSICS           | ",t(a)," | ",y(a1)," | ",a2,"  |  ",grd(a2),"        |")
            print("|043  | CHEMISTRY         | ",t(b)," | ",y(b1)," | ",b2,"  |  ",grd(b2),"        |")
            print("|044  | BIOLOGY           | ",t(d)," | ",y(d1)," | ",d2,"  |  ",grd(d2),"        |")
            print("|500  | WORK EXPERIENCE   |        |        |         |   ",up(g),"         |")
            print("|502  | PHY & HEALTH EDUCA|        |        |         |   ",up(h),"         |")
            print("|503  | GENERAL STUDIES   |        |        |         |   ",up(i),"         |")
            print("|_____|___________________|________|________|_________|________________|")
            print("संक्षिप्तियों का अर्थ : Abbreviations")
            print("AB:विषय में अनुपस्थित Absent in the Subject             परिणाम   Result")
            print("EX:छूट-प्राप्त Exempted","\t\t\t\t\t", pa(a,b,c,d,e,a1,b1,c1,d1,e1))
            print("FP:प्रयोगात्म्क में असफल Fail in Practical")
            print("FT:लिखिल में असफल Fail in Theory                         ~SMT~                       ")
            print("दिल्ली Delhi                                           परीक्षा नियंत्रक                     ")
            print("दिनांक Dated                                   Controller of Examinations")
            db.close()


        elif ch==5:
            import mysql.connector as mysql
            db=mysql.connect(host="localhost",user='root',passwd=p_w,database='Student')
            cursor=db.cursor()
            cursor.execute("Select Name,Mother_Name,Father_Name,School From Student_Details where Roll_Number='"+roll+"'")
            for m in cursor:
                l=['No use']
            p,q,r,s=m
            cursor.execute("Select Physics,Chemistry,Biology,I_P,English From Marks where Roll_Number='"+roll+"'")
            for j1 in cursor:
                l=['No use']
            a,b,c,d,e=j1
            cursor.execute("Select Physics_pr,Chemistry_pr,Biology_pr,I_P_pr,English_pr From Marks where Roll_Number='"+roll+"'")
            for x in cursor:
                l=['No use']
            a1,b1,c1,d1,e1=x
            cursor.execute("Select Work_Experience,Physical_Health,General_Studies From Grade where Roll_Number='"+roll+"'")
            for x1 in cursor:
                l=['No use']
            g,h,i=x1
            a2=a+a1
            b2=b+b1
            c2=c+c1
            d2=d+d1
            e2=e+e1
            print("क्रमांक                                            केन्द्रीय माध्यमिक शिक्षा बोर्ड")
            print("S.No.SSCE/2020                           CENTRAL BOARD OF SECONDAY EDUCATION")
            print("                                             अंक विवरणिका परीक्षा MARKS STATEMENT")
            print("\t",    sno(),"                               सीनियर स्कूल सर्टिफिकेट परीक्षा,2020 ")
            print("ALL INDIA                               SENIOR SCHOOL CERTIFICATE EXAMINATION,2020")
            print("नाम Name",up(p),"                                                        अनुक्रमांक Roll No.")
            print("माता का नाम Mother's Name ",up(q), "\t\t\t\t\t\t\t",roll,)
            print("पिता का नाम Father's Name",up(r))
            print("विद्यालय School",up(s))
            print(" __________________________________________________________________________")
            print("|विषय कोड|                      |    प्राप्तांक     MARKS OBTAINED |                |")
            print("|     |                      |___________________________|   स्थितीय ग्रेड       |")
            print("|SUB. |   विषय SUBJECT        |  लि.    |   प्रै.   | योग       |   POSITIONAL   |")
            print("|CODE |                      |  TH    |  PR    | TOTAL   |   GRADE        |")
            print("|_____|______________________|________|________|_________|________________|")
            print("|301  | ENGLISH CORE         | ",o(e)," | ",f(e1)," | ",e2,"  |  ",grd(e2),"        |")
            print("|044  | BIOLOGY              | ",o(c)," | ",f(c1)," | ",c2,"  |  ",grd(c2),"        |")
            print("|042  | PHYSICS              | ",t(a)," | ",y(a1)," | ",a2,"  |  ",grd(a2),"        |")
            print("|043  | CHEMISTRY            | ",t(b)," | ",y(b1)," | ",b2,"  |  ",grd(b2),"        |")
            print("|065  | INFORMATION PRACTICES| ",t(d)," | ",y(d1)," | ",d2,"  |  ",grd(d2),"        |")
            print("|500  | WORK EXPERIENCE      |        |        |         |   ",up(g),"         |")
            print("|502  | PHY & HEALTH EDUCA   |        |        |         |   ",up(h),"         |")
            print("|503  | GENERAL STUDIES      |        |        |         |   ",up(i),"         |")
            print("|_____|______________________|________|________|_________|________________|")
            print("संक्षिप्तियों का अर्थ : Abbreviations")
            print("AB:विषय में अनुपस्थित Absent in the Subject             परिणाम   Result")
            print("EX:छूट-प्राप्त Exempted","\t\t\t\t\t", pa(a,b,c,d,e,a1,b1,c1,d1,e1))
            print("FP:प्रयोगात्म्क में असफल Fail in Practical")
            print("FT:लिखिल में असफल Fail in Theory                         ~SMT~                       ")
            print("दिल्ली Delhi                                           परीक्षा नियंत्रक                     ")
            print("दिनांक Dated                                   Controller of Examinations")
            db.close()
        else:
            print("Your Choice is Wrong.")
            print("Please Try Again.")
        c=input("Press Y for continue else press any other key:")
        if c=='Y' or c=='y':
            continue
        else:
            break

#_________________________________________________________________________________________
#_________________________________________________________________________________________
#About the Project
def about():
    print("\nSTUDENT'S MARKSHEET MANAGEMENT SYSTEM FOR CLASS XII SCIENCE\n")
    print("**This project has been made for partial fulfilment of AISSCE 2020 -21 **")
    print("Made by:- SHUBHANSHU MANI TRIPATHI XII(SCIENCE)")
    print("Our Project is about Marksheet Management.")
    print("The user in the starting will select his choice from the menu and will enter")
    print("the details that are asked in that particular choice that he had made. ")
    print("After that user has to choose the 6th Option to print his Marksheet.")
    print("His Marksheet will be Successfully printed.")

#_________________________________________________________________________________________
#_________________________________________________________________________________________
#To exit
def leave():
    import sys
    print("                       ___      _                 _      ")
    print("                        |  |_| |_| |\ | |/   \ / | | | | ")
    print("                        |  | | | | | \| |\    |  |_| |_| ")
    print(" \n")
    print("                                   VISIT AGAIN !")
    print("                                     ________            ")
    print("                                    |        |     ")
    print("                                    |  O  O  |     ")
    print("                                    |  \__/  |")
    print("                                    |________|             ")
    sys.exit()

#_________________________________________________________________________________________
#_________________________________________________________________________________________
#Computer Science Project Class 12
#Student Data Management System
while True:
    print('\t ______________________________________________________________________')
    print('\t|    ______________________________________________________________    |')
    print('\t|   |                                                              |   |')
    print('\t|   |**************************************************************|   |')
    print("\t|   |   STUDENT'S MARKSHEET MANAGEMENT SYSTEM FOR CLASS XII SCIENCE|   |")
    print('\t|   |**************************************************************|   |')
    print('\t|   |______________________________________________________________|   |')
    print('\t|______________________________________________________________________|')
    print("**This project has been made for partial fulfilment of AISSCE 2020 -21.**")
    print("Welcome to the Student Marksheet Management System for Class XII SCIENCE")
    print("Here you can Create,Update,Print and Delete Student's Record.")
    print("The Main tool is your Unique Board Roll Number.")
    print(" __________________________________________________________")
    print("|                                                          |")
    print("|1|->>      To Add New Student Details and Marks.          |")
    print("|2|->>      To Modify the Existing Record.                 |")
    print("|3|->>      To Delete the Existing Record.                 |")
    print("|4|->>      To Print the Student's Details.                |")
    print("|5|->>      To Print  the List of Existing Roll Numbers.   |")
    print("|6|->>      To Print the Student's Marksheet.              |")
    print("|7|->>      About                                          |")
    print("|8|->>      Exit                                           |")
    print('|__________________________________________________________|')
    database()
    table()
    marks_science()
    grade()
    choice=int(input("Enter your Choice by seeing the Above Menu:"))
    if choice==1:
        Student_Details()
        Subject()
    elif choice==2:
        Update()
    elif choice==3:
        Delete()
    elif choice==4:
        Details()
    elif choice==5:
        eroll()
    elif choice==6:
        Result()
    elif choice==7:
        about()
    elif choice==8:
        leave()
    else:
        print("Wrong Choice")
        print("Try Again")
        ch=input("Press Y if want to continue else Press any other key:")
        if ch=='Y' or ch=='y':
            continue
        else:
            leave()
            break
    print("If you want to go to the Main Menu then press Y else press any other key.")
    ch=input("Enter Y or N as per your choice:")
    if ch=='Y' or ch=='y':
        continue
    else:
        leave()
        break














