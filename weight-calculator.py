 import csv
from traceback import print_tb

import pandas as pd
import os

print("Hello,choose an option:")
print( "a) Type a mass and see it's weight on Mars")
print( "b) Show the rovers weight on Mars")

choice = input("Type a or b and press enter:")

if choice == "a":
    mass = float(input("Enter the mass in kilograms: "))
    Gravity_Mars = 3.711   # m/s^2
    weight_Mars_N = mass * Gravity_Mars
    weight_Mars_Lbs = weight_Mars_N * 0.224809  # Convert N to Lbs
    print(f"Mass: {mass:.2f} kg")
    print(f"weight on Mars: {weight_Mars_N:.2f} N ({weight_Mars_Lbs:.2f} Lbs)")

elif choice == "b":
    rovers = [
        {"Name": "Perseverance", "Mass_kg": 1025},
        {"Name": "Curiosity", "Mass_kg": 900},
        {"Name": "Opportunity", "Mass_kg": 185},
        {"Name": "Spirit", "Mass_kg": 185},
        {"Name": "Sojourner", "Mass_kg": 10.6}
    ]

    filename = 'Rovers.csv'
    with open(filename, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Name", "Mass_kg"])
        for r in rovers:
            csvwriter.writerow([r["Name"], r["Mass_kg"]])

    # Load rover data
    rover = pd.read_csv(filename)

    # Constants
    Gravity_Earth = 9.81  # m/s^2
    Gravity_Mars = 3.711  # m/s^2

    # Calculate Weight
    rover["Weight_Earth_N"] = rover["Mass_kg"] * Gravity_Earth
    rover["Weight_Earth_Lbs"] = rover["Weight_Earth_N"] * 0.224809  # Convert N to Lbs
    rover["Weight_Mars_N"] = rover["Mass_kg"] * Gravity_Mars
    rover["Weight_Mars_Lbs"] = rover["Weight_Mars_N"] * 0.224809  # Convert N to Lbs

    os.makedirs('result', exist_ok=True)

    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 100)

    # Save results
    rover.to_csv('result/Rover_weight.txt')

    # Print results
    print("Rover Weight:")
    print(rover[['Name', 'Weight_Earth_N', 'Weight_Earth_Lbs', 'Weight_Mars_N', 'Weight_Mars_Lbs']])



