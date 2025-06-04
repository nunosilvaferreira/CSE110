import math

# Core Requirements
# Square
square_side = float(input("What is the length of a side of the square (in cm)? "))
square_area_cm2 = square_side ** 2
square_area_m2 = square_area_cm2 / 10000
print("The area of the square is: {:.2f} cm² or {:.4f} m²".format(square_area_cm2, square_area_m2))

# Rectangle
rectangle_length = float(input("What is the length of the rectangle (in cm)? "))
rectangle_width = float(input("What is the width of the rectangle (in cm)? "))
rectangle_area_cm2 = rectangle_length * rectangle_width
rectangle_area_m2 = rectangle_area_cm2 / 10000
print("The area of the rectangle is: {:.2f} cm² or {:.4f} m²".format(rectangle_area_cm2, rectangle_area_m2))

# Circle
circle_radius = float(input("What is the radius of the circle (in cm)? "))
circle_area_cm2 = math.pi * (circle_radius ** 2)
circle_area_m2 = circle_area_cm2 / 10000
print("The area of the circle is: {:.2f} cm² or {:.4f} m²".format(circle_area_cm2, circle_area_m2))

# Stretch Challenge
print("\nStretch Challenge")
universal_length = float(input("Enter a single length value (in cm): "))

# Square area
square_area_stretch = universal_length ** 2
print("Area of square: {:.2f} cm²".format(square_area_stretch))

# Circle area
circle_area_stretch = math.pi * (universal_length ** 2)
print("Area of circle: {:.2f} cm²".format(circle_area_stretch))

# Cube volume
cube_volume = universal_length ** 3
print("Volume of cube: {:.2f} cm³".format(cube_volume))

# Sphere volume
sphere_volume = (4/3) * math.pi * (universal_length ** 3)
print("Volume of sphere: {:.2f} cm³".format(sphere_volume))
