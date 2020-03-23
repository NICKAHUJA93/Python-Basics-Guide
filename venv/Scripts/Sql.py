import sqlite3
#CRUD
#CURSOR
def createTable():
    query = "create table if not exists login (id Integer(4),username TEXT(32) ,password TEXT(32))"
    con.execute(query)
    con.commit()
# String should be in single court in SQL
def insertData(uid,un,up):
    query = "insert into login values(%d,'%s','%s')"%(uid,un,up)
    con.execute(query)
    con.commit()
#SQL will return result set and get stored in cursor ,We need to fetch all rows in the cursors
def deleteData(deleteid):
    query = "DELETE FROM login WHERE id =%d"% (deleteid)
    con.execute(query)
    con.commit()
def fetchData():
    query = "select * from login"
    cur = con.execute(query)
    rows = cur.fetchall()
    for r in rows:
        s1 =str(r[0])+"\t"+r[1]+"\t"+r[2]
        print(s1)
con = sqlite3.connect("college.db")
if con!=None:
    print("connected with database",type(con))
    createTable()
    print("Enter the data")
    userid=int(input("Enter User ID"))
    un=input("Enter user name")
    unpass=input("Enter user password")
    insertData(userid,un,unpass)
    fetchData()
    deleteid=int(input("Enter ID to be deleted"))
    deleteData(deleteid)
else:
    print("Connection failed")