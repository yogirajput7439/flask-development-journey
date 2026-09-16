# FOR ISNERT THE VALUES OF THE SQL TABLE

from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route("/add-user", methods=["GET", "POST"])
def add_user():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        age = request.form.get("age")

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
            (name, email, age)
        )

        conn.commit()
        conn.close()


        return "User added successfulyy..."

    return render_template("user.html")
