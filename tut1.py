from flask import Flask, render_template, request, jsonify, session, redirect
from flask_sqlalchemy import SQLAlchemy
from _datetime import datetime
import math
import pandas as pd
from flask_mysqldb import MySQL
#from flask_mail import Mail
import random

#app = Flask(__name__)
#app.config.update(
#    MAIL_SERVER='smtp.gmail.com',
#   MAIL_PORT='465',
#   MAIL_USE_SSL=True,
#   MAIL_USERNAME="teamexousia1@gmail.com",
#   MAIL_PASSWORD="uilnkuubdeuqzyvh"

#)
#mail = Mail(app)

app = Flask(__name__)
app.secret_key = 'bipan'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/nutrigenie'
db = SQLAlchemy(app)


class Feedback(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(15), nullable=False)
    last_name = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    message = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(12), nullable=True)


class Sign(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(6), nullable=False)


@app.route("/sign", methods=['GET', 'POST'])
def sign():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        entry1 = Sign(name=name, email=email, password=password)
        db.session.add(entry1)
        db.session.commit()
        return render_template('index.html')
    return render_template('sign_up.html')


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


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/feedback", methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        message = request.form.get('message')
        entry = Feedback(first_name=first_name, last_name=last_name, email=email, message=message, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        #mail.send_message("New message from " + first_name, sender="email", recipients="teamexousia1@gmail.com",
                          #body="message")

    return render_template('feedback.html')


@app.route('/logout')
def logout():
    if "username" in session and session['username'] == 'bipan':
        session.pop("username")
    return redirect('/')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if "username" in session and session['username'] == 'bipan':
        sign = Sign.querry.all()
        return render_template("dashboard.html", sign=sign)

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'bipan' and password == 'tiwari':
            sign = Sign.query.all()
            feedback = Feedback.query.all()
            return render_template("dashboard.html", sign=sign, feedback=feedback)
        else:
            return render_template('error.html')
    return render_template('login.html')


@app.route('/error')
def error():
    return render_template('error.html')


#@app.route('/dashboard')
#def dash():
 #   return render_template('dashboard.html')


@app.route('/reports', methods=['POST'])
def reports():
    data = request.get_json()
    gender = int(data['gender'])
    weight = float(data['weight'])
    height = float(data['height'])
    age = int(data['age'])
    activity_level = int(data['activity_level'])
    waist = float(data['waist'])
    neck = float(data['neck'])

    DCN = calculate_DCN(gender, weight, height, age, activity_level)
    BMR = calculate_BMR(gender, weight, height, age)
    BFP = calculate_BFP(gender, waist, neck, height)

    response = {
        'DCN': round(DCN),
        'BMR': round(BMR),
        'BFP': round(BFP, 2)
    }

    return jsonify(response)


def calculate_DCN(gender, weight, height, age, activity_level):
    if gender == 0:
        DCN = (10 * weight) + (6.25 * height) - (5 * age) + 5
    elif gender == 1:
        DCN = (10 * weight) + (6.25 * height) - (5 * age) - 161

    if activity_level == 1:
        DCN *= 1.2
    elif activity_level == 2:
        DCN *= 1.375
    elif activity_level == 3:
        DCN *= 1.55
    elif activity_level == 4:
        DCN *= 1.725
    elif activity_level == 5:
        DCN *= 1.9

    return DCN


def calculate_BMR(gender, weight, height, age):
    if gender == 0:
        BMR = (10 * weight) + (6.25 * height) - (5 * age) + 5
    elif gender == 1:
        BMR = (10 * weight) + (6.25 * height) - (5 * age) - 161

    return BMR


def calculate_BFP(gender, waist, neck, height):
    if gender == 0:
        BFP = 495 / (1.0324 - 0.19077 * math.log10(waist - neck) + 0.15456 * math.log10(height)) - 450
    elif gender == 1:
        BFP = 495 / (1.29579 - 0.35004 * math.log10(waist + neck - height)) - 450

    return BFP


@app.route('/health')
def health():
    return render_template('health.html')


@app.route('/exercise')
def exercise():
    return render_template('exercise.html')


exercise_data = pd.read_csv('EXERCISE_DB.csv')


@app.route('/recommend', methods=['POST'])
def recommend():
    # Get user input from form
    gender = request.form['gender']
    age = int(request.form['age'])
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    calories = int(request.form['calories'])

    # Filter the exercise data based on user input
    filtered_data = exercise_data[
        (exercise_data['CALORIES_PR_MIN'] >= calories) &
        (exercise_data['TOTAL_SET'] >= 3) &
        (exercise_data['REPETITIONS'] >= 10)
        ].sample(5)

    # Convert the filtered data to a JSON object and return it
    return jsonify(filtered_data.to_dict(orient='records'))


@app.route("/delete/<string:sno>", methods=['GET', 'POST'])
def delete(sno):
    if "username" in session and session['username'] == 'bipan':
        feedback = Feedback.query.filter_by(sno=sno).first()
        db.session.delete(feedback)
        db.session.commit()
    return redirect("/login")


def calculate_calories(gender, weight, height, age, activity_level):
    calories = 0
    if gender == 0: #male
        calories = 88.362 + (5.677 * float(weight)) + (4.799 * float(height)) - (5.677 * int(age))
    elif gender == 1:   #female
        calories = 447.593 + (4.330 * float(weight)) + (3.098 * float(height)) - (4.330 * int(age))

    if activity_level == 1:
        calories = calories * 1.2
    elif activity_level == 2:
        calories = calories * 1.375
    elif activity_level == 3:
        calories = calories * 1.55
    elif activity_level == 4:
        calories = calories * 1.725
    elif activity_level == 5:
        calories = calories * 1.9

    return calories


def recommend_diet_plan(gender, weight, height, age, activity_level):
    calories = calculate_calories(gender, weight, height, age, activity_level)

    # calculating macronutrient requirements
    protein_req = (calories * 0.3) // 4
    carb_req = (calories * 0.5) // 4
    fat_req = (calories * 0.2) // 9

    # reading food datasets
    breakfast = pd.read_csv("breakfast_dataset.csv")
    lunch = pd.read_csv("lunch_dataset.csv")
    dinner = pd.read_csv("dinner_dataset.csv")

    # selecting random food items for each meal
    breakfast_item = breakfast.sample().reset_index(drop=True)
    lunch_item = lunch.sample().reset_index(drop=True)
    dinner_item = dinner.sample().reset_index(drop=True)

    # creating diet plan
    diet_plan = {
        "calories": calories,
        "protein": protein_req,
        "carbohydrates": carb_req,
        "fat": fat_req,
        "breakfast": breakfast_item.to_dict(orient='records'),
        "lunch": lunch_item.to_dict(orient='records'),
        "dinner": dinner_item.to_dict(orient='records')
    }

    return diet_plan


@app.route('/diet')
def diet():
    # generating random values
    gender = random.randint(0, 1)
    weight = random.randint(50, 150)
    height = random.randint(150, 200)
    age = random.randint(18, 50)
    activity_level = random.randint(1, 5)

    # recommending diet plan
    diet_plan = recommend_diet_plan(gender, weight, height, age, activity_level)

    return jsonify(diet_plan)

@app.route('/diet_plan')
def diet_plan():
    return render_template('diet_plan.html')


app.run(debug=True)
