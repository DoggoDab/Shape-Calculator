import math

GREEN = '\033[32m'
RESET = '\033[0m'

try: 
    class Rhombus():
        def __init__(self, area, diagonal, diagonal1, side, perimeter, select):
            self.area = area
            self.diagonal = diagonal
            self.diagonal1 = diagonal1
            self.side = side
            self.perimeter = perimeter
            self.select = select

        def rhombus_area(self):
            return "A = {:.2f}".format((self.diagonal * self.diagonal1) / (2))
        
        def rhombus_diagonal_p(self):
            return "p = {:.2f}".format(2 * (self.area) / (self.diagonal1))
        
        def rhombus_diagonal_q(self):
            return "q = {:.2f}".format(2 * (self.area) / (self.diagonal))
        
        def rhombus_perimeter(self):
            return "P = {:.2f}".format(4 * self.side)
        
        def rhombus_perimeter_side(self):
            return "a = {:.2f}".format(self.perimeter / 4)
        
        def rhombus_side(self):
            return "a = {:.2f}".format(math.sqrt(self.diagonal ** 2 + self.diagonal1 ** 2) / 2)
        
        def rhombus_side_diagonal_p(self):
            return "p = {:.2f}".format(math.sqrt(4 * math.pow(self.side, 2) - math.pow(self.diagonal1, 2)))
        
        def rhombus_side_diagonal_q(self):
            return "q = {:.2f}".format(math.sqrt(4 * math.pow(self.side, 2) - math.pow(self.diagonal, 2)))
        
    print(F"{GREEN}RHOMBUS CALCULATOR{RESET}")
    print("\n".join(["1. Area", "2. Diagonal P", "3. Diagonal Q", "4. Perimeter", "5. Perimeter Side", "6. Diagonal Side", "7. Diagonal P Side", "8. Diagonal Q Side"]))
    select = str(input("Select one of the following: "))
    if select.strip().lower() == "area":
        diagonal = float(input("Diagonal: "))
        diagonal1 = float(input("Diagonal: "))
        r = Rhombus(None, diagonal, diagonal1, None, None, select)
        print(r.rhombus_area())

    elif select.strip().lower() == "diagonal p":
        area = float(input("Area: "))
        diagonal1 = float(input("Diagonal: "))
        r = Rhombus(area, None, diagonal1, None, None, select)
        print(r.rhombus_diagonal_p())

    elif select.strip().lower() == "diagonal q":
        area = float(input("Area: "))
        diagonal = float(input("Diagonal: "))
        r = Rhombus(area, diagonal, None, None, None, select)
        print(r.rhombus_diagonal_q())

    elif select.strip().lower() == "perimeter":
        side = float(input("Side: "))
        r = Rhombus(None, None, None, side, None, select)
        print(r.rhombus_perimeter())

    elif select.strip().lower() == "perimeter side":
        perimeter = float(input("Perimeter: "))
        r = Rhombus(None, None, None, None, perimeter, select)
        print(r.rhombus_perimeter_side())

    elif select.strip().lower() == "diagonal side":
        diagonal = float(input("Diagonal: "))
        diagonal1 = float(input("Diagonal: "))
        r = Rhombus(None, diagonal, diagonal1, None, None, select)
        print(r.rhombus_side())

    elif select.strip().lower() == "diagonal p side":
        side = float(input("Side: "))
        diagonal1 = float(input("Diagonal: "))
        r = Rhombus(None, None, diagonal1, side, None, select)
        print(r.rhombus_side_diagonal_p())

    elif select.strip().lower() == "diagonal q side":
        side = float(input("Side: "))
        diagonal = float(input("Diagonal: "))
        r = Rhombus(None, diagonal, None, side, None, select)
        print(r.rhombus_side_diagonal_q())

    else: 
        print("ERROR, Invalid Input!")

except ValueError: 
    print("ERROR, Invalid Input!")