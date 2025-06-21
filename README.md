# Macro-Based Meal Planner

A Python-based tool that helps users create personalized meal plans tailored to their fitness goals, body composition, and daily lifestyle. Whether you're cutting, bulking, or maintaining, this script estimates your total daily energy expenditure (TDEE) and distributes your macros accordingly—using real food examples.

## Features
- Calculates Basal Metabolic Rate (BMR) and Total Daily Energy Expenditure (TDEE)
- Estimates daily target calories based on your body composition and goals
- Distributes macronutrients (carbohydrates, protein, fat) using standard nutritional guidelines
- Accepts detailed user input: current/target weight, muscle mass, body fat %, age, sex, height, duration
- Outputs macro breakdown for each meal, with real food examples from a built-in food database
- Simple terminal-based interaction—no external tools or configuration needed

## Requirements
- Python 3.7 or higher

## How to Run
```bash
python main.py
```
Follow the terminal prompts:
- Age, sex, height (cm)
- Current weight, muscle mass, and body fat %
- Target weight, muscle mass, and body fat %
- Duration (in weeks)
- Activity level (1 to 5)
- Number of meals per day

## Example Input
```
Age: 26
Sex: M
Height (cm): 170
Current Weight (kg): 66.2
Current Muscle Mass (kg): 37
Current Body Fat %: 14
Target Weight (kg): 64
Target Muscle Mass (kg): 38
Target Body Fat %: 10
Duration (weeks): 8
Activity Level (1-5): 3
Meals per Day: 3
```

## Example Output
```
=== Personalized Nutrition Plan ===
Daily Calorie Target: 2600 kcal
{
  "Protein (g)": 98,
  "Fat (g)": 58,
  "Carbs (g)": 358
}

[Meal 1]
  Carbs: White Rice 260.9g
  Protein: Chicken Breast 132.3g
  Fat: Almonds 11.4g
  Total kcal: 651.3 kcal

[Meal 2]
  Carbs: Sweet Potato 240.5g
  Protein: Egg 142.0g
  Fat: Walnuts 9.2g
  Total kcal: 654.7 kcal

[Meal 3]
  Carbs: Oatmeal 145.6g
  Protein: White Fish 137.2g
  Fat: Avocado 29.8g
  Total kcal: 648.9 kcal
```

## Activity Level Guide
| Level | Description                            |
|-------|----------------------------------------|
| 1     | Sedentary (little or no exercise)      |
| 2     | Light activity (1–3 days/week)         |
| 3     | Moderate activity (3–5 days/week)      |
| 4     | Active (daily exercise or intense 3–4 days/week) |
| 5     | Very active (twice/day or athlete level training) |

## Reference Equations
- **BMR** (Mifflin-St Jeor Equation)
- **TDEE** = BMR × Activity Factor
- **Macronutrient Distribution** (Approx.): 15% Protein, 20% Fat, 65% Carbs

## Data Source
Food data (calories, protein, carbs, fat) is based on USDA average values and simplified for this project.
