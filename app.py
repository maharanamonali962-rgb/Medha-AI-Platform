print("RUNNING NEW CODE")

from flask import Flask, render_template, request, session, redirect
import sqlite3

app = Flask(__name__)          
app.secret_key = "secret123"   

# 🏠 HOME
@app.route('/')
def home():
    return render_template('index.html')

# 📊 DASHBOARD
@app.route('/dashboard', methods=['POST'])
def dashboard():
    name = request.form.get('name') 
    goal = request.form.get('goal')

    if not name:
        name = "User"

    roadmap = """Step 1: Learn Basics
Step 2: Practice
Step 3: Build Projects"""

    return render_template('dashboard.html', name=name, roadmap=roadmap)

@app.route('/progress')
def progress():
    user = session.get('user')

    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT score FROM scores WHERE user=?", (user,))
    data = cur.fetchall()
    conn.close()

    scores = [row[0] for row in data]

    return render_template('progress.html', scores=scores)

# 🔐 REGISTER 
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO users(name,email,password) VALUES(?,?,?)",
                    (name, email, password))
        conn.commit()
        conn.close()

        return redirect('/login')

    return render_template('register.html')

# 🔐 LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        conn = sqlite3.connect('database.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE email=? AND password=?",
                    (email, password))
        user = cur.fetchone()
        conn.close()

        if user:
            session['user'] = user[1]
            return redirect('/')
        else:
            return "Invalid login"

    return render_template('login.html')

@app.route('/chat', methods=['POST'])
def chat():
    msg = request.form.get('message')

    if "ai" in msg.lower():
        reply = "AI is the simulation of human intelligence."
    elif "python" in msg.lower():
        reply = "Python is used for AI, web, and more."
    else:
        reply = "I am here to help you learn!"

    return {"reply": reply}

@app.route('/save_score', methods=['POST'])
def save_score():
    score = request.form.get('score')
    user = session.get('user')

    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO scores(user, score) VALUES(?,?)", (user, score))
    conn.commit()
    conn.close()

    return "Saved"

# 🔓 LOGOUT 
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

if __name__ == '__main__':
    app.run()