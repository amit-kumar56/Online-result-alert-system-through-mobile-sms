from flask import Flask,render_template,request,redirect,url_for,flash
import sqlite3 as sql
import xlrd
app = Flask(__name__)


book = xlrd.open_workbook("pytest.xlsx")
sheet = book.sheet_by_name("Sheet1")

with sql.connect("teacher.db") as con :
            con.row_factory = sql.Row
            cur = con.cursor()
            cur.execute("SELECT * FROM teacher_information WHERE username = ?",(uname,) )
            rows = cur.fetchall()
            cd=rows[0][4]
            sem=rows[0][5]
            con.close()
            with sql.connect("B17.db") as con :
                con.row_factory = sql.Row
                cur = con.cursor()    
                query = "INSERT INTO result (Rollsem,Code,Grade,Sub_GP) VALUES (%s, %s, %s, %s)"
                for r in range(2, sheet.nrows):
                    Rollsem=str(sheet.cell(r,1).value)+"S"+str(sem)
                    Code=cd
                    Grade=sheet.cell(r,2).value
                    Sub_GP=sheet.cell(r,3).value
                    values=(Rollsem,Code,Grade,Sub_GP)
                    cur.execute(query, values)
                con.commit()    
                con.close()  
  

print ("")
print ("All Done! Bye, for now.")
print ("")
columns = str(sheet.ncols)
rows = str(sheet.nrows)
