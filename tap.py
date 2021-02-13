from flask import Flask,render_template,request,redirect,flash,url_for
import sqlite3 as sql  

app = Flask(__name__)
app.secret_key = "vpn"

@app.route("/")
def home():
    return render_template("thome.html")

@app.route('/tloginpage')
def loginpage():
    return render_template("tlogin.html")

@app.route("/register")
def register():
    return render_template('signup.html')

@app.route("/tlogin",methods = ['POST','GET']) 
def tlogin():
    if request.method == 'POST':
        try :
            uname = request.form['Username']
            pwd = request.form['Password']

            with sql.connect("teacher.db") as con :
                con.row_factory = sql.Row
                cur = con.cursor() 
                cur.execute("SELECT username , password FROM teacher_information WHERE username = ? AND password = ?",(uname,pwd) )
                records = cur.fetchall()

                if len(records) == 1 :
                    msg1 = "Logged in"
                    msg2 = "Continue"
                    return render_template("all2.html",msg1 = msg1 , msg2 = msg2 , uname = uname)
                else :
                    flash("Invalid Username or Password")
                    flag = 1
                    return render_template("tlogin.html",flag = flag)
        except :
            con.rollback()
            msg1 = "Login Failed"
            msg2 = "Retry"
            return render_template("all.html",msg1 = msg1 , msg2 = msg2)


@app.route("/signup",methods = ['POST','GET'])
def signup():
    if request.method == 'POST':
        try :
            username = request.form['Username']
            name = request.form["Name"]
            trade = request.form['Trade']
            department = request.form['Department']
            course_code = request.form['Coursecode']
            semester = request.form["Semester"]
            year = request.form["Year"]
            password = request.form['Password']
            cpassword = request.form['Cpassword']

            with sql.connect("teacher.db") as con:
                cur = con.cursor()
                if password == cpassword :
                    cur.execute("SELECT username FROM teacher_information WHERE username = ?",(username,) )
                    records = cur.fetchall()
                    if len(records) == 1 :
                        flash("Username already taken !!")
                        flag = 6
                        return render_template("signup.html",flag = flag)
                    else :
                        cur.execute("INSERT INTO teacher_information (username,Name,trade,department,course_code,semester,year,password) VALUES (?,?,?,?,?,?,?,?)",(username,name,trade,department,course_code,semester,year,password) )
                        con.commit()
                        msg1 = "Registered successfully"
                        msg2 = "Login"
                        return render_template("all.html",msg1 = msg1 , msg2 = msg2)
                else:
                    flash("Password did not match !!")
                    flag = 4
                    return render_template("signup.html",flag = flag)
        except:
            con.rollback()
            msg1 = "Error in Registration"
            msg2 = "Retry"
            return render_template("all1.html",msg1 = msg1 , msg2 = msg2)


@app.route('/toptions/<uname>')
def toptions(uname) :
    return render_template('toptions.html',uname = uname)

@app.route("/updation/<uname>")
def updation(uname):
    return render_template('operation.html',uname = uname)

@app.route('/umres/<uname>',methods = ['POST','GET'])
def umres(uname):
    if request.method == 'POST':
        try:
            purpose = request.form["purpose"]
            return render_template("resupdate.html",uname = uname,purpose = purpose)
        except:
            flash("Something went wrong !")
            return render_template("operation.html",uname = uname,purpose = purpose)

@app.route('/change/<uname>/<purpose>',methods = ['POST','GET'])
def change(uname,purpose):
    if request.method == 'POST':
        try:
            rollno = request.form["rollno"]
            grade = request.form["grade"]
            subgp = request.form["subgp"]
            with sql.connect("teacher.db") as con :
                con.row_factory = sql.Row
                cur = con.cursor()
                cur.execute("SELECT * FROM teacher_information WHERE username  = ?",(uname,) )
                row = cur.fetchone()

                coursecode = row["course_code"]
                semester = row["semester"]
                year = row["year"]
                trade = row["trade"]
                #department = row["department"]
 
                if trade == "B.Tech" :
                    syear = year - (semester//2)
                    srollno = syear % 100
                    rno = str(rollno)
                    sroll = ( int(rno[0])*10 + int(rno[1]) )
                    dbase = "B" + str(sroll) + ".db"
                elif trade == "B.Arch" :
                    dbase = "x.db"
                elif trade == "M.Tech":
                    dbase == "x.db"
                elif trade == "M.Sc":
                    dbase = "x.db"
                elif trade == "MBA":
                    dbase = "x.db"


                if srollno == sroll :
                    with sql.connect(dbase) as conn :
                        conn.row_factory = sql.Row
                        curr = conn.cursor()
                        Rollsem = str(rollno) + "S" + str(semester)
                        if purpose == "Upload" :
                            query = "INSERT INTO Result "+ " (Rollsem,Code,Grade,Sub_GP) VALUES(?,?,?,?)"
                            curr.execute(query,(Rollsem,coursecode,grade,subgp))
                            conn.commit()
                            return render_template("uploaded.html",uname = uname,purpose = purpose) 
                        else:
                            query = "UPDATE Result " + " SET Grade=" + '"' + grade + '"' + ", Sub_GP="  + str(subgp) + " WHERE Code=" + '"' +  coursecode + '"' + " and Rollsem = " +  "'" + Rollsem + "'"
                            curr.execute(query)
                            conn.commit()
                            return render_template("uploaded.html",uname = uname,purpose = purpose)
                else :
                    flash("Access Denied")
                    return render_template("resupdate.html",uname = uname,purpose = purpose)
        except:
            con.rollback()
            flash("Something went wrong !")
            return render_template("resupdate.html", uname = uname, purpose = purpose)

@app.route('/back/<uname>/<purpose>')
def back(uname,purpose):
    return render_template("resupdate.html",uname = uname,purpose = purpose)
                    


@app.route("/changepassword/<uname>")
def changepassword(uname):
    return render_template("cpwd.html",uname = uname)

@app.route('/personalinformation/<uname>')
def personalinformation(uname):
    try :
        with sql.connect("teacher.db") as con :
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM teacher_information WHERE username = ?",(uname,) )
            rows = cur.fetchall()
            return render_template("t_info.html", rows = rows, uname = uname)
    except:
        con.rollback()
        flash("Something went wrong !")
        return render_template("toptions.html",uname = uname)

@app.route('/cpwd/<uname>',methods = ['POST','GET'])
def cpwd(uname):
    if request.method == 'POST' :
        try :
            npwd = request.form["npwd"]
            cnpwd = request.form["cnpwd"]
            if npwd == cnpwd :
                with sql.connect("teacher.db") as con :
                    cur = con.cursor() 
                    cur.execute("UPDATE teacher_information SET password = ? WHERE username = ?",(npwd,uname) )
                    con.commit()
                    return render_template("pwdchanged.html",uname = uname)
            else :
                flash("Password didnt match !")
                return render_template("cpwd.html",uname = uname)
        except :
            flash("Something went wrong !")
            return render_template("cpwd.html",uname = uname)



if __name__ == '__main__' :
    app.run(debug=True)