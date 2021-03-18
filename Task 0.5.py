from math import sqrt

def area_of_a_triangle(side1,side2,side3):
    
    semi_perimeter = (side1 + side2 + side3)/2 
    area = round(sqrt((semi_perimeter*(semi_perimeter-side1)*(semi_perimeter-side2)*(semi_perimeter-side3))),2) 
   
    return area
    
print(area_of_a_triangle(50,50,50))
