from math import sqrt as s

#The code below calculates Area of a triangle using Heron's Formula!!! 3 sided triangle
def area_of_a_triangle(x,y,z):
    
    i = (x + y + z)/2 #This Calculates Half Of Tringles Perimeter
    j = round(s((i*(i-x)*(i-y)*(i-z))),2) #We then find the area using this formula
   
    print("The Area of this Triangle is: ", j)

x = int(input("Size of size x: "))
y = int(input("Size of side y: "))
z = int(input("Size of side z: "))    
    
area_of_a_triangle(x,y,z)