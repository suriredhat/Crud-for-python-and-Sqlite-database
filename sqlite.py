import sqlite3
import os
from flask import Flask,render_template,request,flash,redirect
from flask_wtf.csrf import CSRFProtect
app = Flask(__name__)
csrf = CSRFProtect(app)
Database="Student.db"
@app.route('/',methods=["GET","POST"])
def home():
    if(os.path.isfile(Database)):
        conn = sqlite3.connect(Database)
        print("Opened Database")
        cursor = conn.execute("SELECT * from tbl_course")
        myresult = cursor.fetchall()
        return render_template("Crud/sqlite.html",Records=myresult,pageBack=1,PageNext=1,PageCount=1)
        conn.commit()
        conn.close()
        
    else:
        print("Database Not Found")

   
   

@app.route('/crud/create',methods=["GET","POST"])
def insert():
    
    if request.method == "POST":

        if(os.path.isfile(Database)):
            conn = sqlite3.connect(Database)
            cursorObj = conn.cursor()
            cname=request.form['inscname']
            duration=request.form['insduration']
            fees=request.form['insfee']
            cursorObj.execute("INSERT INTO tbl_course(Coursename,Duration,Fees) VALUES (?,?,?)",(cname,duration,fees))
            conn.commit()
            if(conn.total_changes>=1):
                return redirect("/")
            else:
                print("Not Inserted")
            
            conn.close()
        else:
            print("Database Not Found")
    else:

         return redirect("/")


@app.route('/crud/delete',methods=["GET","POST"])
def deleteR():

    if request.method == "POST":

        conn = sqlite3.connect(Database)
        mycursor = conn.cursor()
        cid=request.form['delc_id']
        sql="delete from tbl_course where ID=?"
        conn.execute(sql,(cid))
        conn.commit()
        print("Record Deleted")
        return redirect("/")

    else:
        return redirect("/")


@app.route('/crud/recupdt',methods=["GET","POST"])
def record():

    if request.method == "POST":

        if(os.path.isfile(Database)):
            conn = sqlite3.connect(Database)
            cursorObj = conn.cursor()
            cid=request.form['ucid']
            cname=request.form['ucname']
            duration=request.form['uduration']
            fees=request.form['ufee']
            sql="update tbl_course set Coursename=?,Duration=?,Fees=? where ID=?"
            conn.execute(sql,(cname,duration,fees,cid))
            conn.commit()
            if(conn.total_changes>=1):
                return redirect("/")
            else:
                print("Not Updated")
            
            conn.close()
        else:
            print("Database Not Found")
    else:

         return redirect("/")    

if __name__ =='__main__':
     app.config['SECRET_KEY'] = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
     app.run(debug=True)
   