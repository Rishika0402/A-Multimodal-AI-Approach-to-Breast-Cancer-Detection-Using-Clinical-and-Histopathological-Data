from flask import Flask, render_template_string, redirect
import subprocess
import threading
import webbrowser

app = Flask(__name__)

def run_app_py():
    subprocess.Popen(["python", "app.py"])

def run_my_app_py():
    subprocess.Popen(["python", "My_App.py"])

landing_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Breast Cancer Detection</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(to right, #ffe6f0, #ffd6eb);
            color: #333;
        }
        header {
            background-color: #ff99cc;
            padding: 30px 20px;
            text-align: center;
            color: white;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
        header h1 {
            font-size: 3em;
            margin: 0;
        }
        header p {
            font-size: 1.2em;
            margin-top: 10px;
        }
        .container {
            text-align: center;
            margin-top: 40px;
        }
        .btn {
            background-color: #ff66b2;
            color: white;
            border: none;
            padding: 15px 35px;
            margin: 20px;
            font-size: 1.1em;
            border-radius: 10px;
            cursor: pointer;
            transition: 0.3s;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        }
        .btn:hover {
            background-color: #e60073;
            transform: scale(1.05);
        }
        .info-section {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            margin: 60px 20px;
        }
        .card {
            background: white;
            border-radius: 12px;
            padding: 25px;
            box-shadow: 0 6px 15px rgba(0,0,0,0.1);
            width: 300px;
            margin: 20px;
        }
        .card h3 {
            color: #cc0066;
        }
        .card p {
            font-size: 0.95em;
            color: #555;
        }
        footer {
            background: #ffe6f0;
            padding: 20px;
            text-align: center;
            color: #888;
            font-size: 0.9em;
        }
        img.ribbon {
            width: 50px;
            margin-right: 10px;
            vertical-align: middle;
        }
    </style>
</head>
<body>
    <header>
        <h1><img src="https://images.squarespace-cdn.com/content/v1/5e223cac4610b208610b2989/1590182936929-62O0K386DL18FTUATTCI/Pink-Ribbon.jpg" class="ribbon"> Breast Cancer Detection Portal</h1>
        <p>Empowering early diagnosis with technology 💻</p>
    </header>

    <div class="container">
        <form action="/launch_app">
            <button class="btn">🔢 Predict using Numerical Data</button>
        </form>
        <form action="/launch_my_app">
            <button class="btn">🖼️ Predict using Image Detection</button>
        </form>
    </div>

    <div class="info-section">
        <div class="card">
            <h3>What is Breast Cancer?</h3>
            <p>Breast cancer is a disease in which cells in the breast grow out of control. It can occur in women and rarely in men. Early detection increases survival chances.</p>
        </div>
        <div class="card">
            <h3>Why Early Detection?</h3>
            <p>Detecting cancer early can reduce treatment costs and increase recovery rates. Our models aim to assist medical professionals in timely diagnosis.</p>
        </div>
        <div class="card">
            <h3>About This Project</h3>
            <p>This project uses ML and DL to classify breast cancer using both medical data and histopathology images. Built using Flask, TensorFlow & Scikit-learn.</p>
        </div>
    </div>

    <footer>
        Made with ❤️ by Team DetectHER | Final Year Project 2025
    </footer>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(landing_html)

@app.route('/launch_app')
def launch_app():
    threading.Thread(target=run_app_py).start()
    return redirect("http://127.0.0.1:5000")

@app.route('/launch_my_app')
def launch_my_app():
    threading.Thread(target=run_my_app_py).start()
    return redirect("http://127.0.0.1:5001")

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:8000")
    app.run(port=8000)
