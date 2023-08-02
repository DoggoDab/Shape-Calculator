import math

GREEN = '\033[32m'
RESET = '\033[0m'

try: 
    class Dodecahedron():
        def __init__(self, volume, edge, surface_area, select):
            self.volume = volume
            self.edge = edge
            self.surface_area = surface_area
            self.select = select

        dodecahedron_volume = lambda self: "V = {:.2f}".format((15 + 7 * math.sqrt(5)) / (4) * self.edge ** 3)
        dodecahedron_volume_edge = lambda self: "a = {:.2f}".format(math.pow(2, 2/3) * math.pow(((self.volume) / (15 + math.sqrt(245))), 1/3))
        dodecahedron_surface_area = lambda self: "A = {:.2f}".format(3 * math.sqrt(25 + 10 * math.sqrt(5)) * self.edge ** 2)
        dodecahedron_surface_area_edge = lambda self: "a = {:.2f}".format(math.pow(5, 3/4) * (math.sqrt((self.surface_area) / (75))) / (math.pow((math.sqrt(20) + 5), 1/4)))

    print(f"{GREEN}DODECAHEDRON CALCULATOR{RESET}")
    options = [
        "volume", 
        "volume edge", 
        "surface area", 
        "surface area edge"
    ]
    print("\n".join([f"{i+1}. {key.title()}" for i, key in enumerate(options)]))
    select = str(input("Select one of the following: "))
    if select.strip().lower() == "volume":
        edge = float(input("Edge: "))
        d = Dodecahedron(None, edge, None, select)
        print(d.dodecahedron_volume())

    elif select.strip().lower() == "volume edge":
        volume = float(input("Volume: "))
        d = Dodecahedron(volume, None, None, select)
        print(d.dodecahedron_volume_edge())

    elif select.strip().lower() == "surface area":
        edge = float(input("Edge: "))
        d = Dodecahedron(None, edge, None, select)
        print(d.dodecahedron_surface_area())

    elif select.strip().lower() == "surface area edge":
        surface_area = float(input("Surface Area: "))
        d = Dodecahedron(None, None, surface_area, select)
        print(d.dodecahedron_surface_area_edge())

    else: 
        print("ERROR, Invalid Input!")
except ValueError:
    print("ERROR, Invalid Input!")