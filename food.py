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
    breakfast = pd.read_csv("C:/Users/USER/Downloads/breakfast_dataset.csv")
    lunch = pd.read_csv("C:/Users/USER/Downloads/lunch_dataset.csv")
    dinner = pd.read_csv("C:/Users/USER/Downloads/dinner_dataset.csv")

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
    dic ={"Breakfast": breakfast_plan, "Lunch": lunch_plan, "Dinner": dinner_plan}
    print(dic)





g = int(input("enter the gender Male or Female : "))
w = float(input("enter the weight : "))
h = float(input("enter the height : "))
a = int(input("enter the age : "))
al = int(input("enter the activity level : "))
#calculate_calories(g, w, h, a, al)
recommend_diet_plan(g, w, h, a, al)