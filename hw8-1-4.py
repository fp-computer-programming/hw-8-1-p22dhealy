#author: DMH 12/10/21

def surface_area(radius,height):
    surface_area = 0
    surface_area = (2 * (3.14 * int(radius) * int(height))) + (2 * (3.14 * (int(radius) ** 2)))
    return surface_area

radius = input("What is the radius:")
height = input("What is the height:")

print(surface_area(radius,height))
