import math
 
latitude_one = float(input("Input the latitude of coordinate 1: "))
longitude_one = float(input("Input the longitude of coordinate 1:"))
latitude_two = float(input("Input the latitude of coordinate 2: "))
longitude_two = float(input("Input the longitude of coordinate 2: "))
radius = 6371.01

latitude_one = math.radians(latitude_one)
latitude_two = math.radians(latitude_two)
longitude_one = math.radians(longitude_one)
longitude_two = math.radians(longitude_two)



distance = radius * math.acos(math.sin(latitude_one) * math.sin(latitude_two) + math.cos(latitude_one) * math.cos(latitude_two) * math.cos(longitude_one - longitude_two))

print(f"The distance between those points is: {distance:.4f}km")