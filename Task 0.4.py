def even_or_Odd(num):
    
    if num % 2 == 1:
        return "Odd number"
    else:
        return "Even number"

num = int(input("Enter a number to see if it's ODD or EVEN"))    
print(num,"is an: " + even_or_Odd(num))