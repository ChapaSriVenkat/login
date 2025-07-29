from flask import Flask, request, redirect
import mysql.connector

app = Flask(__name__)

def connect_db():
    return mysql.connector.connect(
        host="34.230.255.114",
        user="root",
        password="Srii@773",
        database="html-login"
    )

@app.route('/')
def index():
    with open('../page/Index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    return html

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO data (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    conn.close()

    return "User added successfully! <a href='/'>Go Back</a>"

if __name__ == '__main__':
    app.run(debug=True)
