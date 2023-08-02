import math

GREEN = '\033[32m'
RESET = '\033[0m'

try: 
    class Cone():
        def __init__(self, volume, radius, height, slant_height, surface_area, lateral_surface, base_area, select):
            self.volume = volume
            self.radius = radius
            self.height = height
            self.slant_height = slant_height
            self.surface_area = surface_area
            self.lateral_surface = lateral_surface
            self.base_area = base_area
            self.select = select

        cone_volume = lambda self: "V = {:.2f}".format(math.pi * self.radius ** 2 * (self.height) / (3))
        cone_volume_radius = lambda self: "r = {:.2f}".format(math.sqrt(3 * (self.volume) / (math.pi * self.height)))
        cone_volume_height = lambda self: "h = {:.2f}".format(3 * (self.volume) / (math.pi * self.radius ** 2))
        cone_slant_height = lambda self: "l = {:.2f}".format(math.sqrt(self.radius ** 2 + self.height ** 2))
        cone_slant_height_radius = lambda self: "r = {:.2f}".format(math.sqrt(self.slant_height ** 2 - self.height ** 2))
        cone_slant_height_height = lambda self: "h = {:.2f}".format(math.sqrt(self.slant_height ** 2 - self.radius ** 2))
        cone_surface_area = lambda self: "A = {:.2f}".format(math.pi * self.radius * (self.radius + math.sqrt(self.height ** 2 + self.radius ** 2)))
        cone_surface_area_radius = lambda self: "r = {:.2f}".format(math.sqrt((self.surface_area ** 2) / (math.pi * (math.pi * self.height ** 2 + 2 * self.surface_area))))
        cone_surface_area_height = lambda self: "h = {:.2f}".format(math.sqrt(self.surface_area * ((self.surface_area) / (self.radius ** 2) - 2 * math.pi)) / (math.pi))
        cone_lateral_surface = lambda self: "AL = {:.2f}".format(math.pi * self.radius * math.sqrt(self.height ** 2 + self.radius ** 2))
        cone_lateral_surface_radius = lambda self: "r = {:.2f}".format((math.sqrt(2 * math.sqrt(math.pi ** 2 * self.height ** 4 + 4 * self.lateral_surface ** 2) - 2 * math.pi * self.height ** 2)) / (2 * math.sqrt(math.pi)))
        cone_lateral_surface_height = lambda self: "h = {:.2f}".format((math.sqrt(((self.lateral_surface) / (self.radius)) ** 2 - (math.pi * self.radius) ** 2) / (math.pi))) 
        cone_base_area = lambda self: "AB = {:.2f}".format(math.pi * self.radius ** 2)
        cone_base_area_radius = lambda self: "r = {:.2f}".format(math.sqrt((self.base_area) / (math.pi)))

    print(f"{GREEN}CONE CALCULATOR{RESET}")
    options = [
        "volume", 
        "volume radius", 
        "volume height", 
        "slant height", 
        "slant height radius", 
        "slant height height",
        "surface area", 
        "surface area radius", 
        "surface area height", 
        "lateral surface", 
        "lateral surface radius", 
        "lateral surface height", 
        "base area", 
        "base area radius"
    ]
    print("\n".join([f"{i+1}. {key.title()}" for i, key in enumerate(options)]))
    select = str(input("Select one of the following: "))
    if select.strip().lower() == "volume":
        radius = float(input("Radius: "))
        height = float(input("Height: "))
        c = Cone(None, radius, height, None, None, None, None, select)
        print(c.cone_volume())

    elif select.strip().lower() == "volume radius":
        height = float(input("Height: "))
        volume = float(input("Volume: "))
        c = Cone(volume, None, height, None, None, None, None, select)
        print(c.cone_volume_radius())

    elif select.strip().lower() == "volume height":
        radius = float(input("Radius: "))
        volume = float(input("Volume: "))
        c = Cone(volume, radius, None, None, None, None, None, select)
        print(c.cone_volume_height())

    elif select.strip().lower() == "slant height":
        radius = float(input("Radius: "))
        height = float(input("Height: "))
        c = Cone(None, radius, height, None, None, None, None, select)
        print(c.cone_slant_height())

    elif select.strip().lower() == "slant height radius":
        height = float(input("Height: "))
        slant_height = float(input("Slant Height: "))
        c = Cone(None, None, height, slant_height, None, None, None, select)
        print(c.cone_slant_height_radius())

    elif select.strip().lower() == "slant height height":
        radius = float(input("Radius: "))
        slant_height = float(input("Slant Height: "))
        c = Cone(None, radius, None, slant_height, None, None, None, select)
        print(c.cone_slant_height_height())

    elif select.strip().lower() == "surface area":
        radius = float(input("Radius: "))
        height = float(input("Height: "))
        c = Cone(None, radius, height, None, None, None, None, select)
        print(c.cone_surface_area())

    elif select.strip().lower() == "surface area radius":
        height = float(input("Height: "))
        surface_area = float(input("Surface Area: "))
        c = Cone(None, None, height, None, surface_area, None, None, select)
        print(c.cone_surface_area_radius())

    elif select.strip().lower() == "surface area height":
        radius = float(input("Radius: "))
        surface_area = float(input("Surface Area: "))
        c = Cone(None, radius, None, None, surface_area, None, None, select)
        print(c.cone_surface_area_height())

    elif select.strip().lower() == "lateral surface":
        radius = float(input("Radius: "))
        height = float(input("Height: "))
        c = Cone(None, radius, height, None, None, None, None, select)
        print(c.cone_lateral_surface())

    elif select.strip().lower() == "lateral surface radius":
        height = float(input("Height: "))
        lateral_surface = float(input("Lateral Surface: "))
        c = Cone(None, None, height, None, None, lateral_surface, None, select)
        print(c.cone_lateral_surface_radius())

    elif select.strip().lower() == "lateral surface height":
        radius = float(input("Radius: "))
        lateral_surface = float(input("Lateral Surface: "))
        c = Cone(None, radius, None, None, None, lateral_surface, None, select)
        print(c.cone_lateral_surface_height())

    elif select.strip().lower() == "base area":
        radius = float(input("Radius: "))
        c = Cone(None, radius, None, None, None, None, None, select)
        print(c.cone_base_area())

    elif select.strip().lower() == "base area radius":
        base_area = float(input("Base Area: "))
        c = Cone(None, None, None, None, None, None, base_area, select)
        print(c.cone_base_area_radius())

    else: 
        print("ERROR, Invalid Input!")
except ValueError:
    print("ERROR, Invalid Input!")