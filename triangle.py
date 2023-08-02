import math

GREEN = '\033[32m'
RESET = '\033[0m'

try: 
    class Triangle():
        def __init__(self, base, height, area, select, side, side1, gamma, perimetre):
            self.base = base
            self.height = height
            self.area = area
            self.select = select
            self.side = side
            self.side1 = side1
            self.gamma = gamma
            self.perimetre = perimetre

        def triangle_area(self):
            return "A = {:.2f}".format(self.height * self.base / 2)
        
        def triangle_base(self):
            return "b = {:.2f}".format(2 * self.area / self.height)
        
        def triangle_height(self):
            return "hb = {:.2f}".format(2 * self.area / self.base)
        
        def triangle_gamma_degrees(self):
            v = 2 * self.area / (self.base * self.side)
            if v >= -1 and v <= 1:
                rad = math.asin(v)
                deg = math.degrees(rad)
                return "γ = {:.2f}".format(deg)
            
            else: 
                return "ERROR, Invalid Input!"
            
        def triangle_gamma_radians(self):
            v = 2 * self.area / (self.base * self.side)
            if v >= -1 and v <= 1:
                rad = math.asin(v)
                return "γ = {:.2f}".format(rad)
            
            else:
                return "ERROR, Invalid Input!"
            
        def triangle_gamma_side_degrees(self):
            g = math.radians(self.gamma)
            return "a = {:.2f}".format(2 * self.area / (self.base * math.sin(g)))
        
        def triangle_gamma_side_radians(self):
            g = math.radians(self.gamma)
            d = math.degrees(g)
            return "a = {:.2f}".format(2 * self.area / (self.base * math.sin(d)))
        
        def triangle_gamma_base_degrees(self):
            g = math.radians(self.gamma)
            return "b = {:.2f}".format(2 * self.area / (self.side * math.sin(g)))
        
        def triangle_gamma_base_radians(self):
            g = math.radians(self.gamma)
            d = math.degrees(g)
            return "b = {:.2f}".format(2 * self.area / (self.side * math.sin(d)))

        def triangle_gamma_area_degrees(self): 
            g = math.radians(self.gamma)
            return "A = {:.2f}".format(self.side * self.base * (math.sin(g)) / (2))
        
        def triangle_gamma_area_radians(self):
            g = math.radians(self.gamma)
            d = math.degrees(g)
            return "A = {:.2f}".format(self.side * self.base * (math.sin(d)) / (2))

        def triangle_perimetre(self):
            return "P = {:.2f}".format(self.side + self.base + self.side1)

        def triangle_perimetre_side_a(self):
            return "a = {:.2f}".format(self.perimetre - self.base - self.side1) 
        
        def triangle_perimetre_base(self):
            return "b = {:.2f}".format(self.perimetre - self.side - self.side1)
        
        def triangle_perimetre_side_c(self):
            return "c = {:.2f}".format(self.perimetre - self.side - self.base)
                        
    print(f"{GREEN}TRIANGLE CALCULATOR{RESET}")
    print("\n".join(["1. Area", "2. Base", "3. Height", "4. Gamma", "5. Gamma Side A", "6. Gamma Base", "7. Gamma Area","8. Perimeter", "9. Perimeter Side A", "10. Perimeter Base", "11. Perimeter Side C"]))
    select = str(input("Select one of the following above: "))
    if select.strip().lower() == "area":
        height = float(input("Height: "))
        base = float(input("Base: "))
        t = Triangle(base, height, None, select, None, None, None, None)
        print(t.triangle_area())

    elif select.strip().lower() == "base": 
        height = float(input("Height: "))
        area = float(input("Area: "))
        t = Triangle(None, height, area, select, None, None, None, None)
        print(t.triangle_base())

    elif select.strip().lower() == "height":
        base = float(input("Base: "))
        area = float(input("Area: "))
        t = Triangle(base, None, area, select, None, None, None, None)
        print(t.triangle_height())

    elif select.strip().lower() == "gamma":
        print("\n".join(["1. Degrees", "2. Radians"]))
        select = str(input("Select from the following above: "))
        if select.strip().lower() == "degrees":
            area = float(input("Area: "))
            base = float(input("Base: "))
            side = float(input("Side: "))
            t = Triangle(base, None, area, select, side, None, None, None)
            print(t.triangle_gamma_degrees())

        elif select.strip().lower() == "radians":
            area = float(input("Area: "))
            base = float(input("Base: "))
            side = float(input("Side: "))
            t = Triangle(base, None, area, select, side, None, None, None)
            print(t.triangle_gamma_radians())

    elif select.strip().lower() == "gamma side a":
        print("\n".join(["1. Degrees", "2. Radians"]))
        select = str(input("Select one of the following: "))
        if select.strip().lower() == "degrees":
            base = float(input("Base: "))
            gamma = float(input("Gamma: "))
            area = float(input("Area: "))
            t = Triangle(base, None, area, select, None, None, gamma, None)
            print(t.triangle_gamma_side_degrees())

        elif select.strip().lower() == "radians":
            base  = float(input("Base: "))
            gamma = float(input("Gamma: "))
            area = float(input("Area: "))
            t = Triangle(base, None, area, select, None, None, gamma, None)
            print(t.triangle_gamma_side_radians())

    elif select.strip().lower() == "gamma base":
        print("\n".join(["1. Degrees", "2. Radians"]))
        select = str(input("Select one of the following: "))
        if select.strip().lower() == "degrees":
            side = float(input("Side: "))
            gamma = float(input("Gamma: "))
            area = float(input("Area: "))
            t = Triangle(None, None, area, select, side, None, gamma, None)
            print(t.triangle_gamma_base_degrees())

        elif select.strip().lower() == "radians":
            side = float(input("Side: "))
            gamma = float(input("Gamma: "))
            area = float(input("Area: "))
            t = Triangle(None, None, area, select, side, None, gamma, None)
            print(t.triangle_gamma_base_radians())

    elif select.strip().lower() == "gamma area":
        print("\n".join(["1. Degrees", "2. Radians"]))
        select = str(input("Select one of the following: "))
        if select.strip().lower() == "degrees":
            side = float(input("Side: "))
            base = float(input("Base: "))
            gamma = float(input("Gamma: "))
            t = Triangle(base, None, None, select, side, None, gamma, None)
            print(t.triangle_gamma_area_degrees())

        elif select.strip().lower() == "radians":
            side = float(input("Side: "))
            base = float(input("Base: "))
            gamma = float(input("Gamma: "))
            t = Triangle(base, None, None, select, side, None, gamma, None)
            print(t.triangle_gamma_area_radians())

    elif select.strip().lower() == "perimeter":
        side = float(input("Side: "))
        base = float(input("Base: "))
        side1 = float(input("Side: "))
        t = Triangle(base, None, None, select, side, side1, None, None)
        print(t.triangle_perimetre())

    elif select.strip().lower() == "perimeter side a":
        perimetre = float(input("Perimeter: "))
        base = float(input("Base: "))
        side1 = float(input("Side: "))
        t = Triangle(base, None, None, select, None, side1, None, perimetre)
        print(t.triangle_perimetre_side_a())    
            
    elif select.strip().lower() == "perimeter base":
        perimetre = float(input("Perimeter: "))
        side = float(input("Side: "))
        side1 = float(input("Side: "))
        t = Triangle(None, None, None, select, side, side1, None, perimetre)
        print(t.triangle_perimetre_base())

    elif select.strip().lower() == "perimeter side c": 
        perimetre = float(input("Perimeter: "))
        base = float(input("Base: "))
        side = float(input("Side: "))
        t = Triangle(base, None, None, select, side, None, None, perimetre)
        print(t.triangle_perimetre_side_c())

    else: 
        print("ERROR, Invalid Input!")

except ValueError: 
    print("ERROR, Invalid Input!")
