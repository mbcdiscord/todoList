from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="app"
    )

@app.route('/table')
def show_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM LIST")
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('table.html', tasks = tasks)

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()  
    cursor.execute("SELECT ID, TASK FROM list WHERE STATUS = 'incomplete'")
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO list (TASK) VALUES (%s)", (task,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')

@app.route('/dele/<int:id>', methods=['POST'])
def dele(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM list WHERE ID=%s",(id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')

@app.route('/complete/<int:id>')
def complete(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE list SET STATUS = 'complete' WHERE ID = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute('ALTER TABLE list AUTO_INCREMENT=1')
    cursor.close()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
