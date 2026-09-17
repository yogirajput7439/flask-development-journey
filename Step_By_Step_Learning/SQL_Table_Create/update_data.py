# INSERT THE VALUES IN THE TABLE OF NEW USERS

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

        return "User added successfully..."

    return render_template("user.html")


# UPDATE THE DATA OF THE PREVIES USERS


@app.route("/users")
def users():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")

    users = cursor.fetchall()

    conn.close()

    return render_template("users.html", users=users)

@app.route("/edit-users/<int:id>", methods = ["GET", "POST"])

def edit_user(id):

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    if request.method == "POST":

        name = request.form.get("name")
        email  = request.form.get("email")
        age = request.form.get("age")


        cursor.execute("""
            UPDATE users
            SET name = ?, email = ?, age = ? 
            WHERE id = ?
            """,
            (name, email, age, id)
        )

        conn.commit()
        conn.close()

        return "user update successfully..."

    cursor.execute(
        "SELECT * FROM users WHERE id = ?",
        (id,)
    )

    user = cursor.fetchone()

    conn.close()

    return render_template("edit_user.html", user = user)
