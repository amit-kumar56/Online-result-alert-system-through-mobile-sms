from twilio.rest import Client
import sqlite3 as sql
client = Client("AC7a3fa82dcbd82f7a861ea0cc4222366f","979c0607a0925a50fcf6b8f25f429b12")
with sql.connect("B17.db") as con :
    con.row_factory = sql.Row
    cur = con.cursor()
    qstring = "SELECT * FROM Total"
    cur.execute(qstring)
    rec = cur.fetchall()
    query = "SELECT * FROM Student_info"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rec :
        rollno = row["Rollno"]
        body = "Result Declared.Visit website for more details."
        for r in rows :
            if r["Roll_no"] == rollno :
                mob = "+91" + r["Mobile_no"]
                for sem in range(1,9) :
                    sg = "S" + str(sem) 
                    cg = "C" + str(sem)
                    if row[sg] : 
                        body += (sg + " : " + str(row[sg]) + "  ")
                    if row[cg] :
                        body += (cg + " : " + str(row[cg]) + " | " )
                client.messages.create(to = mob , from_ = "+12015845617" , body = body)