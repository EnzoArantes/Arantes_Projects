# Function to compute Body Mass Index (BMI)
def computeBMI(height_, weight_):
    # Convert weight from pounds to kilograms and height from inches to meters, then calculate BMI
    bmi = (weight_ / 2.205) / ((height_ / 39.37) ** 2)
    return bmi

# Introduction
print("This program computes and evaluates Body Mass Index (BMI)")
print()

# User input for height and weight
print("Enter height in Feet and Inches")
height_ft = int(input("Enter feet: "))  # Input height in feet
height_in = int(input("Enter inches: "))  # Input height in inches
weight = float(input("Enter Weight in Pounds: "))  # Input weight in pounds

# Convert height to total inches
height = (height_ft * 12) + height_in  
print("Height is", height, "inches")
print()

# Calculate and display BMI
bmi = round(computeBMI(height, weight), 1)  # Compute BMI and round to one decimal
print("Your Body Mass Index is", bmi)

# Evaluate and print BMI category
if 18.5 <= bmi <= 25:
    print("Normal Weight")
elif bmi > 25:
    print("Overweight")
else:
    print("Underweight")
