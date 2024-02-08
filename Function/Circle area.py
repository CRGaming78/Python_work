def calculate_circle_area(radius):
    pi_approx = 3.14159
    area = pi_approx*(radius**2)
    return area

radius = float(input("Enter the radius of the circle: "))
area = calculate_circle_area(radius)
print(f"The area of the circle with radius {radius} is: {area:.2f}")