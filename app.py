# CHANGED: Proper structure + DB + UI

from flask import Flask, render_template_string, request
import mysql.connector

app = Flask(__name__)

# DB CONNECTION
def get_db_connection():
    return mysql.connector.connect(
        host="mysql-db",
        user="root",
        password="root123",
        database="studentdb"
    )

# HOME PAGE (UI)
@app.route("/")
def home():
    return render_template_string("""
    <html>
    <head>
        <title>Student Dashboard</title>
        <style>
            body {
                font-family: Arial;
                background: linear-gradient(to right, #667eea, #764ba2);
                color: white;
                text-align: center;
            }
            .card {
                background: white;
                color: black;
                padding: 20px;
                margin: 50px auto;
                width: 300px;
                border-radius: 10px;
            }
            input, button {
                padding: 10px;
                margin: 5px;
            }
        </style>
    </head>
    <body>
        <h1>🚀 Student Dashboard</h1>
        <div class="card">
            <form action="/add" method="post">
                <input type="text" name="name" placeholder="Enter Name" required>
                <button type="submit">Add Student</button>
            </form>
            <br>
            <a href="/data">View Data</a>
        </div>
    </body>
    </html>
    """)

# CREATE TABLE + INSERT
@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    conn = get_db_connection()
    cursor = conn.cursor()

    # create table if not exists
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100)
    )
    """)

    cursor.execute("INSERT INTO students (name) VALUES (%s)", (name,))
    conn.commit()

    return "Student Added! <br><a href='/'>Go Back</a>"

# VIEW DATA
@app.route("/data")
def data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    output = "<h2>Students List</h2>"
    for r in rows:
        output += f"{r[0]} - {r[1]}<br>"

    output += "<br><a href='/'>Go Back</a>"
    return output

# RUN APP
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
