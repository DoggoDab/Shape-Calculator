import math

GREEN = '\033[32m'
RESET = '\033[0m'

try: 
    class Cuboid():
        def __init__(self, total_surface_area, volume, diagonal, select, length, breadth, height):
            self.total_surface_area = total_surface_area
            self.volume = volume
            self.diagonal = diagonal
            self.length = length
            self.breadth = breadth
            self.height = height
            self.select = select

        def cuboid_surface_area(self):
            return "A = {:.2f}".format(2 * (self.length * self.breadth + self.breadth * self.height + self.length * self.height))

        def cuboid_surface_area_length(self):
            return "l = {:.2f}".format(((self.total_surface_area / 2) - self.height * self.breadth) / (self.height + self.breadth))
        
        def cuboid_surface_area_width(self):
            return "w = {:.2f}".format(((self.total_surface_area / 2) - self.height * self.length) / (self.height + self.length))
        
        def cuboid_surface_area_height(self):
            return "h = {:.2f}".format(((self.total_surface_area / 2) - self.length * self.breadth) / (self.length + self.breadth))
        
        def cuboid_volume(self):
            return "V = {:.2f}".format(self.length * self.breadth * self.height)
        
        def cuboid_volume_length(self):
            return "l = {:.2f}".format((self.volume) / (self.height * self.breadth))
        
        def cuboid_volume_width(self):
            return "w = {:.2f}".format((self.volume) / (self.height * self.length))
        
        def cuboid_volume_height(self):
            return "h = {:.2f}".format((self.volume) / (self.length * self.breadth))
        
        def cuboid_diagonal(self):
            return "d = {:.2f}".format(math.sqrt(math.pow(self.length, 2) + math.pow(self.breadth, 2) + math.pow(self.height, 2)))
        
        def cuboid_diagonal_length(self):
            return "l = {:.2f}".format(math.sqrt(math.pow(self.diagonal, 2) - math.pow(self.height, 2) - math.pow(self.breadth, 2)))

        def cuboid_diagonal_width(self):
            return "w = {:.2f}".format(math.sqrt(math.pow(self.diagonal, 2) - math.pow(self.height, 2) - math.pow(self.length, 2)))
        
        def cuboid_diagonal_height(self):
            return "h = {:.2f}".format(math.sqrt(math.pow(self.diagonal, 2) - math.pow(self.length, 2) - math.pow(self.breadth, 2)))
        
    print(f"{GREEN}CUBOID CALCULATOR{RESET}")
    print("\n".join(["1. Surface Area", "2. Surface Area Length", "3. Surface Area Width", "4. Surface Area Height", "5. Volume", "6. Volume Length", "7. Volume Width", "8. Volume Height", "9. Diagonal", "10. Diagonal Length", "11. Diagonal Width", "12. Diagonal Height"]))
    select = str(input("Select one of the following: "))
    if select.strip().lower() == "surface area":
        length = float(input("Length: "))
        breadth = float(input("Breadth: "))
        height = float(input("Height: "))
        c = Cuboid(None, None, None, select, length, breadth, height)
        print(c.cuboid_surface_area())

    elif select.strip().lower() == "surface area length":
        total_surface_area = float(input("Surface Area: "))
        breadth = float(input("Breadth: "))
        height = float(input("Height: "))
        c = Cuboid(total_surface_area, None, None, select, None, breadth, height)
        print(c.cuboid_surface_area_length())

    elif select.strip().lower() == "surface area width":
        total_surface_area = float(input("Surface Area: "))
        length = float(input("Length: "))
        height = float(input("Height: "))
        c = Cuboid(total_surface_area, None, None, select, length, None, height)
        print(c.cuboid_surface_area_width())

    elif select.strip().lower() == "surface area height":
        total_surface_area = float(input("Surface Area: "))
        length = float(input("Length: "))
        breadth = float(input("Breadth: "))
        c = Cuboid(total_surface_area, None, None, select, length, breadth, None)
        print(c.cuboid_surface_area_height())

    elif select.strip().lower() == "volume":
        length = float(input("Length: "))
        breadth = float(input("Breadth: "))
        height = float(input("Height: "))
        c = Cuboid(None, None, None, select, length, breadth, height)
        print(c.cuboid_volume())

    elif select.strip().lower() == "volume length":
        volume = float(input("Volume: "))
        breadth = float(input("Breadth: "))
        height = float(input("Height: "))
        c = Cuboid(None, volume, None, select, None, breadth, height)
        print(c.cuboid_volume_length())

    elif select.strip().lower() == "volume width":
        volume = float(input("Volume: "))
        length = float(input("Length: "))
        height = float(input("Height: "))
        c = Cuboid(None, volume, None, select, length, None, height)
        print(c.cuboid_volume_width())

    elif select.strip().lower() == "volume height":
        volume = float(input("Volume: "))
        length = float(input("Length: "))
        breadth = float(input("Breadth: "))
        c = Cuboid(None, volume, None, select, length, breadth, None)
        print(c.cuboid_volume_height())

    elif select.strip().lower() == "diagonal":
        length = float(input("Length: "))
        breadth = float(input("Breadth: "))
        height = float(input("Height: "))
        c = Cuboid(None, None, None, select, length, breadth, height)
        print(c.cuboid_diagonal())

    elif select.strip().lower() == "diagonal length":
        diagonal = float(input("Diagonal: "))
        breadth = float(input("Breadth: "))
        height = float(input("Height: "))
        c = Cuboid(None, None, diagonal, select, None, breadth, height)
        print(c.cuboid_diagonal_length())

    elif select.strip().lower() == "diagonal width":
        diagonal = float(input("Diagonal: "))
        length = float(input("Length: "))
        height = float(input("Height: "))
        c = Cuboid(None, None, diagonal, select, length, None, height)
        print(c.cuboid_diagonal_width())

    elif select.strip().lower() == "diagonal height":
        diagonal = float(input("Diagonal: "))
        length = float(input("Length: "))
        breadth = float(input("Breadth: "))
        c = Cuboid(None, None, diagonal, select, length, breadth, None)
        print(c.cuboid_diagonal_height())

    else: 
        print("ERROR, Invalid Input!")

except ValueError:
    print("ERROR, Invalid Input!")