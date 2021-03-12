from math import sqrt as s

#The code below calculates Area of a triangle using Heron's Formula!!! 3 sided triangle
def area_of_a_triangle(side1,side2,side3):
    
    i = (side1 + side2 + side3)/2 #This Calculates Half Of Tringles Perimeter
    j = round(s((i*(i-side1)*(i-side2)*(i-side3))),2) #We then find the area using this formula
   
    print("The Area of this Triangle is: ", j)

side1 = int(input("Size of size side1: "))
side2 = int(input("Size of side side2: "))
side3 = int(input("Size of side side3: "))    
    
area_of_a_triangle(side1,side2,side3)
