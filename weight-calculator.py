import csv
from traceback import print_tb

import pandas as pd
import os

# Dictionary of planets in our solar system and their gravity (m/s^2)
planet_gravity = {
    "Mercury": 3.7,
    "Venus": 8.87,
    "Earth": 9.81,
    "Moon": 1.62,
    "Mars": 3.711,
    "Jupiter": 24.79,
    "Saturn": 10.44,
    "Uranus": 8.69,
    "Neptune": 11.15
}

print("Hello,choose an option:")
print( "a) Type a mass and see weight on other Planets")
print( "b) Show the rovers weight on Mars")

choice = input("Type a or b and press enter: ")

if choice == "a":
    mass = float(input("Type a mass weight: "))

    results = []
    for planet, gravity in planet_gravity.items():
        weight_N = mass * gravity
        weight_Lbs = weight_N * 0.224809   # Convert Newtons (N) into pounds (Lbs)
        results.append([planet, weight_N, weight_Lbs])
    print(f"Mass weight: {mass:.2f} kg")
    print("Weight on different Planets:")
    for planet, N, Lbs in results:
        print(f"{planet:<8}: {N:8.2f} N  ({Lbs:8.2f} Lbs)")

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
    Gravity_Earth = planet_gravity["Earth"]  # m/s^2
    Gravity_Mars = planet_gravity["Mars"]    # m/s^2

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


