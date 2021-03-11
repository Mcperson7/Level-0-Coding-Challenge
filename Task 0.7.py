#Temperature calculator from celsius to fahrenheit

def celsius_to_fahrenheit(celsius):
        
    farh = round(((celsius * (9/5)) + 32),2)
    return str(farh) + " Fahrenheit" 

celsius = float(input("Please enter the Temparature in Celsius Degrees "))
print(celsius_to_fahrenheit(celsius))

#Different conversion, from fahrenheit to celsius

def fahrenheit_to_Cels(fahr):
    
    cels = round(((fahr - 32) / (9/5)),2)
    return str(cels) + " Degrees Celsius"

fahr = float(input("Please enter the Temparature in Fahrenheit Degrees "))
print(fahrenheit_to_Cels(fahr))