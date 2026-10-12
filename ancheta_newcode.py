import math

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def distance_between_points(x1, y1, x2, y2):
    return math.dist((x1, y1), (x2, y2))

x1 = get_float("Enter x1: ")
y1 = get_float("Enter y1: ")
x2 = get_float("Enter x2: ")
y2 = get_float("Enter y2: ")

distance = distance_between_points(x1, y1, x2, y2)
print(f"\nThe distance between the two points is: {distance:.2f}")