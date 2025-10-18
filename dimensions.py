from math import ceil

def calc_package_dimensions(length, width, height, qty=1, padding=2):
    package_length = (length * qty) + padding * 2 #Issues fixed
    package_width  = width + padding * 2
    package_height = height + padding * 2
    volume = package_length * package_width * package_height
    return package_length, package_width, package_height, volume

if _name_ == "_main_":
    print("Enter item dimensions (L W H) in cm:")
    l, w, h = map(float, input().split())
    q = int(input("Quantity: "))
    p = float(input("Padding per side (default 2): ") or 2)
    result = calc_package_dimensions(l, w, h, q, p)
    print("Package (LxWxH):", result[:-1])
    print("Volume:", result[-1])