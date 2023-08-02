import math

GREEN = '\033[32m'
RESET = '\033[0m'

try: 
    class Hexagon():
        def __init__(self, side, area, perimeter, select):
            self.side = side
            self.area = area
            self.perimeter = perimeter
            self.select = select

        def hexagon_area(self):
            return "A = {:.2f}".format((3 * math.sqrt(3)) / (2) * math.pow(self.side, 2))
        
        def hexagon_area_side(self):
            return "a = {:.2f}".format(math.pow(3, 0.25) * math.sqrt(2 * self.area / 9))
        
        def hexagon_perimeter(self):
            return "P = {:.2f}".format(6 * self.side)
        
        def hexagon_perimeter_side(self):
            return "a = {:.2f}".format(self.perimeter / 6)
        
    print(f"{GREEN}HEXAGON CALCULATOR{RESET}")
    print("\n".join(["1. Area", "2. Area Side", "3. Perimeter", "4. Perimeter Side"]))
    select = str(input("Select one of the following: "))
    if select.strip().lower() == "area":
        side = float(input("Side: "))
        h = Hexagon(side, None, None, select)
        print(h.hexagon_area())

    elif select.strip().lower() == "area side":
        area = float(input("Area: "))
        h = Hexagon(None, area, None, select)
        print(h.hexagon_area_side())

    elif select.strip().lower() == "perimeter":
        side = float(input("Side: "))
        h = Hexagon(side, None, None, select)
        print(h.hexagon_perimeter())

    elif select.strip().lower() == "perimeter side":
        perimeter = float(input("Perimeter: "))
        h = Hexagon(None, None, perimeter, select)
        print(h.hexagon_perimeter_side())

    else: 
        print("ERROR, Invalid Input!")

except ValueError: 
    print("ERROR, Invalid Input!")