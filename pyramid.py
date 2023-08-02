import math

GREEN = '\033[32m'
RESET = '\033[0m'

try: 
    class Pyramid():
        def __init__(self, volume, base_length, base_width, pyramid_height, surface_area, lateral_surface, base_area, select):
            self.volume = volume
            self.base_length = base_length
            self.base_width = base_width
            self.pyramid_height = pyramid_height
            self.surface_area = surface_area
            self.lateral_surface = lateral_surface
            self.base_area = base_area
            self.select = select

        pyramid_volume = lambda self: "V = {:.2f}".format((self.base_length * self.base_width * self.pyramid_height) / (3))
        pyramid_volume_base_length = lambda self: "l = {:.2f}".format(3 * (self.volume) / (self.pyramid_height * self.base_width))
        pyramid_volume_base_width = lambda self: "w = {:.2f}".format(3 * (self.volume) / (self.pyramid_height * self.base_length))
        pyramid_volume_pyramid_height = lambda self: "h = {:.2f}".format(3 * (self.volume) / (self.base_length * self.base_width))
        pyramid_surface_area = lambda self: "A = {:.2f}".format(self.base_length * self.base_width + self.base_length * math.sqrt(((self.base_width) / (2)) ** 2 + self.pyramid_height ** 2) + self.base_width * math.sqrt(((self.base_length) / (2)) ** 2 + self.pyramid_height ** 2))
        pyramid_surface_area_pyramid_height = lambda self: "h = {:.2f}".format(math.sqrt((self.base_length ** 4 * self.base_width ** 2 + self.base_length ** 2 * self.base_width ** 4 - 2 * self.surface_area * self.base_length ** 3 * self.base_width - 2 * self.surface_area * self.base_length * self.base_width ** 3 + (self.surface_area * self.base_length) ** 2 + (self.surface_area * self.base_width) ** 2 - math.sqrt((self.base_length * self.base_width) ** 2 * (self.base_length ** 6 * self.base_width ** 2 + 2 * (self.base_length * self.base_width) ** 4 + self.base_length ** 2 * self.base_width ** 6 - 2 * self.surface_area * self.base_length ** 5 * self.base_width - 12 * self.surface_area * (self.base_length * self.base_width) ** 3 - 2 * self.surface_area * self.base_length * self.base_width ** 5 + self.surface_area ** 2 * self.base_length ** 4 + 22 * (self.surface_area * self.base_length * self.base_width) ** 2 + self.surface_area ** 2 * self.base_width ** 4 - 16 * self.surface_area ** 3 * self.base_length * self.base_width + 4 * self.surface_area ** 4))) / (self.base_length ** 4 - 2 * (self.base_length * self.base_width) ** 2 + self.base_width ** 4)))
        pyramid_lateral_surface = lambda self: "AL = {:.2f}".format(self.base_length * math.sqrt(((self.base_width) / (2)) ** 2 + self.pyramid_height ** 2) + self.base_width * math.sqrt(((self.base_length) / (2)) ** 2 + self.pyramid_height ** 2)) 
        pyramid_lateral_surface_base_length_one = lambda self: "l = {:.2f}".format(math.sqrt((2 * self.pyramid_height ** 4 * self.base_width ** 2 + 2 * (self.lateral_surface * self.pyramid_height) ** 2 + (self.lateral_surface * self.base_width) ** 2 + math.sqrt(16 * self.pyramid_height ** 6 * (self.lateral_surface * self.base_width) ** 2 + 4 * self.lateral_surface ** 2 * (self.pyramid_height * self.base_width) ** 4 + 4 * self.lateral_surface ** 4 * (self.pyramid_height * self.base_width) ** 2 + (self.lateral_surface * self.base_width) ** 4)) / (2 * self.pyramid_height ** 4)))
        pyramid_lateral_surface_base_length_two = lambda self: "l = {:.2f}".format(math.sqrt(2) * (math.sqrt(2 * self.base_width ** 2 + 2 * ((self.lateral_surface) / (self.pyramid_height)) ** 2 + ((self.lateral_surface * self.base_width) ** 2) / (self.pyramid_height ** 4) - (math.sqrt(16 * self.pyramid_height ** 6 * (self.lateral_surface * self.base_width) ** 2 + 4 * self.lateral_surface ** 2 * (self.pyramid_height * self.base_width) ** 4 + 4 * self.lateral_surface ** 4 * (self.pyramid_height * self.base_width) ** 2 + (self.lateral_surface * self.base_width) ** 4)) / (self.pyramid_height ** 4))) / (2))
        pyramid_lateral_surface_base_width_one = lambda self: "w = {:.2f}".format(math.sqrt((2 * self.pyramid_height ** 4 * self.base_length ** 2 + 2 * (self.lateral_surface * self.pyramid_height) ** 2 + (self.lateral_surface * self.base_length) ** 2 + math.sqrt(16 * self.pyramid_height ** 6 * (self.lateral_surface * self.base_length) ** 2 + 4 * self.lateral_surface ** 2 * (self.pyramid_height * self.base_length) ** 4 + 4 * self.lateral_surface ** 4 * (self.pyramid_height * self.base_length) ** 2 + (self.lateral_surface * self.base_length) ** 4)) / (2 * self.pyramid_height ** 4)))
        pyramid_lateral_surface_base_width_two = lambda self: "w = {:.2f}".format(math.sqrt(2) * (math.sqrt(2 * self.base_length ** 2 + 2 * ((self.lateral_surface) / (self.pyramid_height)) ** 2 + ((self.lateral_surface * self.base_length) ** 2) / (self.pyramid_height ** 4) - (math.sqrt(16 * self.pyramid_height ** 6 * (self.lateral_surface * self.base_length) ** 2 + 4 * self.lateral_surface ** 2 * (self.pyramid_height * self.base_length) ** 4 + 4 * self.lateral_surface ** 4 * (self.pyramid_height * self.base_length) ** 2 + (self.lateral_surface * self.base_length) ** 4)) / (self.pyramid_height ** 4))) / (2))
        pyramid_lateral_surface_pyramid_height_one = lambda self: "h = {:.2f}".format(math.sqrt(((self.lateral_surface * self.base_length) ** 2) / (self.base_length ** 4 - 2 * (self.base_length * self.base_width) ** 2 + self.base_width ** 4) + ((self.lateral_surface * self.base_width) ** 2) / (self.base_length ** 4 - 2 * (self.base_length * self.base_width) ** 2 + self.base_width ** 4) + (math.sqrt(self.base_length * (self.lateral_surface * self.base_width) ** 2 - 2 * self.lateral_surface ** 2 * (self.base_length * self.base_width) ** 4 + self.base_width ** 6 * (self.lateral_surface * self.base_length) ** 2 + 4 * self.lateral_surface ** 4 * (self.base_length * self.base_width) ** 2)) / (self.base_length ** 4 - 2 * (self.base_length * self.base_width) ** 2 + self.base_width ** 4)))
        pyramid_base_area = lambda self: "AB = {:.2f}".format(self.base_length * self.base_width)
        pyramid_base_area_base_length = lambda self: "l = {:.2f}".format(self.base_area / self.base_width)
        pyramid_base_area_base_width = lambda self: "w = {:.2f}".format(self.base_area / self.base_length)

    print(f"{GREEN}PYRAMID CALCULATOR{RESET}")
    options = [
        "volume", 
        "volume base length", 
        "volume base width", 
        "volume pyramid height", 
        "surface area", 
        "surface area pyramid height", 
        "lateral surface", 
        "lateral surface base length", 
        "lateral surface base width", 
        "lateral surface pyramid height", 
        "base area", 
        "base area base length", 
        "base area base width"
    ]
    print("\n".join([f"{i+1}. {key.title()}" for i, key in enumerate(options)]))
    select = str(input("Select one of the following: "))
    if select.strip().lower() == "volume": 
        base_length = float(input("Base Length: "))
        base_width = float(input("Base Width: "))
        pyramid_height = float(input("Pyramid Height: "))
        p = Pyramid(None, base_length, base_width, pyramid_height, None, None, None, select)
        print(p.pyramid_volume())

    elif select.strip().lower() == "volume base length": 
        base_width = float(input("Base Width: "))
        pyramid_height = float(input("Pyramid Height: "))
        volume = float(input("Volume: "))
        p = Pyramid(volume, None, base_width, pyramid_height, None, None, None, select)
        print(p.pyramid_volume_base_length())

    elif select.strip().lower() == "volume base width": 
        base_length = float(input("Base Length: "))
        pyramid_height = float(input("Pyramid Height: "))
        volume = float(input("Volume: "))
        p = Pyramid(volume, base_length, None, pyramid_height, None, None, None, select)
        print(p.pyramid_volume_base_width())

    elif select.strip().lower() == "volume pyramid height": 
        base_length = float(input("Base Length: "))
        base_width = float(input("Base Width: "))
        volume = float(input("Volume: "))
        p = Pyramid(volume, base_length, base_width, None, None, None, None, select)
        print(p.pyramid_volume_pyramid_height())

    elif select.strip().lower() == "surface area": 
        base_length = float(input("Base Length: "))
        base_width = float(input("Base Width: "))
        pyramid_height = float(input("Pyramid Height: "))
        p = Pyramid(None, base_length, base_width, pyramid_height, None, None, None, select)
        print(p.pyramid_surface_area())

    elif select.strip().lower() == "surface area pyramid height": 
        base_length = float(input("Base Length: "))
        base_width = float(input("Base Width: "))
        surface_area = float(input("Surface Area: "))
        p = Pyramid(None, base_length, base_width, None, surface_area, None, None, select)
        print(p.pyramid_surface_area_pyramid_height())

    elif select.strip().lower() == "lateral surface": 
        base_length = float(input("Base Length: "))
        base_width = float(input("Base Width: "))
        pyramid_height = float(input("Pyramid Height: "))
        p = Pyramid(None, base_length, base_width, pyramid_height, None, None, None, select)
        print(p.pyramid_lateral_surface())

    elif select.strip().lower() == "lateral surface base length": 
        base_width = float(input("Base Width: "))
        pyramid_height = float(input("Pyramid Height: "))
        lateral_surface = float(input("Lateral Surface: "))
        p = Pyramid(None, None, base_width, pyramid_height, None, lateral_surface, None, select)
        print("\n".join(["There are two answers: ",f"{p.pyramid_lateral_surface_base_length_one()}", f"{p.pyramid_lateral_surface_base_length_two()}"]))

    elif select.strip().lower() == "lateral surface base width": 
        base_length = float(input("Base Length: "))
        pyramid_height = float(input("Pyramid Height: "))
        lateral_surface = float(input("Lateral Surface: "))
        p = Pyramid(None, base_length, None, pyramid_height, None, lateral_surface, None, select)
        print("\n".join(["There are two answers: ", f"{p.pyramid_lateral_surface_base_width_one()}", f"{p.pyramid_lateral_surface_base_width_two()}"]))

    elif select.strip().lower() == "lateral surface pyramid height": 
        base_length = float(input("Base Length: "))
        base_width = float(input("Base Width: "))
        lateral_surface = float(input("Lateral Surface: "))
        p = Pyramid(None, base_length, base_width, None, None, lateral_surface, None, select)
        print(p.pyramid_lateral_surface_pyramid_height_one())

    elif select.strip().lower() == "base area":  
        base_length = float(input("Base Length: "))
        base_width = float(input("Base Width: "))
        p = Pyramid(None, base_length, base_width, None, None, None, None, select)
        print(p.pyramid_base_area())

    elif select.strip().lower() == "base area base length": 
        base_width = float(input("Base Width: "))
        base_area = float(input("Base Area: "))
        p = Pyramid(None, None, base_width, None, None, None, base_area, select)
        print(p.pyramid_base_area_base_length())

    elif select.strip().lower() == "base area base width": 
        base_length = float(input("Base Length: "))
        base_area = float(input("Base Area: "))
        p = Pyramid(None, base_length, None, None, None, None, base_area, select)
        print(p.pyramid_base_area_base_width())

    else: 
        print("ERROR, Invalid Input!")
except ValueError:
    print("ERROR, Invalid Input!")