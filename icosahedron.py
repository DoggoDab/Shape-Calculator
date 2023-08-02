import math

GREEN = '\033[32m'
RESET = '\033[0m'

try: 
    class Icosahedron():
        def __init__(self, volume, edge, surface_area, select):
            self.volume = volume
            self.edge = edge
            self.surface_area = surface_area
            self.select = select

        icosahedron_volume = lambda self: "V = {:.2f}".format((5 * (3 + math.sqrt(5))) / (12) * self.edge ** 3)
        icosahedron_volume_edge = lambda self: "a = {:.2f}".format(math.pow((9 * (self.volume) / (5) - 3 * math.sqrt(5) * (self.volume) / (5)), 1/3))
        icosahedron_surface_area = lambda self: "A = {:.2f}".format(5 * math.sqrt(3) * self.edge ** 2)
        icosahedron_surface_area_edge = lambda self: "a = {:.2f}".format(math.pow(3, 3/4) * math.sqrt((self.surface_area) / (45)))

    print(f"{GREEN}ICOSAHEDRON CALCULATOR{RESET}")
    options = [
        "volume", 
        "volume edge", 
        "surface area", 
        "surface area edge"
    ]
    print("\n".join([f"{j+1}. {key.title()}" for j, key in enumerate(options)]))
    select = str(input("Select one of the following: "))
    if select.strip().lower() == "volume":
        edge = float(input("Edge: "))
        i = Icosahedron(None, edge, None, select)
        print(i.icosahedron_volume())

    elif select.strip().lower() == "volume edge":
        volume = float(input("Volume: "))
        i = Icosahedron(volume, None, None, select)
        print(i.icosahedron_volume_edge())

    elif select.strip().lower() == "surface area":
        edge = float(input("Edge: "))
        i = Icosahedron(None, edge, None, select)
        print(i.icosahedron_surface_area())

    elif select.strip().lower() == "surface area edge":
        surface_area = float(input("Surface Area: "))
        i = Icosahedron(None, None, surface_area, select)
        print(i.icosahedron_surface_area_edge())

    else:
        print("ERROR, Invalid Input!")
except ValueError: 
    print("ERROR, Invalid Input!")