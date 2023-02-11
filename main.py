from graphics.rectangle import area, perimeter

length = int(input("Enter the Length : "))
breadth = int(input("Enter the Breadth : "))
radius = int(input("Enter the Radius :"))
width = int(input("Enter the Width : "))
height = int(input("Enter the Height :"))
area_rect = area(length, breadth)
print("\nThe Area of Rectangle is : ", area_rect)
peri_rect = perimeter(length, breadth)
print("The Perimeter of Rectangle is : ", peri_rect)
from graphics.circle import area, perimeter

area_cir = area(radius)
print("\nThe Area of Circle is : ", area_cir)
peri_cir = perimeter(radius)
print("The Perimeter of Circle is : ", peri_cir)
from graphics.graphics_3d.sphere import area, perimeter

area_sph = area(radius)
print("\nThe Area of Sphere is : ", area_sph)
peri_sph = perimeter(radius)
print("The Perimeter of Sphere is : ", peri_sph)
from graphics.graphics_3d.cuboid import area, perimeter

area_cub = area(length, width, height)
print("\nThe Area of Cuboid is : ", area_cub)
peri_cub = perimeter(length, width, height)
print("The Perimeter of Cuboid is : ", peri_cub)
