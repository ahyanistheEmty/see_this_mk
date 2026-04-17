def calculate_bmi(weight, height):
    \"\"\"
    Calculate the Body Mass Index (BMI).
    Weight should be in kilograms and height in meters.
    \"\"\"
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def get_category(bmi):
    \"\"\"
    Determine the BMI category.
    \"\"\"
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("--- BMI Calculator ---")
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        
        bmi = calculate_bmi(weight, height)
        category = get_category(bmi)
        
        print(f"Your BMI is: {bmi}")
        print(f"Category: {category}")
    except ValueError:
        print("Please enter valid numerical values for weight and height.")

if __name__ == "__main__":
    main()
