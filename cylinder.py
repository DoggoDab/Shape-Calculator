import math

GREEN = '\033[32m'
RESET = '\033[0m'

try: 
    class Cylinder():
        def __init__(self, volume, radius, height, diameter, surface_area, lateral, base):
            self.volume = volume
            self.radius = radius
            self.height = height
            self.diameter = diameter
            self.surface_area = surface_area
            self.lateral = lateral
            self.base = base

        cylinder_volume = lambda self: "V = {:.2f}".format(math.pi * self.radius ** 2 * self.height)
        cylinder_volume_radius = lambda self: "r = {:.2f}".format(math.sqrt((self.volume) / (math.pi * self.height)))
        cylinder_volume_height = lambda self: "h = {:.2f}".format((self.volume) / (math.pi * self.radius ** 2))
        cylinder_diameter = lambda self: "d = {:.2f}".format(2 * math.sqrt((self.volume) / (math.pi * self.height)))
        cylinder_diameter_height = lambda self: "h = {:.2f}".format((self.volume) / (math.pi * ((self.diameter) / (2)) ** 2))
        cylinder_diameter_volume = lambda self: "V = {:.2f}".format(math.pi * ((self.diameter) / (2)) ** 2 * self.height)
        cylinder_surface_area = lambda self: "A = {:.2f}".format(2 * math.pi * self.radius * self.height + 2 * math.pi * 2 ** 2)
        cylinder_surface_area_radius = lambda self: "r = {:.2f}".format((1/2) * math.sqrt(self.height ** 2 + 2 * (self.surface_area) / (math.pi)) - (self.height) / (2))
        cylinder_surface_area_height = lambda self: "h = {:.2f}".format((self.surface_area) / (2 * math.pi * self.radius) - self.radius)
        cylinder_lateral = lambda self: "AL = {:.2f}".format(2 * math.pi * self.radius * self.height)
        cylinder_lateral_radius = lambda self: "r = {:.2f}".format((self.lateral) / (2 * math.pi * self.height))
        cylinder_lateral_height = lambda self: "h = {:.2f}".format((self.lateral) / (2 * math.pi * self.radius))
        cylinder_base = lambda self: "AB = {:.2f}".format(math.pi * self.radius ** 2)
        cylinder_base_radius = lambda self: "r = {:.2f}".format(math.sqrt((self.base) / (math.pi)))

    print(f"{GREEN}CYLINDER CALCULATOR{RESET}")
    options = [
        "volume",
        "volume radius",
        "volume height",
        "diameter",
        "diameter height",
        "diameter volume",
        "surface area",
        "surface area radius",
        "surface area height",
        "lateral surface",
        "lateral surface radius",
        "lateral surface height",
        "base area",
        "base area radius",
    ]
    print("\n".join([f"{i+1}. {key.title()}" for i, key in enumerate(options)]))
    select = str(input("Select one of the following: ")).strip().lower()

    if select.strip().lower() == "volume":
        radius = float(input("Radius: "))
        height = float(input("Height: "))
        c = Cylinder(None, radius, height, None, None, None, None)
        print(c.cylinder_volume())

    elif select.strip().lower() == "volume radius":
        height = float(input("Height: "))
        volume = float(input("Volume: "))
        c = Cylinder(volume, None, height, None, None, None, None)
        print(c.cylinder_volume_radius())

    elif select.strip().lower() == "volume height":
        radius = float(input("Radius: "))
        volume = float(input("Volume: "))
        c = Cylinder(volume, radius, None, None, None, None, None)
        print(c.cylinder_volume_height())

    elif select.strip().lower() == "diameter":
        height = float(input("Height: "))
        volume = float(input("Volume: "))
        c = Cylinder(volume, None, height, None, None, None, None)
        print(c.cylinder_diameter())

    elif select.strip().lower() == "diameter height":
        diameter = float(input("Diameter: "))
        volume = float(input("Volume: "))
        c = Cylinder(volume, None, None, diameter, None, None, None)
        print(c.cylinder_diameter_height())

    elif select.strip().lower() == "diameter volume":
        diameter = float(input("Diameter: "))
        height = float(input("Height: "))
        c = Cylinder(None, None, height, diameter, None, None, None)
        print(c.cylinder_diameter_volume())

    elif select.strip().lower() == "surface area":
        radius = float(input("Radius: "))
        height = float(input("Height: "))
        c = Cylinder(None, radius, height, None, None, None, None)
        print(c.cylinder_surface_area())

    elif select.strip().lower() == "surface area radius":
        height = float(input("Height: "))
        surface_area = float(input("Surface Area: "))
        c = Cylinder(None, None, height, None, surface_area, None, None)
        print(c.cylinder_surface_area_radius())

    elif select.strip().lower() == "surface area height":
        radius = float(input("Radius: "))
        surface_area = float(input("Surface Area: "))
        c = Cylinder(None, radius, None, None, surface_area, None, None)
        print(c.cylinder_surface_area_height())

    elif select.strip().lower() == "lateral surface":
        radius = float(input("Radius: "))
        height = float(input("Height: "))
        c = Cylinder(None, radius, height, None, None, None, None,)
        print(c.cylinder_lateral())

    elif select.strip().lower() == "lateral surface radius":
        height = float(input("Height: "))
        lateral = float(input("Lateral Surface: "))
        c = Cylinder(None, None, height, None, None, lateral, None)
        print(c.cylinder_lateral_radius())

    elif select.strip().lower() == "lateral surface height":
        radius = float(input("Radius: "))
        lateral = float(input("Lateral Surface: "))
        c = Cylinder(None, radius, None, None, None, lateral, None)
        print(c.cylinder_lateral_height())

    elif select.strip().lower() == "base area":
        radius = float(input("Radius: "))
        c = Cylinder(None, radius, None, None, None, None, None)
        print(c.cylinder_base())

    elif select.strip().lower() == "base area radius":
        base = float(input("Base: "))
        c = Cylinder(None, None, None, None, None, None, base)
        print(c.cylinder_base_radius())

    else: 
        print("ERROR, Invalid Input!")

except ValueError:
    print("ERROR, Invalid Input!")