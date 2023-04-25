"""from flask import Flask, jsonify, request, render_template
import pandas as pd

app = Flask(__name__)

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

    # recommending breakfast
    breakfast_plan = {}
    for index, row in breakfast.iterrows():
        if int(row["Protein (g)"]) == protein_req:
            breakfast_plan[row["name"]] = row["Serving Weight 1 (g)"]
            fat_req -= int(row["Fat (g)"])
            carb_req -= int(row["Carbohydrate (g)"])
            break
    for index, row in breakfast.iterrows():
        if int(row["Fat (g)"]) == fat_req:
            breakfast_plan[row["name"]] = row["Serving Weight 1 (g)"]
            carb_req -= int(row["Carbohydrate (g)"])
            break
    for index, row in breakfast.iterrows():
        if int(row["Carbohydrate (g)"]) == carb_req:
            breakfast_plan[row["name"]] = row["Serving Weight 1 (g)"]
            break

    # recommending lunch
    lunch_plan = {}
    for index, row in lunch.iterrows():
        if int(row["Protein (g)"]) == protein_req:
            lunch_plan[row["name"]] = row["Serving Weight 1 (g)"]
            fat_req -= int(row["Fat (g)"])
            carb_req -= int(row["Carbohydrate (g)"])
            break
    for index, row in lunch.iterrows():
        if int(row["Fat (g)"]) == fat_req:
            lunch_plan[row["name"]] = row["Serving Weight 1 (g)"]
            carb_req -= int(row["Carbohydrate (g)"])
            break
    for index, row in lunch.iterrows():
        if int(row["Carbohydrate (g)"]) == carb_req:
            lunch_plan[row["name"]]= row["Serving Weight 1 (g)"]
            break

    # recommending dinner
    dinner_plan = {}
    for index, row in dinner.iterrows():
        if int(row["Protein (g)"]) == protein_req:
            dinner_plan[row["name"]] = row["Serving Weight 1 (g)"]
            fat_req -= int(row["Fat (g)"])
            carb_req -= int(row["Carbohydrate (g)"])
            break
    for index, row in dinner.iterrows():
        if int(row["Fat (g)"]) == fat_req:
            dinner_plan[row["name"]] = row["Serving Weight 1 (g)"]
            carb_req -= int(row["Carbohydrate (g)"])
            break
    for index, row in dinner.iterrows():
        if int(row["Carbohydrate (g)"]) == carb_req:
            dinner_plan[row["name"]] = row["Serving Weight 1 (g)"]
            break

    # creating diet plan
    diet_plan = {"Breakfast": breakfast_plan, "Lunch": lunch_plan, "Dinner": dinner_plan}

    return diet_plan


@app.route("/calculate", methods=["POST"])
def calculate():
    gender = request.json["gender"]
    weight = request.json["weight"]
    height = request.json["height"]
    age = request.json["age"]
    activity_level = request.json["activity_level"]
    diet_plan = recommend_diet_plan(gender, weight, height, age, activity_level)
    return jsonify(diet_plan)

@app.route('/')
def index():
    return render_template('diet_plan.html')


app.run(debug=True)


"""







"""
from flask import Flask, jsonify, request, render_template
import pandas as pd
import random

app = Flask(__name__)

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

import requests

@app.route('/diet')
def diet():
    # generating random values
    gender = random.randint(0, 1)
    weight = random.randint(50, 150)
    height = random.randint(150, 200)
    age = random.randint(18, 50)
    activity_level = random.randint(1, 5)

    # send the data to ChatGPT to get output
    response = requests.post('https://api.openai.com/v1/engines/davinci-codex/completions',
                             headers={'Authorization': 'Bearer YOUR_API_KEY',
                                      'Content-Type': 'application/json'},
                             json={'prompt': f"Generate a diet plan for a {gender} who weighs {weight} kg, is {height} cm tall, {age} years old, and has an activity level of {activity_level}.",
                                   'max_tokens': 1024,
                                   'temperature': 0.5,
                                   'n': 1,
                                   'stop': '.\n\n'})

    # parse the response and get the output text
    output_text = response.json()['choices'][0]['text'].strip()

    # combine the output text with the input data
    result = {'gender': gender, 'weight': weight, 'height': height, 'age': age, 'activity_level': activity_level, 'output_text': output_text}

    return jsonify(result)



@app.route('/')
def diet1():
    return render_template('diet_plan.html')
if __name__ == '__main__':
    app.run()
"""



import openai
from flask import Flask, render_template, request

openai.api_key = "YOUR_API_KEY"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate_plan', methods=['GET', 'POST'])
def generate_plan():
    if request.method == 'POST':
        gender = request.form['gender']
        age = request.form['age']
        weight = request.form['weight']
        height = request.form['height']
        activity_level = request.form['activity_level']
        goal = request.form['goal']
        # You can add more inputs as required

        # Generate the diet plan using ChatGPT
        prompt = f"Generate a diet plan for a {gender} who is {age} years old, weighs {weight} kgs, is {height} cm tall, has an activity level of {activity_level}, and wants to {goal}."
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        diet_plan = response.choices[0].text.strip()

        return render_template('result.html', diet_plan=diet_plan)
    else:
        return render_template('input.html')

if __name__ == '__main__':
    app.run(debug=True)
