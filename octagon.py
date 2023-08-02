import math

GREEN = '\033[32m'
RESET = '\033[0m'

try: 
    class Octagon():
        def __init__(self, side, area, perimeter, select):
            self.side = side
            self.area = area
            self.perimeter = perimeter
            self.select = select

        def octagon_area(self):
            return "A = {:.2f}".format(2 * (1 + math.sqrt(2)) * math.pow(self.side, 2))
        
        def octagon_area_side(self):
            return "a = {:.2f}".format(math.sqrt(math.sqrt(2) * (self.area) / (2) - (self.area) / (2)))
        
        def octagon_perimeter(self):
            return "P = {:.2f}".format(8 * self.side)
        
        def octagon_perimeter_side(self):
            return "a = {:.2f}".format(self.perimeter / 8)
        
    print(f"{GREEN}OCTAGON CALCULATOR{RESET}")
    print("\n".join(["1. Area", "2. Area Side", "3. Perimeter", "4. Perimeter Side"]))
    select = str(input("Select one of the following: "))
    if select.strip().lower() == "area":
        side = float(input("Side: "))
        o = Octagon(side, None, None, select)
        print(o.octagon_area())

    elif select.strip().lower() == "area side":
        area = float(input("Area: ")) 
        o = Octagon(None, area, None, select)
        print(o.octagon_area_side()) 

    elif select.strip().lower() == "perimeter":
        side = float(input("Side: "))
        o = Octagon(side, None, None, select)
        print(o.octagon_perimeter())

    elif select.strip().lower() == "perimeter side":
        perimeter = float(input("Perimeter: "))
        o = Octagon(None, None, perimeter, select)
        print(o.octagon_perimeter_side()) 

    else: 
        print("ERROR, Invalid Input!")

except ValueError: 
    print("ERROR, Invalid Input!")