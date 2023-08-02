import math

GREEN = '\033[32m'
RESET = '\033[0m'

try: 
    class Octahedron():
        def __init__(self, volume, edge, surface_area, select):
            self.volume = volume
            self.edge = edge
            self.surface_area = surface_area
            self.select = select

        octahedron_volume = lambda self: "V = {:.2f}".format((math.sqrt(2)) / (3) * self.edge ** 3)
        octahedron_volume_edge = lambda self: "a = {:.2f}".format(math.pow(2, 5/6) * math.pow((3 * (self.volume) / (8)), 1/3))
        octahedron_surface_area = lambda self: "A = {:.2f}".format(2 * math.sqrt(3) * self.edge ** 2)
        octahedron_surface_area_edge = lambda self: "a = {:.2f}".format(math.pow(3, 3/4) * math.sqrt((self.surface_area) / (18)))

    print(f"{GREEN}OCTAHEDRON CALCULATOR{RESET}")
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
        o = Octahedron(None, edge, None, select)
        print(o.octahedron_volume())

    elif select.strip().lower() == "volume edge":
        volume = float(input("Volume: "))
        o = Octahedron(volume, None, None, select)
        print(o.octahedron_volume_edge())

    elif select.strip().lower() == "surface area":
        edge = float(input("Edge: "))
        o = Octahedron(None, edge, None, select)
        print(o.octahedron_surface_area())

    elif select.strip().lower() == "surface area edge":
        surface_area = float(input("Surface Area: "))
        o = Octahedron(None, None, surface_area, select)
        print(o.octahedron_surface_area_edge())

    else: 
        print("ERROR, Invalid Input!")
except ValueError: 
    print("ERROR, Invalid Input!")