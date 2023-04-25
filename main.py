from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the exercise data from CSV file
exercise_data = pd.read_csv('EXERCISE_DB.csv')


@app.route('/')
def index():
    return render_template('exercise.html')


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


if __name__ == '__main__':
    app.run(debug=True)
