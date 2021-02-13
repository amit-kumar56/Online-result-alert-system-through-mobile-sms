from flask import Flask,render_template,request,redirect,url_for,flash
import sqlite3 as sql
app = Flask(__name__)
app.secret_key = "abc"

@app.route("/")
def home():
    return render_template('main.html')

@app.route('/getresults')
def getresults():
    return render_template('getresults.htm') 

@app.route("/btech")
def btech():
    return render_template('sloginbtech.html', branch = "B" )

@app.route("/sloginbtech/<branch>", methods = ['POST','GET'])
def sloginbtechp(branch) :
    if request.method == 'POST' :
        try :
            rollno = request.form["rollno"]
            rno = str(rollno)
            sroll = ( int(rno[0])*10 + int(rno[1]) )
            dbase = branch + str(sroll) + ".db"
            with sql.connect(dbase) as con :
                con.row_factory = sql.Row
                cur = con.cursor()
                cur.execute("SELECT * FROM Student_info WHERE Roll_no = ?",(rollno,))
                sinfo = cur.fetchall()
                
                rnstring = str(rollno)

                query = "SELECT * FROM  Total "  + "WHERE Rollno = " + rnstring 
                cur.execute(query)
                rows = cur.fetchall()
                
                s1=0
                c1=0
                s2=0
                c2=0
                s3=0
                c3=0
                s4=0
                c4=0
                s5=0
                c5=0
                s6=0
                c6=0
                s7=0
                c7=0
                s8=0
                c8=0


                query1 = "SELECT * FROM  Syllabus INNER JOIN  Result ON Syllabus.Code = Result.Code WHERE Result.Rollsem = " + "'" + rnstring + "S1" + "'"
                cur.execute(query1)
                rows1 = cur.fetchall()
                len1 = len(rows1)
                if len1 :
                    s1 = rows[0][1]
                    c1 = rows[0][2]
                
                query2 = "SELECT * FROM  Syllabus INNER JOIN  Result ON Syllabus.Code = Result.Code WHERE Result.Rollsem = " + "'" + rnstring + "S2" + "'"
                cur.execute(query2)
                rows2 = cur.fetchall()
                len2 = len(rows2)
                if len2 :
                    s2 = rows[0][3]
                    c2 = rows[0][4]

                query3 = "SELECT * FROM  Syllabus INNER JOIN  Result ON Syllabus.Code = Result.Code WHERE Result.Rollsem = " + "'" + rnstring + "S3" + "'"
                cur.execute(query3)
                rows3 = cur.fetchall()
                len3 = len(rows3)
                if len3 :
                    s3 = rows[0][5]
                    c3 = rows[0][6]

                query4 = "SELECT * FROM  Syllabus INNER JOIN  Result ON Syllabus.Code = Result.Code WHERE Result.Rollsem = " + "'" + rnstring + "S4" + "'"
                cur.execute(query4)
                rows4 = cur.fetchall()
                len4 = len(rows4)
                if len4 :
                    s4 = rows[0][7]
                    c4 = rows[0][8]

                query5 = "SELECT * FROM  Syllabus INNER JOIN  Result ON Syllabus.Code = Result.Code WHERE Result.Rollsem = " + "'" + rnstring + "S5" + "'"
                cur.execute(query5)
                rows5 = cur.fetchall()
                len5 = len(rows5)
                if len5 :
                    s5 = rows[0][9]
                    c5 = rows[0][10]

                query6 = "SELECT * FROM  Syllabus INNER JOIN  Result ON Syllabus.Code = Result.Code WHERE Result.Rollsem = " + "'" + rnstring + "S6" + "'"  
                cur.execute(query6)
                rows6 = cur.fetchall()
                len6 = len(rows6)
                if len6 :
                    s6 = rows[0][11]
                    c6 = rows[0][12]

                query7 = "SELECT * FROM  Syllabus INNER JOIN  Result ON Syllabus.Code = Result.Code WHERE Result.Rollsem = " + "'" + rnstring + "S7" + "'"
                cur.execute(query7)
                rows7 = cur.fetchall()
                len7 = len(rows7)
                if len7 :
                    s7 = rows[0][13]
                    c7 = rows[0][14]

                query8 = "SELECT * FROM  Syllabus INNER JOIN  Result ON Syllabus.Code = Result.Code WHERE Result.Rollsem = " + "'" + rnstring + "S8" + "'"
                cur.execute(query8)
                rows8 = cur.fetchall()
                len8 = len(rows8)
                if len8 :
                    s8 = rows[0][15]
                    c8 = rows[0][16]
                    

                return render_template("sres.html",rows = rows,sinfo = sinfo,rows1 = rows1,rows2 = rows2,rows3 = rows3,rows4 = rows4,rows5 = rows5,rows6 = rows6,rows7 = rows7,rows8 = rows8,len1 = len1,len2 = len2,len3 = len3,len4 = len4,len5 = len5,len6 = len6,len7 = len7,len8 = len8,s1 = s1,c1 = c1,s2 = s2,c2 = c2,s3 = s3,c3 = c3,s4 = s4,c4 = c4,s5 = s5,c5 = c5,s6 = s6,c6 = c6,s7 = s7,c7 = c7,s8 = s8,c8 = c8)

        except :
            
            con.rollback()
            flash("Something went wrong !!")
            return redirect(url_for('btech'))

            

@app.route("/barch")
def barch():
    return render_template('sloginbtech.html',branch = "BA")


@app.route("/mba")
def mba():
    return render_template('sloginbtech.html',branch = "MBA")

@app.route("/mt")
def mt():
    return render_template('sloginbtech.html',branch = "MT")

@app.route("/ms")
def ms():
    return render_template('sloginbtech.html',branch = "MS")

if __name__ == '__main__':
    app.run(debug = True)
