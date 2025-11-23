def calc(w, h):
    return w / (h ** 2)

def cat(b):
    if b < 18.5:
        return "Underweight"
    elif b < 25:
        return "Normal"
    elif b < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("BMI Calculator")
    u = input("Unit? (m)etric or (i)mperial: ").lower()
    
    if u == 'm':
        w = float(input("Weight (kg): "))
        h = float(input("Height (m): "))
    elif u == 'i':
        w = float(input("Weight (lbs): "))
        h = float(input("Height (in): "))
        w = w * 0.453592
        h = h * 0.0254
    else:
        print("Invalid unit")
        return
    
    b = calc(w, h)
    c = cat(b)
    
    print(f"BMI: {b:.2f}")
    print(f"Category: {c}")

if __name__ == "_main_":
    main()
