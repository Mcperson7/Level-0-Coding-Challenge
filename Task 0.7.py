#Temperature calculator from celsius to fahrenheit

def celsius_to_fahrenheit(celsius):
        
    farh = round(((celsius * (9/5)) + 32),2)
    return farh

print(celsius_to_fahrenheit(54))

#Different conversion, from fahrenheit to celsius

def fahrenheit_to_Cels(fahr):
    
    cels = round(((fahr - 32) / (9/5)),2)
    return cels


print(fahrenheit_to_Cels(129.2))