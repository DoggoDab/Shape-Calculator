import math

GREEN = '\033[32m'
RESET = '\033[0m'

try: 
    class Circle():
        def __init__(self, radius, area, select, diameter, circumference):
            self.radius = radius
            self.area = area
            self.select = select
            self.diameter = diameter
            self.circumference = circumference

        def circle_area(self):
            return "A = {:.2f}".format(math.pi * self.radius ** 2)
        
        def circle_area_radius(self):
            return "r = {:.2f}".format(math.sqrt(self.area / math.pi))
        
        def circle_diametre(self):
            return "d = {:.2f}".format(self.radius * 2)
        
        def circle_radius(self):
            return "r = {:.2f}".format(self.diameter / 2)
        
        def circle_circumference(self):
            return "C = {:.2f}".format(2 * math.pi * self.radius) 
        
        def circle_circumference_radius(self):
            return "r = {:.2f}".format(self.circumference / (2 * math.pi))
        
    print(f"{GREEN}CIRCLE CALCULATOR{RESET}")
    print("\n".join(["1. Area", "2. Radius Area", "3. Diameter", "4. Radius Diameter", "5. Circumference", "6. Circumference Radius"]))
    select = str(input("Select one of the following: "))
    if select.strip().lower() == "area":
        radius = float(input("Radius: "))
        c = Circle(radius, None, select, None, None)
        print(c.circle_area())

    elif select.strip().lower() == "radius area":
        area = float(input("Area: "))
        c = Circle(None, area, select, None, None)
        print(c.circle_area_radius())

    elif select.strip().lower() == "diameter":
        radius = float(input("Radius: "))
        c = Circle(radius, None, select, None, None)
        print(c.circle_diametre())

    elif select.strip().lower() == "radius diameter":
        diameter = float(input("Diameter: "))
        c = Circle(None, None, select, diameter, None)
        print(c.circle_radius())

    elif select.strip().lower() == "circumference":
        radius = float(input("Radius: "))
        c = Circle(radius, None, select, None, None)
        print(c.circle_circumference())

    elif select.strip().lower() == "circumference radius":
        circumference = float(input("Circumference: "))
        c = Circle(None, None, select, None, circumference)
        print(c.circle_circumference_radius())

    else: 
        print("ERROR, Invalid Input!")    

except ValueError: 
    print("ERROR, Invalid Input!")