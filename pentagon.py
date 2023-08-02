import math

GREEN = '\033[32m'
RESET = '\033[0m'

try: 
    class Pentagon():
        def __init__(self, side, area, diagonal, perimeter, select):
            self.side = side
            self.area = area
            self.diagonal = diagonal 
            self.perimeter = perimeter
            self.select = select

        def pentagon_area(self):
            return "A = {:.2f}".format((1/4 * math.sqrt(5 * (5 + 2 * math.sqrt(5)))) * self.side ** 2)
        
        def pentagon_area_side(self):
            return "a = {:.2f}".format((2 * math.pow(5, 0.75)) * (math.sqrt(self.area)) / (5 * (math.pow(math.sqrt(20) + 5, 0.25))))
        
        def pentagon_diagonal(self):
            return "d = {:.2f}".format((1 + math.sqrt(5)) / (2) * self.side)
        
        def pentagon_diagonal_side(self):
            return "a = {:.2f}".format(self.diagonal * (-1 + math.sqrt(5)) / (2))
        
        def pentagon_perimeter(self):
            return "P = {:.2f}".format(5 * self.side)
        
        def pentagon_perimeter_side(self):
            return "a = {:.2f}".format(self.perimeter / 5)
        
    print(f"{GREEN}PENTAGON CALCULATOR{RESET}")
    print("\n".join(["1. Area", "2. Area Side", "3. Diagonal", "4. Diagonal Side", "5. Perimeter", "6. Perimeter Side"]))
    select = str(input("Select one of the following above: "))
    if select.strip().lower() == "area":
        side = float(input("Side: "))
        p = Pentagon(side, None, None, None, select)
        print(p.pentagon_area())

    elif select.strip().lower() == "area side":
        area = float(input("Area: "))
        p = Pentagon(None, area, None, None, select)
        print(p.pentagon_area_side())

    elif select.strip().lower() == "diagonal":
        side = float(input("Side: "))
        p = Pentagon(side, None, None, None, select)
        print(p.pentagon_diagonal())

    elif select.strip().lower() == "diagonal side":
        diagonal = float(input("Diagonal: "))
        p = Pentagon(None, None, diagonal, None, select)
        print(p.pentagon_diagonal_side())

    elif select.strip().lower() == "perimeter":
        side = float(input("Side: "))
        p = Pentagon(side, None, None, None, select)
        print(p.pentagon_perimeter())

    elif select.strip().lower() == "perimeter side":
        perimeter = float(input("Perimeter: "))
        p = Pentagon(None, None, None, perimeter, select)
        print(p.pentagon_perimeter_side())

    else: 
        print("ERROR, Invalid Input!")

except ValueError:
    print("ERROR, Invalid Input!")