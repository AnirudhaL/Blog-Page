from flask import Flask, render_template, redirect, url_for, request
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect( # ------------------------------------SQL----------------------------- #
    host='localhost',
    user='Anirudha',
    password='password123',
    database='blog'
)
mycursor= mydb.cursor()
sqlFormula = "INSERT INTO posts (name, content) VALUES(%s, %s)"

@app.route("/", methods=["POST", "GET"]) # ---------------------------ROUTE-----------------------------------#
def home():
    if request.method == "POST":
        big = request.form["big"]
        small = request.form["small"].upper()
        a = (small, big)
        if big !=  "" and small!= "":
            mycursor.execute(sqlFormula, a)
            mydb.commit()
            return redirect(url_for("user",small=small))
        else:
            mycursor.execute("SELECT * FROM posts")
            myresult = mycursor.fetchall() 
            return render_template("sub1.html", posts=myresult)
    else:
        mycursor.execute("SELECT * FROM posts")
        myresult = mycursor.fetchall() 
        return render_template("sub1.html", posts=myresult)

@app.route("/<small>", methods=["POST", "GET"])
def user(small):    
    if request.method == "POST":
        big = request.form["big"]
        small = request.form["small"].upper()
        a = (small, big)
        
        mycursor.execute(sqlFormula, a)
        mydb.commit()
        mycursor.execute("SELECT * FROM posts")
        myresult = mycursor.fetchall() 
        return render_template("sub1.html", posts=myresult)
    else:
        mycursor.execute("SELECT * FROM posts")
        myresult = mycursor.fetchall() 
        return render_template("sub1.html", posts=myresult)

if __name__ == "__main__":
    app.run(debug=True)