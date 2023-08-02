import math

GREEN = '\033[32m'
RESET = '\033[0m'

try: 
    class Trapezoid():
        def __init__(self, base, base1, height, area, side, side1, perimeter, select):
            self.base = base
            self.base1 = base1
            self.height = height
            self.area = area
            self.side = side
            self.side1 = side1
            self.perimeter = perimeter
            self.select = select

        def trapezoid_area(self):
            return "A = {:.2f}".format((self.base + self.base1) / (2) * self.height)
        
        def trapezoid_area_base_a(self):
            return "a = {:.2f}".format(2 * (self.area) / (self.height) - self.base1)
        
        def trapezoid_area_base_b(self):
            return "b = {:.2f}".format(2 * (self.area) / (self.height) - self.base)
        
        def trapezoid_height(self):
            return "h = {:.2f}".format(2 * (self.area) / (self.base + self.base1))
        
        def trapezoid_perimeter(self):
            return "P = {:.2f}".format(self.base + self.base1 + self.side + self.side1)
        
        def trapezoid_perimeter_base_a(self):
            return "a = {:.2f}".format(self.perimeter - self.base1 - self.side - self.side1)
        
        def trapezoid_perimeter_base_b(self):
            return "b = {:.2f}".format(self.perimeter - self.base - self.side - self.side1)
        
        def trapezoid_perimeter_side_c(self):
            return "c = {:.2f}".format(self.perimeter - self.base - self.base1 - self.side1)
        
        def trapezoid_perimeter_side_d(self):
            return "d = {:.2f}".format(self.perimeter - self.base - self.base1 - self.side)
        
    print(f"{GREEN}TRAPEZOID CALCULATOR{RESET}")
    print("\n".join(["1. Area", "2. Area Base A", "3. Area Base B", "4. Height", "5. Perimeter", "6. Perimeter Base A", "7. Perimeter Base B", "8. Perimeter Side C", "9. Perimeter Side D"]))
    select = str(input("Select one of the following: "))
    if select.strip().lower() == "area":
        base = float(input("Base: "))
        base1 = float(input("Base: "))
        height = float(input("Height: "))
        t = Trapezoid(base, base1, height, None, None, None, None, select)
        print(t.trapezoid_area())

    elif select.strip().lower() == "area base a":
        area = float(input("Area: "))
        height = float(input("Height: "))
        base1 = float(input("Base: "))
        t = Trapezoid(None, base1, height, area, None, None, None, select)
        print(t.trapezoid_area_base_a())

    elif select.strip().lower() == "area base b":
        area = float(input("Area: "))
        height = float(input("Height: "))
        base = float(input("Base: "))
        t = Trapezoid(base, None, height, area, None, None, None, select)
        print(t.trapezoid_area_base_b())

    elif select.strip().lower() == "height":
        area = float(input("Area: "))
        base = float(input("Base: "))
        base1 = float(input("Base: "))
        t = Trapezoid(base, base1, None, area, None, None, None, select)
        print(t.trapezoid_height())

    elif select.strip().lower() == "perimeter":
        base = float(input("Base: "))
        base1 = float(input("Base: "))
        side = float(input("Side: "))
        side1 = float(input("Side: "))
        t = Trapezoid(base, base1, None, None, side, side1, None, select)
        print(t.trapezoid_perimeter())

    elif select.strip().lower() == "perimeter base a":
        perimeter = float(input("Perimeter: "))
        base1 = float(input("Base: "))
        side = float(input("Side: "))
        side1 = float(input("Side: "))
        t = Trapezoid(None, base1, None, None, side, side1, perimeter, select)
        print(t.trapezoid_perimeter_base_a())

    elif select.strip().lower() == "perimeter base b":
        perimeter = float(input("Perimeter: "))
        base = float(input("Base: "))
        side = float(input("Side: "))
        side1 = float(input("Side: "))
        t = Trapezoid(base, None, None, None, side, side1, perimeter, select)
        print(t.trapezoid_perimeter_base_b())

    elif select.strip().lower() == "perimeter side c":
        perimeter = float(input("Perimeter: "))
        base = float(input("Base: "))
        base1 = float(input("Base: "))
        side1 = float(input("Side: "))
        t = Trapezoid(base, base1, None, None, None, side1, perimeter, select)
        print(t.trapezoid_perimeter_side_c())

    elif select.strip().lower() == "perimeter side d":
        perimeter = float(input("Perimeter: "))
        base = float(input("Base: "))
        base1 = float(input("Base: "))
        side = float(input("Side: "))
        t = Trapezoid(base, base1, None, None, side, None, perimeter, select)
        print(t.trapezoid_perimeter_side_d())

    else: 
        print("ERROR, Invalid Input!")

except ValueError: 
    print("ERROR, Invalid Input!")