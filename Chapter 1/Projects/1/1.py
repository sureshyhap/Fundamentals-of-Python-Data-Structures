"""
Reports relevant values of a sphere
given the radius.
"""

from math import pi

def main():
    """Gets the radius of a sphere and outputs relevant values."""
    radius = float(input("Enter a radius of a sphere: "))
    diameter = radius * 2
    circumference = 2 * pi * radius
    surface_area = 4 * pi * (radius ** 2)
    volume = (4 / 3) * pi * (radius ** 3)
    print(f"Diameter: {diameter}")
    print(f"Circumference: {circumference}")
    print(f"Surface Area: {surface_area}")
    print(f"Volume: {volume}")
    
    
if __name__ == "__main__":
    main()
