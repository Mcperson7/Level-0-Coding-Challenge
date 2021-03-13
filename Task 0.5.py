import math


def area_of_a_triangle(side1,side2,side3):
    
    semi_perimeter = (side1 + side2 + side3)/2 
    area = round(math.sqrt((semi_perimeter*(semi_perimeter-side1)*(semi_perimeter-side2)*(semi_perimeter-side3))),2) 
   
    print("The Area of this Triangle is: ", area)

side1 = int(input("Size of size side1: "))
side2 = int(input("Size of side side2: "))
side3 = int(input("Size of side side3: "))    
    
area_of_a_triangle(side1,side2,side3)
