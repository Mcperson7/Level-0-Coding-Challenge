def max_number(num1,num2,num3):
    
    if num1 > num2 and num1 > num3:
        print (num)
    elif num2 > num3 and num2 > num1:
        print (num2)
    else:
        print (num3)

num1 = 89564
num2 = 78000
num3 = 745        
        
max_number(num1,num2,num3)

'''Below is the same updated fuction as top on
the only difference is that this one accepts user input'''

def max_number(num1,num2,num3):
    
    if num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    else:
        return num1
    
num1 = int(input("Enter the value of num1 "))
num2 = int(input("Enter the value of num2 "))
num3 = int(input("Enter the value of num3 "))

print("The Maximum Value is : ", maximum_num(num1,num2,num3))