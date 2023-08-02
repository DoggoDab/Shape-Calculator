import math

GREEN = '\033[32m'
RESET = '\033[0m'

try: 
    class Cube():
        def __init__(self, surface_area, edge, space_diagonal, volume, select, lateral):
            self.surface_area = surface_area
            self.edge = edge
            self.space_diagonal = space_diagonal
            self.volume = volume
            self.select = select
            self.lateral = lateral

        def cube_surface_area(self):
            return "A = {:.2f}".format(6 * self.edge ** 2)
        
        def cube_edge_area(self):
            return "a = {:.2f}".format(math.sqrt(self.surface_area / 6))
        
        def cube_space_diagonal(self):
            return "d = {:.2f}".format(math.sqrt(3) * self.edge)
        
        def cube_edge_diagonal(self):
            return "a = {:.2f}".format(math.sqrt(3) * self.space_diagonal / 3)
        
        def cube_volume(self):
            return "V = {:.2f}".format(self.edge ** 3)
        
        def cube_edge_volume(self):
            return "a = {:.2f}".format(math.pow(self.volume, 1/3))
        
        def cube_lateral(self):
            return "l = {:.2f}".format(4 * (self.edge) ** 2)
        
        def cube_edge_lateral(self):
            return "a = {:.2f}".format(2 * math.sqrt(self.lateral) / 4)
        
    print(f"{GREEN}CUBE CALCULATOR{RESET}")
    print("\n".join(["1. Surface Area", "2. Area Edge", "3. Space Diagonal", "4. Space Diagonal Edge", "5. Volume", "6. Volume Edge"]))
    select = str(input("Select one of the following: "))
    if select.strip().lower() == "surface area":
        edge = float(input("Edge: "))
        c = Cube(None, edge, None, None, select, None)
        print(c.cube_surface_area())

    elif select.strip().lower() == "area edge":
        surface_area = float(input("Surface Area: "))
        c = Cube(surface_area, None, None, None, select, None)
        print(c.cube_edge_area())

    elif select.strip().lower() == "space diagonal":
        edge = float(input("Edge: "))
        c = Cube(None, edge, None, None, select, None)
        print(c.cube_space_diagonal())

    elif select.strip().lower() == "space diagonal edge":
        space_diagonal = float(input("Space Diagonal: "))
        c = Cube(None, None, space_diagonal, None, select, None)
        print(c.cube_edge_diagonal())

    elif select.strip().lower() == "volume":
        edge = float(input("Edge: "))
        c = Cube(None, edge, None, None, select, None)
        print(c.cube_volume())

    elif select.strip().lower() == "volume edge":
        volume = float(input("Volume: "))
        c = Cube(None, None, None, volume, select, None)
        print(c.cube_edge_volume())

    elif select.strip().lower() == "lateral":
        edge = float(input("Edge: "))
        c = Cube(None, edge, None, None, select, None)
        print(c.cube_lateral())

    elif select.strip().lower() == "lateral edge":
        lateral = float(input("Lateral: "))
        c = Cube(None, None, None, None, select, lateral)
        print(c.cube_edge_lateral())

    else: 
        print("ERROR, Invalid Input!")

except ValueError:
    print("ERROR, Invalid Input!")