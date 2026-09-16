# CREATING THE TABLE IN SQL DATABASE

from flask import Flask

import sqlite3

app = Flask(__name__)


def create_table():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            age INTEGER
        )
    """)

    conn.commit()
    conn.close()

    print("Users table created successfully!")


if __name__ == "__main__":
    create_table()
    app.run(debug=True)
