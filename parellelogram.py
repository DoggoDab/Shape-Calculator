import math

GREEN = '\033[32m'
RESET = '\033[0m'

try: 
    class Parellelogram():
        def __init__(self, base, height, area, side, perimeter, select):
            self.base = base
            self.height = height
            self.area = area
            self.side = side
            self.perimeter = perimeter
            self.select = select

        def parellelogram_area(self):
            return "A = {:.2f}".format(self.base * self.height)
        
        def parellelogram_area_base(self):
            return "b = {:.2f}".format(self.area / self.height)
        
        def parellelogram_height(self):
            return "h = {:.2f}".format(self.area / self.base) 
        
        def parellelogram_perimeter(self):
            return "P = {:.2f}".format(2 * (self.side + self.base))
        
        def parellelogram_perimeter_base(self):
            return "b = {:.2f}".format((self.perimeter) / (2) - self.side)
        
        def parellelogram_side(self):
            return "a = {:.2f}".format((self.perimeter) / (2) - self.base)
        
    print(f"{GREEN}PARELLELOGRAM CALCULATOR{RESET}")
    print("\n".join(["1. Area", "2. Area Base", "3. Height", "4. Perimeter", "5. Perimeter Base", "6. Side"]))
    select = str(input("Select one of the following: "))
    if select.strip().lower() == "area":
        base = float(input("Base: "))
        height = float(input("Height: "))
        p = Parellelogram(base, height, None, None, None, select)
        print(p.parellelogram_area())

    elif select.strip().lower() == "area base":
        area = float(input("Area: "))
        height = float(input("Height: "))
        p = Parellelogram(None, height, area, None, None, select)
        print(p.parellelogram_area_base())

    elif select.strip().lower() == "height":
        area = float(input("Area: "))
        base = float(input("Base: "))
        p = Parellelogram(base, None, area, None, None, select)
        print(p.parellelogram_height())

    elif select.strip().lower() == "perimeter":
        side = float(input("Side: "))
        base = float(input("Base: "))
        p = Parellelogram(base, None, None, side, None, select)
        print(p.parellelogram_perimeter())

    elif select.strip().lower() == "perimeter base":
        perimeter = float(input("Perimeter: "))
        side = float(input("Side: "))
        p = Parellelogram(None, None, None, side, perimeter, select)
        print(p.parellelogram_perimeter_base())

    elif select.strip().lower() == "side":
        perimeter = float(input("Perimeter: "))
        base = float(input("Base: "))
        p = Parellelogram(base, None, None, None, perimeter, select)
        print(p.parellelogram_side())

    else: 
        print("ERROR, Invalid Input!")

except ValueError:
    print("ERROR, Invalid Input!")