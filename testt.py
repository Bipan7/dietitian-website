from flask import Flask, render_template, request, redirect, session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'bipan'

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'nutrigenie'
mysql = MySQL(app)

# Login route
@app.route('/member')
def member_login():
    return render_template('member_login.html')
@app.route('/')
def landing():
    return render_template('landing_page.html')

# Authentication route
@app.route('/auth', methods=['POST'])
def auth():
    # Get form data
    email = request.form['email']
    password = request.form['password']

    # Check if user exists in database
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM sign WHERE email = %s AND password = %s", (email, password))
    email = cur.fetchone()
    cur.close()

    if email:
        # Store user ID in session
        session['user_id'] = email[0]
        return redirect('/home')
    else:
        return render_template('error.html')


@app.route('/home')
def home():
    # Check if user is logged in
    if 'user_id' in session:
        # Get user data from database
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM sign WHERE email = %s", (session['user_id'],))
        name = cur.fetchone()
        cur.close()

        return render_template('index.html', email=name)
    else:
        return redirect('/member')

# Logout route
@app.route('/logout1')
def logout1():
    # Remove user ID from session
    session.pop('email', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

