def number_to_time_converter():
    
    hour = num // 60
    minut = num % 60
    
    if num <= 60 and num > 0 and minut <= 1:
        return str(hour) + " hour, " + str(minut)+" minute"
    elif num <= 60 and minut > 1:
        return str(hour)+ " hour, " + str(minut) + " minutes"
    elif num >= 60 and num < 120 and minut <= 1:
        return str(hour) + " hour, " + str(minut)+" minute"
    elif num >= 60 and num < 120 and minut >=1:
        return str(hour)+ " hour, " + str(minut) + " minutes"
    elif num >= 120 and minut <= 1:
        return str(hour) +" hours, " + str(minut) + " minute"
    else:
        return str(hour) +" hours, " + str(minut) + " minutes"

num = int(input("Enter any number to get it converted to time: "))    
print(num, "Converted to time is: ", number_to_time_converter())