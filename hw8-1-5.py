#author: DMH 12/10/21

def volume(radius,height):
    volume = 0
    volume = 3.14 * (int(radius) ** 2) * int(height)
    return volume

radius = input("What is the radius")
height = input("What is the height")

print(volume(radius,height))
