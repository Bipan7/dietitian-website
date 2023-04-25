from flask import Flask, jsonify, request, render_template
import pandas as pd
import math

app = Flask(__name__)
"""
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


@app.route('/')
def index():
    return render_template('api.html')


app.run(debug=True)

"""




@app.route('/recommend-exercises', methods=['POST'])
def recommend_exercises():
    data = request.get_json()
    height = data['height']
    weight = data['weight']
    age = data['age']

    # Load the exercises from the CSV file
    exercises_df = pd.read_csv('EXERCISE_DB.csv')

    # Filter the exercises based on the user's height, weight, and age
    filtered_df = exercises_df[(exercises_df['height'] == height) &
                               (exercises_df['weight'] == weight) &
                               (exercises_df['age'] == age)]

    # Select the top 3 exercises
    recommended_exercises = filtered_df['exercise'].head(3).tolist()

    # Return the recommended exercises as a JSON response
    response = {'exercises': recommended_exercises}
    return jsonify(response)


@app.route('/')
def index():
    return render_template('exercise.html')


app.run(debug=True)
