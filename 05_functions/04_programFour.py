import math

def circle_stats(radius):
    area = round(math.pi * radius ** 2,2)
    circ = round(2 * math.pi * radius,2)
    return area, circ

a,c = circle_stats(5)

print(f"Area : {a} & Circumference : {c}")

