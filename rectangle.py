import math

GREEN = '\033[32m'
RESET = '\033[0m'

try: 
    class Rectangle():
        def __init__(self, area, width, length, select, diagonal, perimeter):
            self.area = area
            self.width = width
            self.length = length
            self.select = select
            self.diagonal = diagonal
            self.perimeter = perimeter

        def rectangle_area(self):
            return "A = {}".format(self.width * self.length)
        
        def rectangle_width_area(self):
            return "w = {}".format(self.area / self.length)
        
        def rectangle_length_area(self):
            return "l = {}".format(self.area / self.width)
        
        def rectangle_diagonal(self):
            return "d = {}".format(math.sqrt((self.width ** 2) + (self.length ** 2)))

        def rectangle_length_diagonal(self):
            return "l = {}".format(math.sqrt((self.diagonal ** 2) - (self.width ** 2)))
        
        def rectangle_width_diagonal(self):
            return "w = {}".format(math.sqrt((self.diagonal ** 2) - (self.length ** 2)))
        
        def rectangle_perimeter(self):
            return "P = {}".format(2 * (self.length + self.width))
        
        def rectangle_perimeter_length(self):
            return "l = {}".format((self.perimeter / 2) - self.width)
        
        def rectangle_perimeter_width(self):
            return "w = {}".format((self.perimeter / 2) - self.length)
        
    print(f"{GREEN}RECTANGLE CALCULATOR{RESET}")
    print("\n".join(["1, Area", "2. Area Width", "3. Area Length", "4. Diagonal", "5. Diagonal Width", "6. Diagonal Length", "7. Perimeter", "8. Perimeter Width", "9. Perimeter Length"]))
    select = str(input("Select one of the following: "))
    if select.strip().lower() == "area":
        length = float(input("Length: "))
        width = float(input("Width: "))
        r = Rectangle(None, width, length, select, None, None)
        print(r.rectangle_area())

    elif select.strip().lower() == "area width":
        area = float(input("Area: "))
        length = float(input("Length: "))
        r = Rectangle(area, None, length, select, None, None)
        print(r.rectangle_width_area())

    elif select.strip().lower() == "area length":
        area = float(input("Area: "))
        width = float(input("Width: "))
        r = Rectangle(area, width, None, select, None, None)
        print(r.rectangle_length_area())

    elif select.strip().lower() == "diagonal":
        width = float(input("Width: "))
        length = float(input("Length: "))
        r = Rectangle(None, width, length, select, None, None)
        print(r.rectangle_diagonal())

    elif select.strip().lower() == "diagonal width":
        diagonal = float(input("Diagonal: "))
        length = float(input("Length: "))
        r = Rectangle(None, None, length, select, diagonal, None)
        print(r.rectangle_width_diagonal())

    elif select.strip().lower() == "diagonal length":
        diagonal = float(input("Diagonal: "))
        width = float(input("Width: "))
        r = Rectangle(None, width, None, select, diagonal, None)
        print(r.rectangle_length_diagonal())

    elif select.strip().lower() == "perimeter":
        length = float(input("Length: "))
        width = float(input("Width: "))
        r = Rectangle(None, width, length, select, None, None)
        print(r.rectangle_perimeter())

    elif select.strip().lower() == "perimeter width":
        perimeter = float(input("Perimeter: "))
        length = float(input("Length: "))
        r = Rectangle(None, None, length, select, None, perimeter)
        print(r.rectangle_perimeter_width())

    elif select.strip().lower() == "perimeter length":
        perimeter = float(input("Perimeter: "))
        width = float(input("Width: "))
        r = Rectangle(None, width, None, select, None, perimeter)
        print(r.rectangle_perimeter_length())

    else: 
        print("ERROR, Invalid Input!")

except ValueError:
    print("ERROR, Invalid Input!")