def max_number(a,b,c):
    
    if a > b and a > c:
        print (a)
    elif b > c and b > a:
        print (b)
    else:
        print (c)

a = 89564
b = 78000
c = 745        
        
max_number(a,b,c)

'''Below is the same updated fuction as top on
the only difference is that this one accepts user input'''

def maximum_num(a,b,c):
    
    if b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        return a
    
a = int(input("Enter the value of a "))
b = int(input("Enter the value of b "))
c = int(input("Enter the value of c "))

print("The Maximum Value is : ", maximum_num(a,b,c))