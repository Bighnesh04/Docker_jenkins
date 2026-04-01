# CHANGED: added HTML UI
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Student Dashboard</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(to right, #667eea, #764ba2);
                color: white;
                text-align: center;
            }
            .container {
                margin-top: 100px;
            }
            .card {
                background: white;
                color: #333;
                padding: 30px;
                border-radius: 15px;
                width: 300px;
                margin: auto;
                box-shadow: 0px 10px 25px rgba(0,0,0,0.2);
            }
            h1 {
                margin-bottom: 20px;
            }
            .btn {
                background: #667eea;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 8px;
                cursor: pointer;
            }
            .btn:hover {
                background: #5a67d8;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Student Dashboard</h1>
            <div class="card">
                <h2>Flask App Running</h2>
                <p>Status: ✅ Active</p>
                <button class="btn">Explore</button>
            </div>
        </div>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
