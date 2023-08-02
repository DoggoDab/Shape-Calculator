import math

GREEN = '\033[32m'
RESET = '\033[0m'

try: 
    class Sphere():
        def __init__(self, surface_area, radius, diameter, volume, select):
            self.surface_area = surface_area
            self.radius = radius
            self.diameter = diameter
            self.volume = volume
            self.select = select

        def sphere_surface_area(self):
            return "A = {:.2f}".format(4 * math.pi * self.radius ** 2)
        
        def sphere_surface_area_radius(self):
            return "r = {:.2f}".format(((1/2) * math.sqrt((self.surface_area) / (math.pi))))
        
        def sphere_diameter(self):
            return "d = {:.2f}".format(2 * self.radius)
        
        def sphere_diameter_radius(self):
            return "r = {:.2f}".format(self.diameter / 2)
        
        def sphere_volume(self):
            return "V = {:.2f}".format((4/3) * math.pi * self.radius ** 3)
        
        def sphere_volume_radius(self):
            return "r = {:.2f}".format((3 * self.volume / (4 * math.pi)) ** (1/3))
        
    print(f"{GREEN}SPHERE CALCULATOR{RESET}")
    print("\n".join(["1. Surface Area", "2. Surface Area Radius", "3. Diameter", "4. Diameter Radius", "5. Volume", "6. Volume Radius"]))
    select = str(input("Select one of the following: "))
    if select.strip().lower() == "surface area":
        radius = float(input("Radius: "))
        s = Sphere(None, radius, None, None, select)
        print(s.sphere_surface_area())

    elif select.strip().lower() == "surface area radius":
        surface_area = float(input("Surface Area: "))
        s = Sphere(surface_area, None, None, None, select)
        print(s.sphere_surface_area_radius())

    elif select.strip().lower() == "diameter":
        radius = float(input("Radius: "))
        s = Sphere(None, radius, None, None, select)
        print(s.sphere_diameter())

    elif select.strip().lower() == "diameter radius":
        diameter = float(input("Diameter: "))
        s = Sphere(None, None, diameter, None, select)
        print(s.sphere_diameter_radius())

    elif select.strip().lower() == "volume":
        radius = float(input("Radius: "))
        s = Sphere(None, radius, None, None, select)
        print(s.sphere_volume())

    elif select.strip().lower() == "volume radius":
        volume = float(input("Volume: "))
        s = Sphere(None, None, None, volume, select)
        print(s.sphere_volume_radius())

    else:
        print("ERROR, Invalid Input!")

except ValueError:
    print("ERROR, Invalid Input!")