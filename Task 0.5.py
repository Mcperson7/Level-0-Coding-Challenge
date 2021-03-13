from math import sqrt as s


def area_of_a_triangle(side1,side2,side3):
    
    perimeter = (side1 + side2 + side3)/2 
    area = round(s((perimeter*(perimeter-side1)*(perimeter-side2)*(perimeter-side3))),2) 
   
    print("The Area of this Triangle is: ", area)

side1 = int(input("Size of size side1: "))
side2 = int(input("Size of side side2: "))
side3 = int(input("Size of side side3: "))    
    
area_of_a_triangle(side1,side2,side3)
