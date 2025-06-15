import math

FOOD_DB = {
    "White Rice":        {"carb": 28.0, "protein": 2.7,  "fat": 0.3,  "kcal": 130},
    "Sweet Potato":      {"carb": 20.0, "protein": 1.6,  "fat": 0.1,  "kcal": 86},
    "Pumpkin":           {"carb": 7.0,  "protein": 1.0,  "fat": 0.1,  "kcal": 26},
    "Whole Wheat Bread": {"carb": 43.0, "protein": 13.0, "fat": 4.0,  "kcal": 247},
    "Oatmeal":           {"carb": 66.0, "protein": 17.0, "fat": 7.0,  "kcal": 389},
    "Chicken Breast":    {"carb": 0.0,  "protein": 31.0, "fat": 3.6,  "kcal": 165},
    "Pork Tenderloin":   {"carb": 0.0,  "protein": 21.0, "fat": 3.5,  "kcal": 143},
    "Beef Round":        {"carb": 0.0,  "protein": 26.0, "fat": 5.0,  "kcal": 185},
    "White Fish":        {"carb": 0.0,  "protein": 18.0, "fat": 0.7,  "kcal": 82},
    "Egg":               {"carb": 1.1,  "protein": 13.0, "fat": 10.6, "kcal": 155},
    "Almonds":           {"carb": 22.0, "protein": 21.0, "fat": 49.0, "kcal": 579},
    "Walnuts":           {"carb": 14.0, "protein": 15.0, "fat": 65.0, "kcal": 654},
    "Olive Oil":         {"carb": 0.0,  "protein": 0.0,  "fat": 100.0,"kcal": 884},
    "Cheese":            {"carb": 1.3,  "protein": 25.0, "fat": 33.0, "kcal": 403},
    "Avocado":           {"carb": 9.0,  "protein": 2.0,  "fat": 15.0, "kcal": 160},
}

CARB_FOODS    = ["White Rice", "Sweet Potato", "Pumpkin", "Whole Wheat Bread", "Oatmeal"]
PROTEIN_FOODS = ["Chicken Breast", "Pork Tenderloin", "Beef Round", "White Fish", "Egg"]
FAT_FOODS     = ["Almonds", "Walnuts", "Olive Oil", "Cheese", "Avocado"]

ACTIVITY_FACTORS = {
    1: 1.2,
    2: 1.375,
    3: 1.55,
    4: 1.725,
    5: 1.9
}

def calculate_bmr(weight, height, age, sex):
    if sex.lower() in ["male", "m"]:
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

def calculate_macros(
    age, sex, height_cm, activity_level,
    cur_weight, cur_muscle, cur_fat_pct,
    tgt_weight, tgt_muscle, tgt_fat_pct,
    duration_weeks
):
    cur_fat_mass = cur_weight * (cur_fat_pct / 100)
    tgt_fat_mass = tgt_weight * (tgt_fat_pct / 100)

    delta_fat = tgt_fat_mass - cur_fat_mass
    delta_muscle = tgt_muscle - cur_muscle

    fat_kcal_change = delta_fat * 7700
    muscle_kcal = delta_muscle * 2500
    total_kcal_change = fat_kcal_change + muscle_kcal
    daily_kcal_change = total_kcal_change / (duration_weeks * 7)

    bmr = calculate_bmr(cur_weight, height_cm, age, sex)
    tdee = bmr * ACTIVITY_FACTORS[activity_level]
    target_calories = tdee + daily_kcal_change

    protein = cur_weight * 1.5
    protein_kcal = protein * 4
    total_ratio = 5 + 3 + 2
    carb_kcal = target_calories * (5 / total_ratio)
    fat_kcal = target_calories * (2 / total_ratio)

    fat = fat_kcal / 9
    carb = carb_kcal / 4

    return round(target_calories), round(protein), round(fat), round(carb)

def generate_meal_plan(protein_g, fat_g, carb_g, meals):
    plan = []
    for i in range(meals):
        carb = CARB_FOODS[i % len(CARB_FOODS)]
        prot = PROTEIN_FOODS[i % len(PROTEIN_FOODS)]
        fat = FAT_FOODS[i % len(FAT_FOODS)]

        def grams(food, target, macro):
            val = FOOD_DB[food][macro]
            return (target / val * 100) if val > 0 else 0

        g_carb = grams(carb, carb_g / meals, "carb")
        g_prot = grams(prot, protein_g / meals, "protein")
        g_fat = grams(fat, fat_g / meals, "fat")

        kcal = lambda f, g: FOOD_DB[f]["kcal"] * g / 100

        plan.append({
            "meal": i + 1,
            "carb_food": carb,
            "carb_g": round(g_carb, 1),
            "protein_food": prot,
            "protein_g": round(g_prot, 1),
            "fat_food": fat,
            "fat_g": round(g_fat, 1),
            "total_kcal": round(kcal(carb, g_carb) + kcal(prot, g_prot) + kcal(fat, g_fat), 1)
        })
    return plan

if __name__ == "__main__":
    age = int(input("Age: "))
    sex = input("Sex (male/female): ")
    height = float(input("Height (cm): "))

    print("""
Select your activity level:
  1 - Sedentary (little or no exercise)
  2 - Lightly active (light exercise/sports 1–3 days/week)
  3 - Moderately active (moderate exercise/sports 3–5 days/week)
  4 - Very active (hard exercise/sports 6–7 days/week)
  5 - Extra active (very hard exercise, physical job or 2x training)
""")

    activity = int(input("Enter your activity level (1–5): "))

    cur_weight = float(input("Current weight (kg): "))
    cur_muscle = float(input("Current skeletal muscle mass (kg): "))
    cur_fat_pct = float(input("Current body fat percentage (%): "))

    tgt_weight = float(input("Target weight (kg): "))
    tgt_muscle = float(input("Target skeletal muscle mass (kg): "))
    tgt_fat_pct = float(input("Target body fat percentage (%): "))

    duration = int(input("Duration (weeks): "))
    meals = int(input("Meals per day: "))

    calories, protein, fat, carb = calculate_macros(
        age, sex, height, activity,
        cur_weight, cur_muscle, cur_fat_pct,
        tgt_weight, tgt_muscle, tgt_fat_pct,
        duration
    )

    print(f"\nTarget Calories: {calories} kcal")
    print(f"Protein: {protein}g | Fat: {fat}g | Carbs: {carb}g\n")

    plan = generate_meal_plan(protein, fat, carb, meals)
    for meal in plan:
        print(f"[Meal {meal['meal']}]")
        print(f"  Carbs: {meal['carb_food']} {meal['carb_g']}g")
        print(f"  Protein: {meal['protein_food']} {meal['protein_g']}g")
        print(f"  Fat: {meal['fat_food']} {meal['fat_g']}g")
        print(f"  Total kcal: {meal['total_kcal']} kcal\n")
