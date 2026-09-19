# Print the json data

from flask import Flask, render_templates, redirect, url_forl, request, sqlite3

@app.route("/api/users")
def api_users():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users",
        )
    
    users = cursor.fetchall()

    conn.close()

    user_data = []

    for user in users:

        user_data.append({
            "Id" : user[0],
            "Name" : user[1],
            "Email" : user[2],
            "Age" : user[3]
        })

    return user_data

    
