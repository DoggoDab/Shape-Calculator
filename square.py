from math import sqrt

GREEN = "\033[32m"
RESET = "\033[0m"

try: 
    class Square():
        def __init__(self, area, side, select, diagonal, perimeter):
            self.area = area
            self.side = side
            self.select = select
            self.diagonal = diagonal
            self.perimeter = perimeter

        def square_area(self):
            return "A = {}".format(self.side ** 2)
        
        def square_side(self):
            return "a = {}".format(sqrt(self.area))
        
        def square_diagonal(self):
            return "d = {}".format(sqrt(2) * self.side)
        
        def square_diagonal_side(self):
            return "a = {}".format(sqrt(2) * self.diagonal / 2)
        
        def square_perimetre(self):
            return "P = {}".format(4 * self.side)
        
        def square_perimetre_side(self):
            return "a = {}".format(self.perimeter / 4)
        
    print(f"{GREEN}SQUARE CALCULATOR{RESET}")
    print("\n".join(["1. Area", "2. Side", "3. Diagonal", "4. Diagonal Side", "5. Perimeter", "6. Perimeter Side"]))
    select = str(input("Select one of the following above: "))
    if select.strip().lower() == "area":
        side = float(input("Side: "))
        s = Square(None, side, select, None, None)
        print(s.square_area())

    elif select.strip().lower() == "side":
        area = float(input("Area: "))
        s = Square(area, None, select, None, None)
        print(s.square_side())

    elif select.strip().lower() == "diagonal":
        side = float(input("Side: "))
        s = Square(None, side, select, None, None)
        print(s.square_diagonal())

    elif select.strip().lower() == "diagonal side":
        diagonal = float(input("Diagonal: "))
        s = Square(None, None, select, diagonal, None)
        print(s.square_diagonal_side())

    elif select.strip().lower() == "perimeter":
        side = float(input("Side: "))
        s = Square(None, side, select, None, None)
        print(s.square_perimetre())

    elif select.strip().lower() == "perimeter side":
        perimeter = float(input("Perimeter: "))
        s = Square(None, None, select, None, perimeter)
        print(s.square_perimetre_side())

    else:
        print("ERROR, Invalid Input!")

except ValueError:
    print("ERROR, Invalid Input!")