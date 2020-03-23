#Update the database in such a way that number will represent different optiion for the database
import sqlite3
def create_Table():
    querry = "create table if not exists Student_database(id Integer(4) PRIMARY KEY,name CHAR(30),age Integer(4),address CHAR(50),course_opt CHAR(50),course_duration Integer(4),fees Integer(6))"
    con.execute(querry)
    con.commit()
def fetch_table():
    querry = "Select * from Student_database"
    # Convert into cursor
    cur= con.execute(querry)
    # convert into rows
    rows=cur.fetchall()
    for r in rows:
        s1 =str(r[0]) +"\t"+ r[1] +"\t"+str(r[2]) +"\t" +r[3] +"\t" +r[4] +"\t"+str(r[5]) +"\t"+str(r[6])
        print(s1)
def insert_data(id,name,age,address,course_opt,course_duration,fees):
    querry = "Insert into Student_database values(%d,'%s',%d,'%s','%s',%d,%d)"%(id,name,age,address,course_opt,course_duration,fees)
    con.execute(querry)
    con.commit()
def drop_table(condition):
    if condition == True:
        querry = "Drop table Student_database"
        con.execute(querry)
        con.commit()
    else:
        print("Do not drop the table")
def search_record():
    id_input = int(input("Enter the ID to be search\n"))
    querry = "Select * from Student_database WHERE id = (%d)"%(id_input)
    cur=con.execute(querry)
    rows=cur.fetchall()
    for r in rows:
        s1 = str(r[0]) + "\t" + r[1] + "\t" + str(r[2]) + "\t" + r[3] + "\t" + r[4] + "\t" + str(r[5]) + "\t" + str(r[6])
        print(s1)
def delete_record(condition):
    if condition == True:
        Id_Input =int(input("Enter the student id to be deleted\n"))
        querry = "DELETE FROM Student_database WHERE id =%d"%(Id_Input)
        con.execute(querry)
        con.commit()
    else:
        print("Can not delete the record")

#Create a connectoion with database
con = sqlite3.connect("Student.db")
if con != None:
    print("Connected with Adifico data base")
    id = int(input("Enter the ID"))
    name = str(input("Enter the name of the student"))
    age = int(input("Enter the age of the student"))
    address = str(input("Enter the address of the student"))
    course_opt =str(input("Enter the courses opt by students"))
    course_duration =int(input("Enter the course duration in months"))
    fees = int(input("Enter the fees of the student"))
    create_Table()
    insert_data(id,name,age,address,course_opt,course_duration,fees)
    fetch_table()
    drop_table(False)
    fetch_table()
    search_record()
    delete_record(True)
    print("Feching a table after record delete")
    fetch_table()