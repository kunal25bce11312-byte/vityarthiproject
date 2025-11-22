def calculate_bmi(weight, height):
    
    bmi = weight / (height ** 2)
    return bmi


def label_bmi(bmi):
    
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "obese"


def main():
    print("=== BMI Calculator ===")

    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)
    labeling = label_bmi(bmi)

    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Category: {labeling}")


if __name__ == "__main__":
    main()
