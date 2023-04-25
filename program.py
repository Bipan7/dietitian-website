"""
import pandas as pd


def calculate_calories(gender, weight, height, age, activity_level):
    calories = 0
    if gender == 0:

        calories = 88.362 + (13.397 * float(weight)) + (4.799 * float(height)) - (5.677 * int(age))
    elif gender == 1:

        calories = 447.593 + (9.247 * float(weight)) + (3.098 * float(height)) - (4.330 * int(age))

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

    print(calories)
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
            print(breakfast_plan)
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
            lunch_plan[row["name"]] = row["Serving Weight 1 (g)"]
            print(lunch_plan)
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
            print(dinner_plan)
            break

    # returning diet plan
    #return {"Breakfast": breakfast_plan, "Lunch": lunch_plan, "Dinner": dinner_plan}





g = int(input("enter the gender Male or Female"))
w = float(input("enter the weight"))
h = float(input("enter the height"))
a = int(input("enter the age"))
al = int(input("enter the activity level"))
calculate_calories(g, w, h, a, al)

"""
"""
import pandas as pd

def test():
    calories = 2000

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
            print(breakfast_plan)
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
            lunch_plan[row["name"]] = row["Serving Weight 1 (g)"]
            print(lunch_plan)
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
            print(dinner_plan)
            break

test()
"""
import math
def calculate_DCN(gender, weight, height, age, activity_level):
    if gender == 'male':
        DCN = (10 * weight) + (6.25 * height) - (5 * age) + 5
    elif gender == 'female':
        DCN = (10 * weight) + (6.25 * height) - (5 * age) - 161

    if activity_level == 'sedentary':
        DCN *= 1.2
    elif activity_level == 'lightly active':
        DCN *= 1.375
    elif activity_level == 'moderately active':
        DCN *= 1.55
    elif activity_level == 'very active':
        DCN *= 1.725
    elif activity_level == 'extra active':
        DCN *= 1.9

    return DCN

def calculate_BMR(gender, weight, height, age):
    if gender == 'male':
        BMR = (10 * weight) + (6.25 * height) - (5 * age) + 5
    elif gender == 'female':
        BMR = (10 * weight) + (6.25 * height) - (5 * age) - 161

    return BMR

def calculate_BFP(gender, waist, neck, height):
    if gender == 'male':
        BFP = 495 / (1.0324 - 0.19077 * math.log10(waist - neck) + 0.15456 * math.log10(height)) - 450
    elif gender == 'female':
        BFP = 495 / (1.29579 - 0.35004 * math.log10(waist - neck) + 0.22100 * math.log10(height)) - 450

    return BFP

# Example usage
gender = 'male'
weight = 70 # kg
height = 170 # cm
age = 25
activity_level = 'lightly active'
waist = 80 # cm
neck = 35 # cm

DCN = calculate_DCN(gender, weight, height, age, activity_level)
BMR = calculate_BMR(gender, weight, height, age)
BFP = calculate_BFP(gender, waist, neck, height)

print("Daily Calorie Needs (DCN): {} kcal".format(round(DCN)))
print("Basal Metabolic Rate (BMR): {} kcal".format(round(BMR)))
print("Body Fat Percentage (BFP): {}%".format(round(BFP, 2)))

import random

def generate_exercise_recommendation(age, fitness_level):
    # Create a list of exercise types
    exercise_types = ['running', 'cycling', 'swimming', 'yoga', 'strength training']

    # Create a dictionary of exercise duration ranges based on age and fitness level
    duration_ranges = {
        'beginner': {
            'child': (10, 20),
            'teen': (20, 30),
            'adult': (30, 45),
            'senior': (20, 30)
        },
        'intermediate': {
            'child': (20, 30),
            'teen': (30, 45),
            'adult': (45, 60),
            'senior': (30, 45)
        },
        'advanced': {
            'child': (30, 45),
            'teen': (45, 60),
            'adult': (60, 75),
            'senior': (45, 60)
        }
    }

    # Determine the exercise duration range based on age and fitness level
    if age <= 12:
        age_group = 'child'
    elif age <= 18:
        age_group = 'teen'
    elif age <= 65:
        age_group = 'adult'
    else:
        age_group = 'senior'

    if fitness_level == 'beginner':
        duration_range = duration_ranges['beginner'][age_group]
    elif fitness_level == 'intermediate':
        duration_range = duration_ranges['intermediate'][age_group]
    else:
        duration_range = duration_ranges['advanced'][age_group]

    # Generate a random duration within the range
    duration = random.randint(duration_range[0], duration_range[1])

    # Select a random exercise type
    exercise_type = random.choice(exercise_types)

    # Return the recommendation as a string
    return "We recommend {} for {} minutes.".format(exercise_type, duration)

# Example usage
age = 30
fitness_level = 'intermediate'

recommendation = generate_exercise_recommendation(age, fitness_level)

print(recommendation)
