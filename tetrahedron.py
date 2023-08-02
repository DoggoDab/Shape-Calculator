import math

GREEN = '\033[32m'
RESET = '\033[0m'

try: 
    class Tetrahedron():
        def __init__(self, volume, edge, height, surface_area, face_area, select):
            self.volume = volume
            self.edge = edge
            self.height = height
            self.surface_area = surface_area
            self.face_area = face_area
            self.select = select

        tetrahedron_volume = lambda self: "V = {:.2f}".format((self.edge ** 3) / (6 * math.sqrt(2)))
        tetrahedron_volume_edge = lambda self: "a = {:.2f}".format(math.sqrt(2) * math.pow(3 * self.volume, 1/3))
        tetrahedron_height = lambda self: "h = {:.2f}".format(math.sqrt(2/3) * self.edge)
        tetrahedron_height_edge = lambda self: "a = {:.2f}".format(math.sqrt(6) * (self.height) / (2))
        tetrahedron_surface_area = lambda self: "A = {:.2f}".format(math.sqrt(3) * self.edge ** 2)
        tetrahedron_surface_area_edge = lambda self: "a = {:.2f}".format((1) / (3) * math.pow(3, 3/4) * math.sqrt(self.surface_area))
        tetrahedron_face_area = lambda self: "AF = {:.2f}".format((math.sqrt(3)) / (4) * self.edge ** 2)
        tetrahedron_face_area_edge = lambda self: "a = {:.2f}".format((2) / (3) * math.pow(3, 3/4) * math.sqrt(self.face_area))

    print(f"{GREEN}TETRAHEDRON CALCULATOR{RESET}")
    options = [
        "volume", 
        "volume edge", 
        "height", 
        "height edge", 
        "surface area", 
        "surface area edge", 
        "face area",
        "face area edge"
    ]
    print("\n".join([f"{i+1}. {key.title()}" for i, key in enumerate(options)]))
    select = str(input("Select one of the following: "))
    if select.strip().lower() == "volume":
        edge = float(input("Edge: "))
        t = Tetrahedron(None, edge, None, None, None, select)
        print(t.tetrahedron_volume())

    elif select.strip().lower() == "volume edge":
        volume = float(input("Volume: "))
        t = Tetrahedron(volume, None, None, None, None, select)
        print(t.tetrahedron_volume_edge())

    elif select.strip().lower() == "height":
        edge = float(input("Edge: "))
        t = Tetrahedron(None, edge, None, None, None, select)
        print(t.tetrahedron_height())

    elif select.strip().lower() == "height edge":
        height = float(input("Height: "))
        t = Tetrahedron(None, None, height, None, None, select)
        print(t.tetrahedron_height_edge())

    elif select.strip().lower() == "surface area":
        edge = float(input("Edge: "))
        t = Tetrahedron(None, edge, None, None, None, select)
        print(t.tetrahedron_surface_area())

    elif select.strip().lower() == "surface area edge":
        surface_area = float(input("Surface Area: "))
        t = Tetrahedron(None, None, None, surface_area, None, select)
        print(t.tetrahedron_surface_area_edge())

    elif select.strip().lower() == "face area":
        edge = float(input("Edge: "))
        t = Tetrahedron(None, edge, None, None, None, select)
        print(t.tetrahedron_face_area())

    elif select.strip().lower() == "face area edge":
        face_area = float(input("Face Area: "))
        t = Tetrahedron(None, None, None, None, face_area, select)
        print(t.tetrahedron_face_area_edge())

    else: 
        print("ERROR, Invalid Input!")
except ValueError:
    print("ERROR, Invalid Input!")