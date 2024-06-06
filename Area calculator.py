import math

def calculate_area(shape, dimensions):
    if shape == "rectangle":
        length, width = dimensions
        return length * width
    elif shape == "circle":
        radius = dimensions[0]
        return math.pi * (radius ** 2)
    else:
        return "Unknown shape"

rect_area = calculate_area("rectangle", (5, 3))  
circle_area = calculate_area("circle", (4,))    

print(f"Rectangle area: {rect_area}")
print(f"Circle area: {circle_area}")
