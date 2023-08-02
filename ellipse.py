import math

GREEN = '\033[32m'
RESET = '\033[0m'

try: 
    class Ellipse():
        def __init__(self, area, axis, axis1, select):
            self.area = area
            self.axis = axis
            self.axis1 = axis1
            self.select = select

        def ellipse_area(self):
            return "A = {:.2f}".format(math.pi * self.axis * self.axis1)
        
        def ellipse_axis_a(self):
            return "a = {:.2f}".format((self.area) / (math.pi * self.axis1))
        
        def ellipse_axis_b(self):
            return "b = {:.2f}".format((self.area) / (math.pi * self.axis))
        
        def ellipse_circumference(self):
            return "C = {:.2f}".format(math.pi * (self.axis + self.axis1) * (1 + (3 * ((self.axis - self.axis1) ** 2) / (self.axis + self.axis1) ** 2 / (10 + math.sqrt(4 - 3 * ((self.axis - self.axis1) ** 2) / (self.axis + self.axis1) ** 2)))))
        
    print(f"{GREEN}ELLIPSE CALCULATOR{RESET}")
    print("\n".join(["1. Area", "2. Axis A", "3. Axis B", "4. Circumference"]))
    select = str(input("Select one of the following: "))
    if select.strip().lower() == "area":
        axis = float(input("Axis: "))
        axis1 = float(input("Axis: "))
        e = Ellipse(None, axis, axis1, select)
        print(e.ellipse_area())

    elif select.strip().lower() == "axis a":
        area = float(input("Area: "))
        axis1 = float(input("Axis: "))
        e = Ellipse(area, None, axis1, select)
        print(e.ellipse_axis_a())

    elif select.strip().lower() == "axis b":
        area = float(input("Area: "))
        axis = float(input("Axis: "))
        e = Ellipse(area, axis, None, select)
        print(e.ellipse_axis_b())

    elif select.strip().lower() == "circumference":
        axis = float(input("Axis: "))
        axis1 = float(input("Axis: "))
        e = Ellipse(None, axis, axis1, select)
        print(e.ellipse_circumference())

    else: 
        print("ERROR, Invalid Input!")

except ValueError:
    print("ERROR, Invalid Input!")